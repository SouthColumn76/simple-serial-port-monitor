from PySide2.QtSerialPort import QSerialPort
from PySide2.QtCore import QByteArray

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

    ErrorMessages = {
        QSerialPort.NoError:"No Error",
        QSerialPort.DeviceNotFoundError:"Can Not Found Device",
        QSerialPort.PermissionError:"No Permissions Allowed",
        QSerialPort.OpenError:"Port Already Open"
    }
    
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

class SerialPortConnecter:
    def __init__(self) -> None:
        self.printer = None
        self.SerialPort = QSerialPort()
        self.SerialInfo = SerialInfo()

    def connect(self, callbacks:list) -> tuple:
        indices = []
        for func in callbacks:
            indices.append(func())
        self.SerialPort.setPortName(self.SerialInfo.Ports[indices[0]])
        self.SerialPort.setBaudRate(self.SerialInfo.BaudRates[indices[1]])
        self.SerialPort.setDataBits(self.SerialInfo.DataBits[indices[2]])
        self.SerialPort.setParity(self.SerialInfo.Parity[indices[3]])
        self.SerialPort.setFlowControl(self.SerialInfo.FlowControl[indices[4]])
        self.SerialPort.setStopBits(self.SerialInfo.StopBits[indices[5]])
        
        if not self.SerialPort.open(self.SerialPort.OpenModeFlag.ReadWrite) :
            err = self.SerialPort.error()
            if err in SerialInfo.ErrorMessages:
                return False, SerialInfo.ErrorMessages[err]
            else:
                return False, "Unkown Error"
        else:
            self.SerialPort.readyRead.connect(self.receive)
            return  True, "Connected: " + self.SerialInfo.Ports[indices[0]]
    
    def send(self, message:str) -> None:
        data = QByteArray(message.encode())
        self.SerialPort.write(data)

    def receive(self) -> None:
        if self.printer != None:
            data = self.SerialPort.readAll()
            message = bytes(data).decode()
            if message != '':
                self.printer(">> " + message)

    def close(self) -> None:
        if self.SerialPort.isOpen():
            self.SerialPort.close()

    def setPrinter(self, callback) -> None:
        self.printer = callback