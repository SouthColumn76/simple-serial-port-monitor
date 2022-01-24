import PySide6


from PySide6.QtSerialPort import QSerialPort

class SerialInfo():
    Ports = (
        "COM1",
        "COM2",
        "COM3",
        "COM4")
    BaudRates = (
        QSerialPort.Baud1200,
        QSerialPort.Baud2400,
        QSerialPort.Baud4800,
        QSerialPort.Baud9600,
        QSerialPort.Baud19200,
        QSerialPort.Baud38400,
        QSerialPort.Baud57600,
        QSerialPort.Baud115200)
    DataBits = (
        QSerialPort.Data5,
        QSerialPort.Data6,
        QSerialPort.Data7,
        QSerialPort.Data8)
    Direction = (
        QSerialPort.Input,
        QSerialPort.Output,
        QSerialPort.AllDirections)
    FlowControl = (
        QSerialPort.NoFlowControl,
        QSerialPort.HardwareControl,
        QSerialPort.SoftwareControl)
    Parity = (
        QSerialPort.NoParity,
        QSerialPort.EvenParity,
        QSerialPort.OddParity,
        QSerialPort.SpaceParity,
        QSerialPort.MarkParity)
    StopBits = (
        QSerialPort.OneStop,
        QSerialPort.OneAndHalfStop,
        QSerialPort.TwoStop)
    
    def __init__(self) -> None:
        pass

    def getPorts(self) -> tuple:
        return self.Ports
    def getBaudRates(self) -> tuple:
        return ("1200", "2400", "4800", "9600",
                "19200", "38400", "57600", "115200")
    def getDataBits(self) -> tuple:
        return ("5", "6", "7", "8")
    def getDirections(self) -> tuple:
        return ("Input", "Output", "All Directions")
    def getFlowControls(self) -> tuple:
        return ("No", "Hardware", "Software")
    def getParities(self) -> tuple:
        return ("No", "Even", "Odd", "Space", "Mark")
    def getStopBits(self) -> tuple:
        return ("1", "1.5", "2")