# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 518)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 260, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 60, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_StartCommunicate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_StartCommunicate.setGeometry(QtCore.QRect(240, 160, 221, 32))
        self.btn_StartCommunicate.setObjectName("btn_StartCommunicate")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(240, 300, 221, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lne_SendData = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lne_SendData.setObjectName("lne_SendData")
        self.horizontalLayout_2.addWidget(self.lne_SendData)
        self.btn_SendMessage = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_SendMessage.setObjectName("btn_SendMessage")
        self.horizontalLayout_2.addWidget(self.btn_SendMessage)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 200, 421, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 360, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(200, 110, 271, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lne_ConnectionString = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lne_ConnectionString.setObjectName("lne_ConnectionString")
        self.horizontalLayout_3.addWidget(self.lne_ConnectionString)
        self.lne_IncomingMessages = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_IncomingMessages.setGeometry(QtCore.QRect(250, 410, 181, 21))
        self.lne_IncomingMessages.setObjectName("lne_IncomingMessages")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Send Message to Azure IoT Hub"))
        self.label.setText(_translate("MainWindow", "Azure IoT Hub Connector"))
        self.btn_StartCommunicate.setText(_translate("MainWindow", "Start Communicate with Azure"))
        self.btn_SendMessage.setText(_translate("MainWindow", "Send Message"))
        self.label_2.setText(_translate("MainWindow", "Device Connection State :"))
        self.label_3.setText(_translate("MainWindow", "Communication is not provided yet"))
        self.label_4.setText(_translate("MainWindow", "Incoming Data From Azure IoT Hub"))
        self.label_6.setText(_translate("MainWindow", "Connection String :"))
