from ..generated.main_window_ui import Ui_MainWindow
from ..generated.about_dialog_ui import CustomDialog
from ...serial_test import SerialConnection
from ...Worker import Worker

import serial.tools.list_ports
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QThread

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.conn = None
        self.setupUi(self)
        ports = serial.tools.list_ports.comports()

        self.actionAbout.triggered.connect(self.about)
        self.ConnectButton.pressed.connect(self.connect_serial)
        self.readButton.pressed.connect(self.append_text)
        self.AutomaticReadButton.pressed.connect(self.start_automatic_read_mode)
        self.StopAutomaticReadModeButton.pressed.connect(self.stop_automatic_read_mode)

        self.PortsComboBox.addItems([f"{port.device} - {port.description}" for port in ports])

    def start_automatic_read_mode(self):
        self.StopAutomaticReadModeButton.setEnabled(True)
        self.AutomaticReadButton.setEnabled(False)
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.append_text)
        # Step 6: Start the thread
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
        self.conn = SerialConnection(port=port)
        self.ConnectButton.setText("Connected")
        self.ConnectButton.setEnabled(False)

    def append_text(self):
        if not self.conn:
            return
        try:
            temperature = self.conn.read().split("\n")[-2]
        except AttributeError:
            return
        self.textBrowser.append(temperature)
