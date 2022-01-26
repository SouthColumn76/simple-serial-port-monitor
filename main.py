import sys

from PySide2.QtWidgets import QApplication
from SerialPortWindow import SerialPortWindow
from SerialPortFunction import SerialInfo, SerialPortConnecter

if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = SerialPortWindow(serialInfo=SerialInfo(), serialPortConnector=SerialPortConnecter())
    view.show()

    sys.exit(app.exec_())