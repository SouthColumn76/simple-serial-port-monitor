from email.charset import QP
from logging import logThreads
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QComboBox
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QTextBrowser
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout

class SerialPortWindow(QWidget):
    def __init__(self, parent=None, serialInfo=None, serialPortConnector=None) -> None:
        super().__init__(parent)

        self.callbacks = [] # has comboboxes's currentIndex()
        self.SerialPort = serialPortConnector
        self.SerialPort.setPrinter(self.printText)

        layout = QVBoxLayout()

        # Print logs(received, system messages)
        self.logText = QTextBrowser()
        
        # Serial Port Setting
        _port   = self.makeSettingField("Port",         serialInfo.getPorts())
        _rate   = self.makeSettingField("Baud rate",    serialInfo.getBaudRates())
        _data   = self.makeSettingField("Data bits",    serialInfo.getDataBits())
        _parity = self.makeSettingField("Parity",       serialInfo.getParities())
        _flow   = self.makeSettingField("Flow control", serialInfo.getFlowControls())
        _stop   = self.makeSettingField("Stop bits",    serialInfo.getStopBits())

        setting_col1 = QVBoxLayout()
        setting_col1.addLayout(_port)
        setting_col1.addLayout(_parity)

        setting_col2 = QVBoxLayout()
        setting_col2.addLayout(_rate)
        setting_col2.addLayout(_flow)

        setting_col3 = QVBoxLayout()
        setting_col3.addLayout(_data)
        setting_col3.addLayout(_stop)

        self.connect_button = QPushButton("Open")
        self.connect_button.clicked.connect(self.portConnect)
        self.isConnected = False

        setting = QHBoxLayout()
        setting.addLayout(setting_col1)
        setting.addLayout(setting_col2)
        setting.addLayout(setting_col3)
        setting.addWidget(self.connect_button)

        self.sendText = QLineEdit()
        self.sendText.editingFinished.connect(self.textEnter)

        check = QPushButton("Send")
        check.clicked.connect(self.textEnter)

        layout.addWidget(self.logText)
        layout.addLayout(setting)
        layout.addWidget(self.sendText)
        layout.addWidget(check)

        self.setLayout(layout)

    def makeSettingField(self, label:str, items:tuple) -> QHBoxLayout:
        layout = QHBoxLayout()

        _label = QLabel(label)

        _combobox = QComboBox()
        for item in items:
            _combobox.addItem(item)

        self.callbacks.append(_combobox.currentIndex)

        layout.addWidget(_label)
        layout.addWidget(_combobox)
        return layout

    def textEnter(self) -> None:
        message = self.sendText.text()
        if not message == '':
            self.sendText.clear()
            self.send(message)
    
    
    def portConnect(self) -> None:
        if self.isConnected:
            self.SerialPort.close()
            self.printText("-------DisConnected-------")
            self.connect_button.setText("Open")
            self.isConnected = False
            
        else:
            isConnected, message = self.SerialPort.connect(self.callbacks)
            if isConnected:
                self.printText(message)
                self.connect_button.setText("Close")
                self.isConnected = True
            else:
                self.printText(message)

    def send(self, message:str) -> None:
        self.SerialPort.send(message)
        self.printText(message)

    def printText(self, message:str) -> None:
        self.logText.append(message)
