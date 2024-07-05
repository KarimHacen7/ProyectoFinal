from settings import *
from PySide6.QtWidgets import QGraphicsScene
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backend_tools import Cursors
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
import matplotlib
import matplotlib.style as mplstyle

class Plotter():
    plotColors = ['#ff0000', '#ff8000', '#e6e600', '#33cc33', '#0033cc', '#c339fa', '#669999', '#e6e6e6', '']
    axisIncrements = [2e-4,5e-4,10e-4,2e-3,5e-3,10e-3 ,2e-2,5e-2,10e-2, 2e-1,5e-1,1,2,5,10,20,25,30,50,60,70,100]
    dataBuffer = []
    edgesBuffer = []
    channelLengthInSamples = 0
    channelLengthInUnit = 0
    channelLengthInSeconds = 0
    timeUnitMultiplier = 1
    timeUnitString = "s"
    plottingInProcess = False
    isGridOn = False
    xAxisData = []
    cursor1PositionSample = None
    cursor2PositionSample = None
    protocolSigns = []
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
    def processAndPlot(self, rawdata:bytearray, samplingSettings:SamplingSettings) -> None:
        # DO NOT CHANGE ORDER OF EXECUTION
        if samplingSettings.mode == SamplingMode.DIGITAL:
            self.processRawDigitalData(rawData=rawdata, channelNumber=samplingSettings.channels)
            self.plotDigitalChannels(samplingFrequency=samplingSettings.samplingFrequenciesLUT[samplingSettings.frequency])
            self.plotDigitalAxis()
        else:
            self.processRawAnalogData(rawData=rawdata, samplingFrequency=samplingSettings.samplingFrequenciesLUT[samplingSettings.frequency])
            self.plotAnalogChannel(samplingFrequency=samplingSettings.samplingFrequenciesLUT[samplingSettings.frequency])

    
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
        self.axisPlot.fixedCursor1 = self.axisPlot.axes.axvline(color='#3affff', lw=1.5, ls='--')
        self.axisPlot.fixedCursor1.set_visible(False)
        self.axisPlot.fixedCursor2 = self.axisPlot.axes.axvline(color='#ff88ff', lw=1.5, ls='--')
        self.axisPlot.fixedCursor2.set_visible(False)
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
        self.axisPlot.axes.xaxis.set_major_formatter('{x} %s' %self.timeUnitString)
        
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
            self.channelPlots[index].axes.set_ylim(-0.1,1.65)
            self.channelPlots[index].axes.set_axis_off()
            self.channelPlots[index].cursorLine = self.channelPlots[index].axes.axvline(color='#ffffff', lw=1, ls='--', animated=True)
            self.channelPlots[index].cursorLine.set_visible(False)
            self.channelPlots[index].fixedCursor1 = self.channelPlots[index].axes.axvline(color='#3affff', lw=1.5, ls='--')
            self.channelPlots[index].fixedCursor1.set_visible(False)
            self.channelPlots[index].fixedCursor2 = self.channelPlots[index].axes.axvline(color='#ff88ff', lw=1.5, ls='--')
            self.channelPlots[index].fixedCursor2.set_visible(False)
        


    def plotAnalogChannel(self, samplingFrequency:int) -> None:
        self.channelLengthInSamples = len(self.dataBuffer[0])
        self.channelLengthInSeconds = self.channelLengthInSamples*(1/samplingFrequency)
        self.calculateTimeUnitMultiplier()
        self.channelLengthInUnit = self.channelLengthInSeconds*self.timeUnitMultiplier

        for channel in self.channelPlots:
            channel.axes.clear()

        self.xAxisData = np.linspace(start=0, stop=self.channelLengthInUnit, num=self.channelLengthInSamples)
        
        self.channelPlots[0].plottedLine = self.channelPlots[0].axes.plot(self.xAxisData, self.dataBuffer[0], color=self.plotColors[0], linewidth=3)
        self.channelPlots[0].cursorLine = self.channelPlots[0].axes.axvline(color='#ffffff', lw=1, ls='--', animated=True)
        self.channelPlots[0].cursorLine.set_visible(False)
        
        self.channelPlots[0].fixedCursor1 = self.channelPlots[0].axes.axvline(color='#3affff', lw=1.5, ls='--')
        self.channelPlots[0].fixedCursor1.set_visible(False)
        self.channelPlots[0].fixedCursor2 = self.channelPlots[0].axes.axvline(color='#ff88ff', lw=1.5, ls='--')
        self.channelPlots[0].fixedCursor2.set_visible(False)
        
        self.channelPlots[0].axes.set_xlim(0,self.channelLengthInUnit/10)
        self.channelPlots[0].axes.set_ylim(0,5)
        
        
        

    ''' 
    This method should get the raw data as a bytearray and the number of channels sampled
    It will return the data as a list (2D Array) of height channelNumber
    '''   
    def processRawDigitalData(self, rawData:bytearray, channelNumber:int) -> None:
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
                    tempBuffer[0].append(int(bit))
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

    def processRawAnalogData(self, rawData:bytearray, samplingFrequency: int) -> None:
        tempBuffer = []
        tempBuffer.append([])
        if samplingFrequency <= 500e3:
            for byte in rawData:
                tempBuffer[0].append(np.round(a=(byte/255)*3.3*2, decimals=3))
        else:
            for byte in rawData:
                tempBuffer[0].append(np.round(a=(byte/255)*2.5*2, decimals=3))
        self.dataBuffer = tempBuffer

    


class Plot():
    def __init__(self) -> None:
        self.figure, self.axes = plt.subplots(layout='constrained')
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.set_cursor(Cursors.SELECT_REGION)
        self.axes.set_axis_off()
        
        self.cursorLine = self.axes.axvline(color='#ffffff', lw=1, ls='--', animated=True)
        self.cursorLine.set_visible(False)
        self.fixedCursor1 = self.axes.axvline(color='#3affff', lw=1.5, ls='--')
        self.fixedCursor1.set_visible(False)
        self.fixedCursor2 = self.axes.axvline(color='#ff88ff', lw=1.5, ls='--')
        self.fixedCursor2.set_visible(False)
        self.isVisible = True
        self.plottedLine = Line2D([], [])
        self.background = None


class ProtocolFrameSign():
    def __init__(self, patch, text) -> None:
        self.patch = patch
        self.text = text
        self.inscription = self.text.get_text()

    def defineRender(self, leftLim, rightLim):
        minimumWidthRatio = 1.1
        self.text.set(visible=True)
        textBbox = self.text.get_window_extent()
        textBbox_data_coords = self.text.axes.transData.inverted().transform(textBbox)
        textBboxX0, textBboxY0 = textBbox_data_coords[0]
        textBboxX1, textBboxY1 = textBbox_data_coords[1]
        textWidth = textBboxX1-textBboxX0

        patchX0 = self.patch.get_x()
        patchX1 = patchX0 + self.patch.get_width()
        if leftLim > patchX0 and leftLim < patchX1 and rightLim > patchX1:
            # se ve un pedazo por izquierda
            patchWidth = patchX1 - leftLim
            if patchWidth > minimumWidthRatio*textWidth:
                self.text.set(visible=True)
            else:
                self.text.set(visible=False)
        elif leftLim <= patchX0 and rightLim >= patchX1:
            # se ve entero
            patchWidth = patchX1 - patchX0
            if patchWidth > minimumWidthRatio*textWidth:
                self.text.set(visible=True)
            else:
                self.text.set(visible=False)
        elif leftLim < patchX0 and rightLim > patchX0 and rightLim < patchX1:
            # se ve un pedazo por derecha
            patchWidth = rightLim-patchX0
            if patchWidth > minimumWidthRatio*textWidth:
                self.text.set(visible=True)
            else:
                self.text.set(visible=False)
        elif (leftLim >= patchX0 and rightLim < patchX1) or (leftLim > patchX0 and rightLim <= patchX1):
            patchWidth = rightLim-leftLim
            if patchWidth > minimumWidthRatio*textWidth:
                self.text.set(visible=True)
            else:
                self.text.set(visible=False)
        else:
            self.text.set(visible=False)
            return
        self.text.draw(self.text.axes.figure.canvas.get_renderer())

