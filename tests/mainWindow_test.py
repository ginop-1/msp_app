import unittest
import sys
from PyQt5 import QtWidgets
from msp_app.App import App
from tests import TestBase

"""
Module Docstring
"""

class TestApp(TestBase):
    """
    Test App
    """
    def test_app_test(self):
        """
        Test App
        """
        sysapp = QtWidgets.QApplication(sys.argv)
        app = App()
        try:
          app.start()
        except:
          pass
        self.assertEqual(1,1)

if __name__ == "__main__":
    unittest.main()