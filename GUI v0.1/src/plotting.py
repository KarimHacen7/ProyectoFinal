from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy

class Plotter():
    # This method should get:
    #   the raw data for the channel to draw as a list
    #   the desired size of the canvas as a tuple (sizeX, sizeY) 
    #   the color in hex format as a string
    # And will return the canvas to be added as a widget in the GUI, through a QGraphicsScene 
    def plotChannel(self, data:list, size:tuple, color:str) -> FigureCanvas:
        self.canvas = FigureCanvas(Figure(figsize=size, layout='constrained'))
        self.axis = self.canvas.figure.subplots()
        self.axis.set_xlim(0,len(data))
        self.axis.set_ylim(0,1)
        self.axis.plot(numpy.linspace(start=0, stop=len(data), num=len(data)), data, color=color, drawstyle='steps')
        self.axis.set_axis_off()
        return self.canvas
    
    # This method should get:
    #   the raw data as a bytearray and the number of channels sampled
    # And will return the data as a 2D array (using lists) of height channelNumber     
    def treatData(self, rawData:bytearray, channelNumber:int) -> list:
        tempBuffer = []
        for _ in range(channelNumber):
            tempBuffer.append([])
        for byte in rawData:
            bits = format(byte, '08b')
            if channelNumber == 8: 
                for i in range(channelNumber):
                    tempBuffer[i].append(int(bits[7-i]))
            if channelNumber == 4:
                for i in range(4):
                    tempBuffer[i].append(int(bits[7-i]))
                    tempBuffer[i].append(int(bits[3-i]))
            if channelNumber == 2:
                for i in range(2):
                    tempBuffer[i].append(int(bits[7-i]))
                    tempBuffer[i].append(int(bits[5-i]))
                    tempBuffer[i].append(int(bits[3-i]))
                    tempBuffer[i].append(int(bits[1-i]))
            if channelNumber == 1:
                for bit in bits:
                    tempBuffer[0].append(bit)
        return tempBuffer
    