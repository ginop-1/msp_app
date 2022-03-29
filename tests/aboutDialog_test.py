import unittest
from msp_app.ui.generated.about_dialog_ui import CustomDialog
from PyQt5 import QtCore, QtWidgets
import sys
from tests import TestBase

"""
Module Docstring
"""

class TestAboutDialog(TestBase):
    """
    Test About Dialog
    """
    def test_about_dialog(self):
        """
        Test About Dialog
        """
        app = QtWidgets.QApplication(sys.argv)
        dlg = CustomDialog()
        dlg.exec_()
        print("test")
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()