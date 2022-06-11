from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from typing import Text
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QApplication, QLabel, QWidget, QComboBox, QTextEdit, QLineEdit
import sys

from PyQt5.QtCore import  QObject, QThread, pyqtSignal # Threading Classes

from MainPage import Ui_MainWindow

from azure.iot.device import IoTHubDeviceClient, Message

import json

class Worker(QtCore.QThread):

    any_signal = QtCore.pyqtSignal(int)

    def __init__(self, QLineEdit, ConnectionString):

        super(QtCore.QThread, self).__init__()

        self.textEditforIncomingMessages = QLineEdit

        self.CONNECTION_STRING = ConnectionString

    
    def message_handler(self, message):

        print("BURAYA GELDI 1")

        messageComesFromAzure = str(message)

        messageComesFromAzure = list(messageComesFromAzure.split(","))

        print(messageComesFromAzure)

        self.textEditforIncomingMessages.setText(messageComesFromAzure[1])

    def run(self):

        self.ClientAzure = IoTHubDeviceClient.create_from_connection_string(self.CONNECTION_STRING)
        print(self.CONNECTION_STRING)
        print("BURAYA GELDI 2")

        while True:

            self.ClientAzure.on_message_received = self.message_handler
    
class ConnectorApp(Ui_MainWindow, QMainWindow, QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.AzureMessages = self.ui.lne_IncomingMessages

        self.ui.btn_StartCommunicate.clicked.connect(self.startCommunicate)

        self.ui.btn_SendMessage.clicked.connect(self.sendMessagetoAzure)

        self.thread=None

    def startCommunicate(self):
        # Run long task

        self.CONNECTION_STRING = self.ui.lne_ConnectionString.text()

        self.thread = Worker(QLineEdit=self.AzureMessages, ConnectionString= self.CONNECTION_STRING)

        self.thread.start()

    def sendMessagetoAzure(self):

        self.CONNECTION_STRING2 = self.ui.lne_ConnectionString.text()

        self.ClientAzure2 = IoTHubDeviceClient.create_from_connection_string(self.CONNECTION_STRING2)
        
        lneInput = self.ui.lne_SendData.text()

        DATA_MESSAGE = {"type":"data", "data":lneInput}

        DATA_MESSAGE = json.dumps(DATA_MESSAGE)

        self.ClientAzure2.send_message(DATA_MESSAGE)
        


if __name__ == "__main__":

    app = QApplication(sys.argv)

    app.setApplicationDisplayName("Azure IoT Hub Connector")

    MainWindow = ConnectorApp()

    MainWindow.show()

    sys.exit(app.exec_())

# from azure.iot.device import IoTHubDeviceClient, Message

# import json

# denemeClient = IoTHubDeviceClient.create_from_connection_string("HostName=tutorial-iot-raspberrypi.azure-devices.net;DeviceId=myPi;SharedAccessKey=qrnNfkAz+haJrrz+EmBSGMZS5qGAtBVW8d7BM1otY3g=")

# message = Message("Selam")

# ERROR_MESSAGE = {"type":"error", "data":"connect error"}

# ERROR_MESSAGE = json.dumps(ERROR_MESSAGE)

# denemeClient.send_message(ERROR_MESSAGE)