from PySide6.QtWidgets import QGraphicsScene
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backend_tools import Cursors
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import matplotlib
import matplotlib.style as mplstyle

class Plotter():
    plotColors = ['#ff0000', '#ff8000', '#e6e600', '#33cc33', '#0033cc', '#660066', '#669999', '#e6e6e6', '']
    dataBuffer = []
    channelLengthInSamples = 0
    channelLengthInUnit = 0
    channelLengthInSeconds = 0
    timeUnitMultiplier = 1
    timeUnitString = "s"
    
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
        self.axisPlot.cursorLine = self.axisPlot.axes.axvline(color='#ffffff', lw=1, ls='--')
        self.axisPlot.cursorLine.set_visible(False)
        self.axisPlot.axes.set_visible(True)
        self.axisPlot.axes.set_axis_on()
        self.axisPlot.axes.set_xlim(0,self.channelLengthInUnit/10)
        self.axisPlot.plottedLine = self.axisPlot.axes.plot([], [])
        self.axisPlot.axes.get_yaxis().set_visible(False)                                                   
        self.axisPlot.axes.tick_params(axis='x', which='both', bottom=False, top=True, labelbottom=False, labeltop=True)
        self.axisPlot.axes.spines['top'].set_visible(True)
        self.axisPlot.axes.spines['right'].set_visible(False)
        self.axisPlot.axes.spines['bottom'].set_visible(False)
        self.axisPlot.axes.spines['left'].set_visible(False)
        self.axisPlot.canvas.draw()
        #self.axis.xaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    
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
            self.channelPlots[index].plottedLine = self.channelPlots[index].axes.step(self.xAxisData, channelData, color=self.plotColors[index], linewidth=5)
            self.channelPlots[index].axes.set_xlim(0,self.channelLengthInUnit/10)
            self.channelPlots[index].axes.set_ylim(0,1)
            self.channelPlots[index].axes.set_axis_off()
            self.channelPlots[index].cursorLine = self.channelPlots[index].axes.axvline(color='#ffffff', lw=1, ls='--')
            self.channelPlots[index].cursorLine.set_visible(False)
            self.channelPlots[index].canvas.draw()
        
    
    ''' 
    This method should get the raw data as a bytearray and the number of channels sampled
    It will return the data as a list (2D Array) of height channelNumber
    '''   
    def processRawData(self, rawData:bytearray, channelNumber:int) -> list:
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
        self.dataBuffer = tempBuffer

# moved channel length, figures, axes, canvas, cursorLines from plotter to channel
# renamed axisMultiplier to timeUnitMultiplier
# renamed channelLength to channelLengthInSamples
# renamed plotter method from setAxisMultiplier to calculateTimeMultiplier
# moved QGraphicsScene from GUI to Plot
# Created Flag for channel activeness
# created Plotter variables dataLengthInUnit, dataLengthInSeconds
# renamed treatData to processRawData


class Plot():
    def __init__(self) -> None:
        self.figure, self.axes = plt.subplots(layout='constrained')
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.set_cursor(Cursors.SELECT_REGION)
        self.axes.set_axis_off()
        self.cursorLine = self.axes.axvline(color='#ffffff', lw=1, ls='--')
        self.cursorLine.set_visible(False)
        self.isVisible = True
        self.plottedLine = Line2D([], [])
        
        
