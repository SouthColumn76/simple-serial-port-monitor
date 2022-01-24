import sys

from PySide6.QtWidgets import QApplication

from SerialPortWindow import SerialPortWindow
from SerialInfo import SerialInfo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = SerialPortWindow(serialInfo=SerialInfo())
    view.show()

    sys.exit(app.exec())