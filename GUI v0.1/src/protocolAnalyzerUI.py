from ui_protocolAnalyzerUI import Ui_mainWindow
from PySide6.QtWidgets import QMainWindow
import numpy as np

class analyzerUI(QMainWindow):
    def __init__(self):
        super(analyzerUI, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)



class I2CAnalyzer():
    def decode(self, data:list[list[int]], edges:list[list[dict]], SCK:int, SDA:int, samplingFrequency:int):
        # Checks to guarantee success in decoding
        if len(data) == 0 or data == []:
            raise AnalyzerError("No data to analyze!")
        if SCK == SDA:
            raise AnalyzerError("multiple roles assigned to the same channel!")
        if len(edges[SDA]) <= 10:
            return []
        decodedFrames = []
        distances = np.array([])
        numberOfEdges = len(edges[SCK])
        if numberOfEdges <= 10:
            return []

        for index in range(1, numberOfEdges):
            distanceBetweenEdges = edges[SCK][index]["1"] - edges[SCK][index-1]["1"]
            distances = np.append(arr=distances, values=distanceBetweenEdges)

        unique, counts = np.unique(distances, return_counts=True)
        indexMostRepetitions = np.argmax(counts)
        edgeDistance = unique[indexMostRepetitions]


        print("La frecuencia entre flancos mas común es %s muestras con %s ocurrencias" %(unique[indexMostRepetitions], counts[indexMostRepetitions]))
        # Get START conditions
        # Get START in SCK
        frameBeginCandidates = [edges[SCK][0]] if edges[SCK][0]["type"] == "F" else []
        for index in range(1, len(edges[SCK])):
            if edges[SCK][index]["type"] == "F" and (abs(edges[SCK][index]["1"]-edges[SCK][index-1]["1"]) > 3*edgeDistance):
                frameBeginCandidates.append(edges[SCK][index])
        # Confirm with SDA
        frameBeginnings = []
        for frameCandidate in frameBeginCandidates:
            for edge in edges[SDA]:
                tempDist = frameCandidate["1"]-edge["1"]
                if edge["type"] == "F" and (tempDist) < 3*edgeDistance and tempDist > 0:
                    frameBeginnings.append(frameCandidate)
                    break
        # Get STOP conditions
        # Get STOP in SCK
        frameEndCandidates = []
        for index in range(0, len(edges[SCK])-1):
            if edges[SCK][index]["type"] == "R" and (abs(edges[SCK][index]["1"]-edges[SCK][index+1]["1"]) > 3*edgeDistance):
                frameEndCandidates.append(edges[SCK][index])
        
        if edges[SCK][-1]["type"] == "R":
            frameEndCandidates.append(edges[SCK][-1])
        
        frameEnds = []
        for frameCandidate in frameEndCandidates:
            for edge in edges[SDA]:
                tempDist = edge["1"] - frameCandidate["1"]
                if edge["type"] == "R" and (tempDist) < 3*edgeDistance and tempDist > 0:
                    frameEnds.append(frameCandidate)
                    break

        if frameBeginnings[0]["1"] > frameEnds[0]["1"]:
            frameEnds.pop(0)
        if frameBeginnings[-1]["1"] > frameEnds[-1]["1"]:
            frameBeginnings.pop(-1)
        
        if len(frameEnds) != len(frameBeginnings):
            print("Problemas de reconocimiento")
            return []
        else:
            
            for i, framebeginning in enumerate(frameBeginnings):
                frameAddress = ""
                frameData = ""
                edgeSelector = edges[SCK].index(framebeginning)+1
                frameEndIndex = edges[SCK].index(frameEnds[i])
                counter = 0
                for _ in range(0, 9):
                    frameAddress += str(data[SDA][edges[SCK][edgeSelector]["2"]])
                    edgeSelector += 2
                
                tempList = self.interpretAddressFrame(frameAddress)
                decodedFrames.append(I2CFrame(start=framebeginning["1"],
                                    end=edges[SCK][edgeSelector-1]["2"], 
                                    message=tempList[0], 
                                    addressOrData="A", 
                                    readOrWrite=tempList[1], 
                                    acknowledge=tempList[2]))


                while edgeSelector < frameEndIndex: 
                    frameData += str(data[SDA][edges[SCK][edgeSelector]["2"]])
                    edgeSelector += 2
                    if counter == 8:
                        decodedFrames.append(I2CFrame(start=edges[SCK][edgeSelector-18]["2"],
                                    end=edges[SCK][edgeSelector]["2"], 
                                    message=frameData[0:8], 
                                    addressOrData="D", 
                                    readOrWrite=None, 
                                    acknowledge=True if frameData[8] == '0' else False))
                        counter=0
                    counter += 1
                
            for frame in decodedFrames:
                print("Desde: %s" %(frame.start*(1000/samplingFrequency)))
                print("Direccion") if frame.addressOrData == "A" else print("Datos")
                print(frame.toLabelText(format="dec"))
                print("Hasta: %s" %(frame.end*(1000/samplingFrequency)))
                print("------------------------------------")
            
                

class SPIAnalyzer():
    def decode(self, data:list[list[int]], edges:list[list[dict]], SCK:int, MOSI:int, MISO:int, CS:int, spiMode:int, reverseBits:bool, samplingFrequency:int):
        # A list of used channels, as chip select is optional (as an analyzer feature)
        usedChannels = []
        for role in [SCK, MOSI, MISO, CS]:
            if role is not None:
                usedChannels.append(role)
        # Checks to guarantee success in decoding
        if len(data) == 0 or data == []:
            raise AnalyzerError("No data to analyze!")
        if spiMode not in [0,1,2,3]:
            raise AnalyzerError("spiMode must be 0,1,2 or 3!")
        if not all(((0 <= value < len(data))) for value in usedChannels):
            raise AnalyzerError("decoded channels must be sampled channels!")
        if not (len(usedChannels) == len(set(usedChannels))):
            raise AnalyzerError("multiple roles assigned to the same channel!")
        
        # If no edges are detected on SCK, return empty list
        distances = np.array([])
        numberOfEdges = len(edges[SCK])
        if numberOfEdges == 0:
            return []
        decodedFrames = []
        # What to look for according to SPI mode
        samplingEdgeType = "R" if spiMode in [0,3] else "F"
        frameBeginEdgeType = "R" if spiMode in [0,1] else "F"

        # Get the distances between edges in an effort to decipher the clock frequency
        # as it is not defined in the protocol
        for index in range(1, numberOfEdges):
            distanceBetweenEdges = edges[SCK][index]["1"] - edges[SCK][index-1]["1"]
            distances = np.append(arr=distances, values=distanceBetweenEdges)
        
        # Get most common ocurrance of distance between edges, measured in samples
        unique, counts = np.unique(distances, return_counts=True)
        indexMostRepetitions = np.argmax(counts)
        edgeDistance = unique[indexMostRepetitions]
        
        # Define what will be recognized as half a period of CLK
        lowerToleranceDistance = np.floor(0.9*edgeDistance)
        upperToleranceDistance = np.ceil(1.1*edgeDistance)
        
        # Now is time to search for frames, first edge is always a candidate 
        frameStartEdgesCandidates = [0]
        # Filter for chip select if desired
        # An edge will be a frame start candidate if the distance to the previous edge 
        # is more than the tolerated half period
        if CS is None:
            for index in range(1, numberOfEdges):
                distanceBetweenEdges = edges[SCK][index]["1"] - edges[SCK][index-1]["1"]
                if (abs(distanceBetweenEdges) > upperToleranceDistance) and (edges[SCK][index]["type"] == frameBeginEdgeType):
                    frameStartEdgesCandidates.append(index)
        else:
            for index in range(1, numberOfEdges):
                distanceBetweenEdges = edges[SCK][index]["1"] - edges[SCK][index-1]["1"]
                if (abs(distanceBetweenEdges) > upperToleranceDistance) and (edges[SCK][index]["type"] == frameBeginEdgeType) and (data[CS][edges[SCK][index]["1"]] == 0):
                    frameStartEdgesCandidates.append(index)
        

        frameStarts = []
        addEdge = False

        # Now, to really determine if the candidate is a frame, we will check that the following
        # 16 edges are more or less on par with the tolerated frequency/period
        for edgeIndex in frameStartEdgesCandidates:
            # Check if frame was not full captured
            if edgeIndex+15 >= len(edges[SCK]):
                break
            for i in range(1, 16):
                newDistance = abs(edges[SCK][edgeIndex+i]["1"] - edges[SCK][edgeIndex+i-1]["1"])
                if ((newDistance > lowerToleranceDistance) and (newDistance < upperToleranceDistance)):
                    addEdge = True
                    continue
                else:
                    addEdge = False
                    break
            if addEdge:
                frameStarts.append(edgeIndex)
        
        SPIMsg = ""
        # Finally, with the frames located, decode on the corresponding channel and edges
        if MOSI:
            for frameStart in frameStarts:
                SPIMsg = ""
                if frameStart+15 >= len(edges[SCK]):
                    break
                for i in range(1, 16):
                    if edges[SCK][frameStart+i]["type"] == samplingEdgeType:
                        SPIMsg += str(data[MOSI][edges[SCK][frameStart+i]["1"]])
                if reverseBits:
                    SPIMsg = SPIMsg[::-1]
                decodedFrames.append(SPIFrame(start=edges[SCK][frameStart]["1"],end=edges[SCK][frameStart+15]["1"], message=SPIMsg, MISOOrMOSI="MOSI"))
        if MISO:
            for frameStart in frameStarts:
                SPIMsg = ""
                if frameStart+15 >= len(edges[SCK]):
                    break
                for i in range(1, 16):
                    if edges[SCK][frameStart+i]["type"] == samplingEdgeType:
                        SPIMsg += str(data[MISO][edges[SCK][frameStart+i]["1"]])
                if reverseBits:
                    SPIMsg = SPIMsg[::-1]
                decodedFrames.append(SPIFrame(start=edges[SCK][frameStart]["1"],end=edges[SCK][frameStart+15]["1"], message=SPIMsg, MISOOrMOSI="MISO"))
        
        for frame in decodedFrames:
            print("Desde: %s" %(frame.start*(1000/samplingFrequency)))
            print(frame.toLabelText(format="ascii"))
            print("Hasta: %s" %(frame.end*(1000/samplingFrequency)))
            print("------------------------------------")

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
        decodedFrames = []
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
        for frameBeginning in frameBegginings:
            # If frame was not captured completly (too close to the end), end the decoding process
            if int(np.ceil(frameBeginning+((dataBits+0.5)*UARTPeriodInSamples))) > (len(data[txLine])-1):
                break
            # Decode and reverse
            UARTMsg = ""
            parityBit = ""
            for i in range(1, dataBits+1):
                UARTMsg += (str(data[txLine][int(np.ceil(frameBeginning+((i+0.5)*UARTPeriodInSamples)))]))
            UARTMsg = UARTMsg[::-1]
            # Check for parity bits
            if parityBits == None:
                parityCheck = None
            if parityBits == "even":
                parityBit = str(data[txLine][int(np.ceil(frameBeginning+((dataBits+1.5)*UARTPeriodInSamples)))])
                fullMsg = UARTMsg + parityBit
                if (fullMsg.count('1') % 2) == 0:
                    parityCheck = True
                else:
                    parityCheck = False
            elif parityBits == "odd":
                parityBit = str(data[txLine][int(np.ceil(frameBeginning+((dataBits+1.5)*UARTPeriodInSamples)))])
                fullMsg = UARTMsg + parityBit
                if (fullMsg.count('1') % 2) != 0:
                    parityCheck = True
                else:
                    parityCheck = False
            decodedFrames.append(UARTFrame(start=frameBeginning,end=frameBeginning+UARTFrameLengthInSamples,message=UARTMsg,parityBit=parityBit,parityOk=parityCheck))
        for frame in decodedFrames:
            print("Desde: %s" %(frame.start*(1000/samplingFrequency)))
            print(frame.toLabelText(format="dec"))
            print("Hasta: %s" %(frame.end*(1000/samplingFrequency)))
            print("------------------------------------")

'''
Esta clase tengo que actualizar luego
'''
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

class Frame():
    '''
    ---------- Description ----------
    Frame is a base class to be inherited by other classes to represent decoded frames
    ---------- Attributes ----------
    start : 'int', the sample where the frame starts
    end : 'int', the sample where the frame ends
    '''
    def __init__(self, start:int, end:int) -> None:
        self.start = start
        self.end = end

    def toLabelText(self):
        '''
        Create a string for the signs that go above the signals
        '''
        pass

    def toTableRows(self):
        '''
        Create strings to be placed in the Frames table 
        '''
        pass

    def binaryStringToFormat(self, data:str, format="dec") -> str:
        '''
        ---------- Description ----------
        Transform a string containing ones and zeroes to the selected format. 
        ---------- Attributes ----------
        format : 'str'. Formats accepted are: "bin", "dec", "hex" or "ascii". defaults to "dec". 
        ---------- Returns ----------
        'str'. Binary converted to the desired format as a string.
        '''
        result = ""
        # Just in case
        try:
            if format == "bin":
                result = ("0b%s" %data)
            elif format == "dec":
                result = ("%s" %int(data, 2))
            elif format == "hex":
                result = ("%s" %hex(int(data, 2)))
            elif format == "ascii":
                if len(data) <= 8:
                    result = ("%s" %chr((int(data, 2))))
                else:
                    result = ("%s" %chr((int(data[1:9], 2))))
        except:
            result = ""
        return result

class UARTFrame(Frame):
    '''
    ---------- Description ----------
    UARTFrame is a class to represent decoded Frames. It is intended to have all its 
    attributes loaded on instantiation, usually after the Frame is decoded
    ---------- Attributes ----------
    message : 'str', the original message ones and zeros decoded from the captured signal
    parityBit : 'str', the parity bit from the Frame, as captured
    parityOk : 'bool', an indicator to tell if the parityBit is correct
    '''
    def __init__(self, start:int, end:int, message:str, parityBit:str, parityOk:bool):
        super().__init__(start=start, end=end)
        self.message = message
        self.parityBit = parityBit
        self.parityOk = parityOk

    def toLabelText(self,format:str):
        self.binaryStringToFormat(data=self.message, format=format)
        return
    
    def toTableRow():
        pass

class SPIFrame(Frame):
    '''
    ---------- Description ----------
    SPIFrame is a class to represent decoded Frames. It is intended to have all its 
    attributes loaded on instantiation, usually after the Frame is decoded
    ---------- Attributes ----------
    message : 'str', the original message ones and zeros decoded from the captured signal
    MISOOrMOSI : 'str, "MISO" or "MOSI" if the message was written by master or slave
    '''
    def __init__(self, start:int, end:int, message:str, MISOOrMOSI:str):
        super().__init__(start=start, end=end)
        self.message = message
        self.MISOOrMOSI = MISOOrMOSI

    def toLabelText(self, format:str):
        self.binaryStringToFormat(data=self.message, format=format)
        return
    
    def toTableRow():
        pass

class I2CFrame(Frame):
    '''
    ---------- Description ----------
    I2CFrame is a class to represent decoded Frames. It is intended to have all its 
    attributes loaded on instantiation, usually after the Frame is decoded
    ---------- Attributes ----------
    message : 'str', the original message ones and zeros decoded from the captured signal
    addressOrData : 'str', "A" for address, "D" for data
    readOrWrite : 'str',  "R" for read, "W" for write
    acknowledge : 'bool', flag indicating if message was acknowledged
    '''
    def __init__(self, start:int, end:int, message:str, addressOrData:str, readOrWrite:str,  acknowledge:bool) -> None:
        super().__init__(start=start, end=end)
        self.message = message
        self.addressOrData = addressOrData
        if addressOrData == "A":
            self.readOrWrite = readOrWrite
        else:
            self.readOrWrite = None
        self.acknowledge = acknowledge

    def toLabelText(self, format="dec") -> str:
        '''
        ---------- Description ----------
        Create a string for the signs that go above the signals. Addresses are always 
        shown in decimal format.
        '''
        text = ""
        if self.addressOrData == "A":
            format = "dec"
        
        text = self.binaryStringToFormat(data=self.message, format=format) + "+"
        
        if self.readOrWrite != None and self.addressOrData == "A":
            text += self.readOrWrite + "+"
        
        if self.acknowledge:
            text += "ACK"  
        else:
            text += "NACK"

        return text
    
    def toTableRow():
        pass

class AnalyzerError(Exception):
    pass
        
