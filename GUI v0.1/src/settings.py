from enum import Enum

class SamplingMode(Enum):
    DIGITAL = 0
    ANALOG = 1

class SamplingSettings():
    
    samplingFrequenciesLUT = [1000,2500,5000,10000,25000,50000,100000,250000,500000,1000000,2500000,5000000,10000000,25000000,50000000,100000000,125000000]

    def __init__(self):
        self.mode = SamplingMode.DIGITAL
        self.triggerMode = 0
        self.channels = 8
        self.triggerChannel = 1
        self.frequency = 16
        self.depth = 192
        self.timeout = 0.1
        self.compareVoltage = 1.65
        self.samplingTime = self.getSamplingTime()

    def getSamplingTime(self):
        return (8*1024*self.depth)/(self.channels * self.samplingFrequenciesLUT[self.frequency])
    
    def parseSamplingStringFromConfig(self):
        commandString = "#"
        
        if self.mode == SamplingMode.DIGITAL:
            commandString += "D"
        else:
            commandString += "A"
        commandString += str(self.triggerMode) + str(self.triggerChannel) + str(self.channels)
        

        if self.frequency < 10:
            temp = "0" + str(self.frequency)
        else:
            temp = str(self.frequency)
        
        commandString += temp

        if self.depth < 100:
            if self.depth < 10:
                temp = "00" + str(self.depth)
            else:
                temp = "0" + str(self.depth)
        else:
            temp = str(self.depth)
        return commandString + temp + ";"
    
    def parseVoltageStringFromConfig(self):
        return ("#CV" + f'{self.compareVoltage:2.2f}'.replace(".", "")) + ";"
    
    def parseTimeoutStringFromConfig(self):
        if self.timeout < 10:
            temp = "0" + f'{self.timeout:2.2f}'
        else:
            temp = f'{self.timeout:2.2f}'
        return ("#CT" + temp.replace(".", ""))+ ";"
