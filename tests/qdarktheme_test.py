import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from msp_app.ui.generated.about_dialog_ui import CustomDialog
import qdarktheme
from tests import TestBase
import unittest

"""
Module Docstring
"""

class TestDarkTheme(TestBase):
    """
    Test About Dialog
    """
    def test_dark_theme(self):
        """
        Test About Dialog
        """
        
        app = QApplication(sys.argv)
        main_win = QMainWindow()
        push_button = QPushButton("PyQtDarkTheme!!")
        main_win.setCentralWidget(push_button)

        # Apply dark theme
        app.setStyleSheet(qdarktheme.load_stylesheet())

        main_win.show()

        app.exec()
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()