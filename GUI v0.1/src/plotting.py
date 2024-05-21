from PySide6.QtWidgets import QGraphicsScene
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backend_tools import Cursors
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import matplotlib
import matplotlib.style as mplstyle

class Plotter():
    plotColors = ['#ff0000', '#ff8000', '#e6e600', '#33cc33', '#0033cc', '#c339fa', '#669999', '#e6e6e6', '']
    axisIncrements = [2e-4,5e-4,10e-4, 2e-3,5e-3,10e-3 ,2e-2,5e-2,10e-2, 2e-1,5e-1,10e-1,2,5,10,20,25,30,50,60,70,100]
    dataBuffer = []
    edgesBuffer = []
    channelLengthInSamples = 0
    channelLengthInUnit = 0
    channelLengthInSeconds = 0
    timeUnitMultiplier = 1
    timeUnitString = "s"
    plottingInProcess = False
    xAxisData = []

    def __init__(self) -> None:
        mplstyle.use(['dark_background','fast'])
        matplotlib.rcParams['path.simplify'] = True
        matplotlib.rcParams['path.simplify_threshold'] = 1
        matplotlib.rcParams['agg.path.chunksize'] = 1000
        
        self.channelPlots = []
        for _ in range(8):
            self.channelPlots.append(Plot())
        self.axisPlot = Plot()

    '''
    Convinience method for ensuring data is processed in the right order
    '''
    def processAndPlot(self, rawdata:bytearray, samplingFrequency:int, channelNumber:int) -> None:
        self.processRawData(rawData=rawdata, channelNumber=channelNumber)
        self.plotDigitalChannels(samplingFrequency=samplingFrequency)
        self.plotDigitalAxis()
    
    '''
    This method should get the sampling time as a float
    It will return the string to be put in the time label as a label
    ''' 
    def calculateTimeUnitMultiplier(self) -> None:
        if self.channelLengthInSeconds < 1e-6:
            self.timeUnitMultiplier = 1e9
            self.timeUnitString = "ns"
        elif self.channelLengthInSeconds < 1e-3:
            self.timeUnitMultiplier = 1e6
            self.timeUnitString = "μs" 
        elif self.channelLengthInSeconds < 1:
            self.timeUnitMultiplier = 1e3
            self.timeUnitString = "ms" 
        else:
            self.timeUnitMultiplier = 1
            self.timeUnitString = "s" 

    '''
    Needs documentation
    '''
    def plotDigitalAxis(self) -> None:
        self.axisPlot.axes.clear()
        self.axisPlot.cursorLine = self.axisPlot.axes.axvline(color='#ffffff', lw=1, ls='--' , animated=True)
        self.axisPlot.cursorLine.set_visible(False)
        self.axisPlot.axes.set_visible(True)
        self.axisPlot.axes.set_axis_on()
        self.axisPlot.axes.set_xlim(0,self.channelLengthInUnit/10)
        self.axisPlot.plottedLine = self.axisPlot.axes.plot([], [])
        self.axisPlot.axes.get_yaxis().set_visible(False)                                                   
        self.axisPlot.axes.tick_params(axis='x', which='both', bottom=False, top=True, labelbottom=False, labeltop=True, length=4)
        self.axisPlot.axes.spines['top'].set_visible(True)
        self.axisPlot.axes.spines['right'].set_visible(False)
        self.axisPlot.axes.spines['bottom'].set_visible(False)
        self.axisPlot.axes.spines['left'].set_visible(False)
        
    '''
    Needs documentation
    '''
    def plotDigitalChannels(self, samplingFrequency:int) -> None:
        self.channelLengthInSamples = len(self.dataBuffer[0])
        self.channelLengthInSeconds = self.channelLengthInSamples*(1/samplingFrequency)
        self.calculateTimeUnitMultiplier()
        self.channelLengthInUnit = self.channelLengthInSeconds*self.timeUnitMultiplier

        for channel in self.channelPlots:
            channel.axes.clear()

        self.xAxisData = np.linspace(start=0, stop=self.channelLengthInUnit, num=self.channelLengthInSamples)
        
        for index, channelData in enumerate(self.dataBuffer):
            self.channelPlots[index].plottedLine = self.channelPlots[index].axes.step(self.xAxisData, channelData, color=self.plotColors[index], linewidth=3, where='mid')
            self.channelPlots[index].axes.set_xlim(0,self.channelLengthInUnit/10)
            self.channelPlots[index].axes.set_ylim(0,1)
            self.channelPlots[index].axes.set_axis_off()
            self.channelPlots[index].cursorLine = self.channelPlots[index].axes.axvline(color='#ffffff', lw=1, ls='--', animated=True)
            self.channelPlots[index].cursorLine.set_visible(False)
            
    
    ''' 
    This method should get the raw data as a bytearray and the number of channels sampled
    It will return the data as a list (2D Array) of height channelNumber
    '''   
    def processRawData(self, rawData:bytearray, channelNumber:int) -> list:
        tempBuffer = []
        self.edgesBuffer = []
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
        self.dataBuffer = tempBuffer
        for _ in range(channelNumber):
            self.edgesBuffer.append([])
        for i, channel in enumerate(self.dataBuffer):
            for j, sample in enumerate(channel):
                if j == len(channel)-1:
                    break
                if channel[j+1] < channel[j]:
                    tempDict = {"1": j, "2":(j+1), "type":"F"}
                    self.edgesBuffer[i].append(tempDict)
                elif channel[j+1] > channel[j]:
                    tempDict = {"1": j, "2":(j+1), "type":"R"}
                    self.edgesBuffer[i].append(tempDict)
                else:
                    continue
        print(self.edgesBuffer)



class Plot():
    def __init__(self) -> None:
        self.figure, self.axes = plt.subplots(layout='constrained')
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.set_cursor(Cursors.SELECT_REGION)
        self.axes.set_axis_off()
        self.cursorLine = self.axes.axvline(color='#ffffff', lw=1, ls='--', animated=True)
        self.cursorLine.set_visible(False)
        self.isVisible = True
        self.plottedLine = Line2D([], [])
        self.background = None
        
        
