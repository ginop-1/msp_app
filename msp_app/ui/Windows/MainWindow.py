from ..generated.main_window_ui import Ui_MainWindow
from ..generated.about_dialog_ui import CustomDialog
from ...SerialConnection import SerialConnection
from ...Worker import Worker

import serial.tools.list_ports
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_ports)
        self.conn = None
        self.setupUi(self)

        self.setWindowIcon(QIcon("./msp_app/ui/imgs/icon.png"))
        self.setup_connectors()
        self.update_ports()

    def disable_buttons(self):
        self.ConnectButton.setEnabled(False)
        self.readButton.setEnabled(False)
        self.ClearButton.setEnabled(False)
        self.AutomaticReadButton.setEnabled(False)
        self.StopAutomaticReadModeButton.setEnabled(False)

    def setup_connectors(self):
        self.actionAbout.triggered.connect(self.about)
        self.ConnectButton.pressed.connect(self.connect_serial)
        self.readButton.pressed.connect(self.append_text)
        self.AutomaticReadButton.pressed.connect(self.start_automatic_read_mode)
        self.StopAutomaticReadModeButton.pressed.connect(self.stop_automatic_read_mode)

    def update_ports(self):
        ports = serial.tools.list_ports.comports()
        self.PortsComboBox.clear()
        self.PortsComboBox.addItems([f"{port.device} - {port.description}" for port in ports])
        if self.PortsComboBox.currentText() == "":
            self.disable_buttons()
            self.timer.start(3000)
        else:
            self.ConnectButton.setText("Connect")
            self.ConnectButton.setEnabled(True)
            self.readButton.setEnabled(True)
            self.ClearButton.setEnabled(True)
            self.AutomaticReadButton.setEnabled(True)
            self.timer.stop()

    def start_automatic_read_mode(self):
        self.StopAutomaticReadModeButton.setEnabled(True)
        self.AutomaticReadButton.setEnabled(False)
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.append_text)
        self.thread.start()

        # Final resets
        self.thread.finished.connect(
            lambda: self.StopAutomaticReadModeButton.setEnabled(False)
        )
        self.thread.finished.connect(
            lambda: self.AutomaticReadButton.setEnabled(True)
        )

    def stop_automatic_read_mode(self):
        self.worker.stop()

    def about(self):
        dlg = CustomDialog()
        dlg.exec_()

    def connect_serial(self):
        if self.conn:
            return
        port = self.PortsComboBox.currentText().split(" - ")[0]
        try:
            self.conn = SerialConnection(port=port)
        except Exception:
            self.ConnectButton.setText("No ports available")
            self.ConnectButton.setEnabled(False)
            self.PortsComboBox.clear()
            self.timer.start(3000)
            return
        self.ConnectButton.setText("Connected")
        self.ConnectButton.setEnabled(False)

    def append_text(self):
        if not self.conn:
            return
        try:
            temperature = self.conn.read().split("\n")[-2]
        except AttributeError:
            return
        except OSError:
            self.worker.stop()
            self.ConnectButton.setText("No ports available")
            self.ConnectButton.setEnabled(False)
            self.PortsComboBox.clear()
            self.timer.start(3000)
            return
        self.textBrowser.append(temperature)
