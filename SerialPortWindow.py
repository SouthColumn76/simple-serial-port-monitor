from email.charset import QP
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QVBoxLayout

class SerialPortWindow(QWidget):
    def __init__(self, parent=None, serialInfo=None) -> None:
        super().__init__(parent)

        self.callbacks = [] # has comboboxes's currentIndex()

        _port   = self.makeSettingField("Port",         serialInfo.getPorts())
        _rate   = self.makeSettingField("Baud rate",    serialInfo.getBaudRates())
        _data   = self.makeSettingField("Data bits",    serialInfo.getDataBits())
        _parity = self.makeSettingField("Parity",       serialInfo.getParities())
        _flow   = self.makeSettingField("Flow control", serialInfo.getFlowControls())
        _stop   = self.makeSettingField("Stop bits",    serialInfo.getStopBits())

        layout = QVBoxLayout()
        layout.addLayout(_port)
        layout.addLayout(_rate)
        layout.addLayout(_data)
        layout.addLayout(_parity)
        layout.addLayout(_flow)
        layout.addLayout(_stop)

        check = QPushButton("Check")
        check.clicked.connect(self.printSettings)
        layout.addWidget(check)

        self.setLayout(layout)

    def makeSettingField(self, label:str, items:tuple) -> QHBoxLayout:
        layout = QHBoxLayout()

        _label = QLabel(label)

        _combobox = QComboBox()
        for item in items:
            _combobox.addItem(item)

        self.callbacks.append(_combobox.currentText)

        layout.addWidget(_label)
        layout.addWidget(_combobox)
        return layout
    
    def printSettings(self) -> None:
        text = ''
        for func in self.callbacks:
            text += func()
            text += ' '
        print(text)