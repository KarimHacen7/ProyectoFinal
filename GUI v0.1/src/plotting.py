from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backend_tools import Cursors
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.style as mplstyle

class Plotter():
    plotColors = ['#ff0000', '#ff8000', '#e6e600', '#33cc33', '#0033cc', '#660066', '#669999', '#e6e6e6', '']
    visibleChannels = [1,2,3,4,5,6,7,8]
    channelLength = 1
    figures = []
    axs = []
    canvases = []
    cursorLines = []
    dataBuffer = []
    xAxisData = []
    for i in range(8):
        figures.append(0)
        axs.append(0)
        canvases.append(0)
        cursorLines.append(0)
    axisMultiplier = 1
    axisUnitString = str()

    def __init__(self) -> None:
        mplstyle.use(['dark_background','fast'])
        matplotlib.rcParams['path.simplify'] = True
        matplotlib.rcParams['path.simplify_threshold'] = 1
        matplotlib.rcParams['agg.path.chunksize'] = 1000
        for i in range(8):
            self.figures[i], self.axs[i] = plt.subplots(layout='constrained')
            self.canvases[i] = FigureCanvasQTAgg(self.figures[i])
            self.canvases[i].set_cursor(Cursors.SELECT_REGION)
            self.axs[i].set_axis_off()
            

        self.axisFigure, self.axisAxs = plt.subplots(layout='constrained')
        self.axisCanvas = FigureCanvasQTAgg(self.axisFigure)
        self.axisCanvas.set_cursor(Cursors.SELECT_REGION)
        self.axisAxs.set_axis_off()

    # This method should get the sampling time as a float
    # It will return the string to be put in the time label 
    def setAxisMultiplier(self, samplingTime) -> str:
        if samplingTime < 1e-6:
            self.axisMultiplier = 1e9
            self.axisUnitString = "ns"
        elif samplingTime < 1e-3:
            self.axisMultiplier = 1e6
            self.axisUnitString = "μs" 
        elif samplingTime < 1:
            self.axisMultiplier = 1e3
            self.axisUnitString = "ms" 
        else:
            self.axisMultiplier = 1
            self.axisUnitString = "s" 
        return "Tiempo[%s]" %self.axisUnitString
        
    def plotDigitalAxis(self, freq:int):
        self.axisAxs.clear()
        self.axisCursorLines= self.axisAxs.axvline(color='#ffffff', lw=1, ls='--')
        self.axisCursorLines.set_visible(False)
        self.axisAxs.set_axis_on()
        self.axisAxs.set_xlim(0,len(self.dataBuffer[0])*self.axisMultiplier/(10*freq))
        self.axisAxs.plot([], [])
        self.axisAxs.get_yaxis().set_visible(False)                                                   
        self.axisAxs.tick_params(axis='x', which='both', bottom=False, top=True, labelbottom=False, labeltop=True)
        self.axisAxs.spines['top'].set_visible(True)
        self.axisAxs.spines['right'].set_visible(False)
        self.axisAxs.spines['bottom'].set_visible(False)
        self.axisAxs.spines['left'].set_visible(False)
        #self.axis.xaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
        self.axisCanvas.draw()
    
    # This method should get the raw data for the channel to draw as a list (2D Array)
    # It will update the canvas automatically
    def plotDigitalChannels(self, freq:int) -> None:
        self.channelLength = len(self.dataBuffer[0])

        for ax in self.axs:
            ax.clear()
        self.cursorLines = []
        for _ in self.dataBuffer:
            self.cursorLines.append(0) 
        
        self.xAxisData = np.linspace(start=0, stop=self.channelLength*self.axisMultiplier/freq, num=self.channelLength)
        
        for index, channel in enumerate(self.dataBuffer):
            self.axs[index].step(self.xAxisData, channel, color=self.plotColors[index], linewidth=5)
            self.axs[index].set_xlim(0,len(channel)*self.axisMultiplier/(10*freq))
            self.axs[index].set_ylim(0,1)
            self.axs[index].set_axis_off()
            self.cursorLines[index] = self.axs[index].axvline(color='#ffffff', lw=1, ls='--')
            self.cursorLines[index].set_visible(False)
            self.canvases[index].draw()
        
    
    # This method should get the raw data as a bytearray and the number of channels sampled
    # It will return the data as a list (2D Array) of height channelNumber     
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
        self.dataBuffer = tempBuffer

    