from ui_protocolAnalyzerUI import Ui_mainWindow
from PySide6.QtWidgets import QMainWindow
import numpy as np

class analyzerUI(QMainWindow):
    def __init__(self):
        super(analyzerUI, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

class UARTAnalyzer():
    allowedBaudRates = [300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200, 250000]
    allowedDataBits = [5, 6, 7, 8, 9]
    allowedStopBits = [1, 2]
    allowedParityBits = [None, "even", "odd"]
    def decode(self, data:list[list[int]], edges:list[dict], txLine:int, baudRate:int, dataBits:int, parityBits:str, stopBits:int, samplingFrequency:int):
        if len(data) == 0 or data == []:
            raise AnalyzerError("No data to analyze!")
        if txLine > len(data)-1:
            raise AnalyzerError("txLine argument must be a sampled channel!")
        if baudRate not in self.allowedBaudRates:
            raise AnalyzerError("baudRate argument invalid!")
        if dataBits not in self.allowedDataBits:
            raise AnalyzerError("dataBits argument invalid!")
        if parityBits not in self.allowedParityBits:
            raise AnalyzerError("parityBits argument invalid!")
        if stopBits not in self.allowedStopBits:
            raise AnalyzerError("stopBits argument invalid!")
        if samplingFrequency < 0:
            raise AnalyzerError("samplingFrequency argument invalid!")
        
        UARTPeriodInSamples = np.floor((1/baudRate)/(1/samplingFrequency)) # samples/baud
        UARTFrameLength = 1 + dataBits + (1 if (parityBits is not None) else 0) + stopBits  # start bit + databits+ paritybits+ 
        UARTFrameLengthInSamples = UARTFrameLength*UARTPeriodInSamples
        
        frameCandidates = []
        frameBegginings = []
        messages = []
        # look for frames, check for falling edges first
        for edge in edges[txLine]:
            if edge["type"] == "F":
                frameCandidates.append(edge["1"])
        # No messages
        if frameCandidates == []:
            return frameCandidates
        # Check for start condition, clear edges subsequent to the first edge that are closer than a frame's length
        lastBeggining = None
        for index, candidate in enumerate(frameCandidates):
            if index == 0:
                lastBeggining = candidate
                frameBegginings.append(candidate)
            elif candidate < lastBeggining+(UARTFrameLengthInSamples-(0.5*UARTPeriodInSamples)):
                pass
            else:
                lastBeggining = candidate
                frameBegginings.append(candidate)
        # Read the data and decode
        for fb in frameBegginings:
            # If frame was not captured completly (too close to the end), end the decoding process
            if int(np.ceil(fb+((dataBits+0.5)*UARTPeriodInSamples))) > (len(data[txLine])-1):
                break
            # Decode and reverse
            UARTMsg = ''
            for i in range(1, dataBits+1):
                UARTMsg += (str(data[txLine][int(np.ceil(fb+((i+0.5)*UARTPeriodInSamples)))]))
            UARTMsg = UARTMsg[::-1]
            # Check for parity bits
            if parityBits == None:
                parityResult = ""
            if parityBits == "even":
                parityBit = str(data[txLine][int(np.ceil(fb+((dataBits+1.5)*UARTPeriodInSamples)))])
                fullMsg = UARTMsg + parityBit
                if (fullMsg.count('1') % 2) == 0:
                    parityResult = "POK"
                else:
                    parityResult = "PNOK"
            elif parityBits == "odd":
                parityBit = str(data[txLine][int(np.ceil(fb+((dataBits+1.5)*UARTPeriodInSamples)))])
                fullMsg = UARTMsg + parityBit
                if (fullMsg.count('1') % 2) != 0:
                    parityResult = "POK"
                else:
                    parityResult = "PNOK"
            messages.append(["%s" %chr((int(UARTMsg, 2))), parityResult])
            #print("Decoded Binary : %s" %UARTMsg)
        print(messages)


class PlainBinaryAnalyzer():
    def decode(self, data:list[list[int]], format:str, reverse:bool):
        if len(data) == 0 or data == []:
            raise AnalyzerError("No data to analyze!")
        
        binaryValues = []
        returnList = []
        for index in range(len(data[0])):
            binaryStr = ''
            for channel in data:
                binaryStr += str(channel[index])
            if reverse:
                binaryValues.append(binaryStr[::-1])
            else:
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
        
