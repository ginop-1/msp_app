import sys
from PyQt5.QtWidgets import QApplication
from msp_app.ui.Windows.MainWindow import MainWindow

class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

    def start(self):
        self.main_window = MainWindow()
        self.main_window.show()
        sys.exit(self.exec_())

if __name__ == "__main__":
    app = App(sys.argv)
    app.start()