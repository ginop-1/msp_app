from PyQt5.QtWidgets import QApplication
import sys
import qdarktheme
from msp_app.ui.Windows.MainWindow import MainWindow


class App():
    def __init__(self):
        self.sysApp = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.sysApp.setStyleSheet(qdarktheme.load_stylesheet("light"))

    def start(self):
        self.main_window.show()
        sys.exit(self.sysApp.exec_())
