from ui_protocolAnalyzerUI import Ui_mainWindow
from PySide6.QtWidgets import QMainWindow


class analyzerUI(QMainWindow):
    def __init__(self):
        super(analyzerUI, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)


class plainBinaryAnalyzer():
    def decode(data:list, format:str):
        if len(data) == 0:
            raise AnalyzerError("No data to analyze!")
        
        binaryValues = []
        returnList = []
        for index in range(len(data[0])):
            binaryStr = ''
            for channel in data:
                binaryStr += str(channel[index])
            binaryValues.append(binaryStr)

        
        if format == 'bin':
            returnList.append(("0b%s" %binaryValues[0]))
            for index in range(1, len(binaryValues)):
                if binaryValues[index] != binaryValues[index-1]:
                    returnList.append(("0b%s" %binaryValues[index]))
            return returnList
        elif format == 'dec':
            returnList.append(("%s" %int(binaryValues[0], 2)))
            for index in range(1, len(binaryValues)):
                if binaryValues[index] != binaryValues[index-1]:
                    returnList.append(("%s" %(int(binaryValues[index], 2))))
            return returnList
        elif format == 'hex':
            returnList.append(("%s" %hex(int(binaryValues[0], 2))))
            for index in range(1, len(binaryValues)):
                if binaryValues[index] != binaryValues[index-1]:
                    returnList.append(("%s" %(hex(int(binaryValues[index], 2)))))
            return returnList
        elif format == 'ascii':
            returnList.append(("%s" %chr((int(binaryStr, 2)))))
            for index in range(1, len(binaryValues)):
                if binaryValues[index] != binaryValues[index-1]:
                    returnList.append(("%s" %chr((int(binaryStr, 2)))))
            return returnList
        else:
            raise AnalyzerError("The [%s] 'format' argument is unsupported" %format)


class AnalyzerError(Exception):
    pass
        
