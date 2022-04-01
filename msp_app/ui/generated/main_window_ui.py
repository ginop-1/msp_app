# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msp_app/ui/raw/window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 532)
        MainWindow.setStyleSheet("border: 10px solid transparent;")
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ConnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectButton.setStyleSheet("")
        self.ConnectButton.setDefault(True)
        self.ConnectButton.setFlat(False)
        self.ConnectButton.setObjectName("ConnectButton")
        self.horizontalLayout.addWidget(self.ConnectButton)
        self.PortsComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.PortsComboBox.setObjectName("PortsComboBox")
        self.horizontalLayout.addWidget(self.PortsComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setStyleSheet("")
        self.ClearButton.setAutoDefault(False)
        self.ClearButton.setDefault(False)
        self.ClearButton.setObjectName("ClearButton")
        self.horizontalLayout_2.addWidget(self.ClearButton)
        self.readButton = QtWidgets.QPushButton(self.centralwidget)
        self.readButton.setStyleSheet("")
        self.readButton.setDefault(False)
        self.readButton.setObjectName("readButton")
        self.horizontalLayout_2.addWidget(self.readButton)
        self.AutomaticReadButton = QtWidgets.QPushButton(self.centralwidget)
        self.AutomaticReadButton.setStyleSheet("")
        self.AutomaticReadButton.setDefault(False)
        self.AutomaticReadButton.setFlat(False)
        self.AutomaticReadButton.setObjectName("AutomaticReadButton")
        self.horizontalLayout_2.addWidget(self.AutomaticReadButton)
        self.StopAutomaticReadModeButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopAutomaticReadModeButton.setEnabled(False)
        self.StopAutomaticReadModeButton.setStyleSheet("")
        self.StopAutomaticReadModeButton.setDefault(False)
        self.StopAutomaticReadModeButton.setObjectName("StopAutomaticReadModeButton")
        self.horizontalLayout_2.addWidget(self.StopAutomaticReadModeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 52))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SMP_CONNECTOR"))
        self.ConnectButton.setText(_translate("MainWindow", "Connect MSP"))
        self.ClearButton.setText(_translate("MainWindow", "clear ouput"))
        self.readButton.setText(_translate("MainWindow", "read serial"))
        self.AutomaticReadButton.setText(_translate("MainWindow", "Activate automatic read mode"))
        self.StopAutomaticReadModeButton.setText(_translate("MainWindow", "Stop"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
