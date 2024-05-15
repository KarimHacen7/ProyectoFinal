from settings import SamplingSettings, SamplingMode
from communication import CommunicationModule, SamplingWorker
from plotting import Plotter
from PySide6.QtWidgets import  QMainWindow, QMessageBox, QGraphicsScene, QGraphicsView,  QCheckBox
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer, QThread, Signal
from ui_mainwindow import Ui_MainWindow
import numpy as np
import time

class MainWindow(QMainWindow):
    statusLabelTimer = QTimer()
    communicationModule = CommunicationModule()
    samplingSettings = SamplingSettings()
    plotter = Plotter()
    initialBuffer = bytearray()
    QGVChannelsList = [] # QGraphicsView Reference List
    QCBChannelsList = [] # QCheckBox Reference List
    QFrChannelsList = [] # QFrame Reference List
    cursorCallbackIDs = []
    resizeSignal = Signal()
    firstResizeDone = False
    cursorIsActive = False
    lastCursorIndex = 0
    channelScenes = []
    axisScene = QGraphicsScene()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Get a list of QGraphicsView for the channels
        for item in dir(self.ui):
            ref = getattr(self.ui, item)
            if isinstance(ref, QGraphicsView) and (item.find("channel") != -1):
                self.QGVChannelsList.append(ref)
        # Get a list of QCheckBox for the channel selector
        for item in dir(self.ui):
            ref = getattr(self.ui, item)
            if isinstance(ref, QCheckBox) and (item.find("channel") != -1):
                self.QCBChannelsList.append(ref)
        # Define a list of the main frames for each channel
        self.QFrChannelsList = [self.ui.channel1Frame,self.ui.channel2Frame,self.ui.channel3Frame,self.ui.channel4Frame,self.ui.channel5Frame,self.ui.channel6Frame,self.ui.channel7Frame,self.ui.channel8Frame] 
        
        # Proxies for interfacing PySide with Matplotlib
        for _ in range(8):
            self.channelScenes.append(QGraphicsScene())
        for index, item in enumerate(self.QGVChannelsList):
            item.setScene(self.channelScenes[index])
            self.channelScenes[index].addWidget(self.plotter.canvases[index])
        self.ui.axisGraphicsView.setScene(self.axisScene)
        self.axisScene.addWidget(self.plotter.axisCanvas)
        # Zoom in and out signals
        for fig in self.plotter.figures:
            fig.canvas.mpl_connect('scroll_event', self.digitalZoomInOut)
        
        # Slide Animation, with signals for responsiveness
        self.configSlideAnimation = QPropertyAnimation(self.ui.slideFrameContainer, b"maximumWidth")#Animate minimumWidht
        self.configSlideAnimation.finished.connect(self.resizeHandler)
        self.resizeSignal.connect(self.resizeHandler)
        self.ui.configSliderPushButton.clicked.connect(self.sidePanelSlideAnimation)
        # Cursor selector
        self.ui.cursorPushButton.clicked.connect(self.startStopCursor)
        # Housekeeping signals
        self.ui.samplingDepthHorizontalSlider.valueChanged.connect(self.updateSamplingDepthLabel)
        self.ui.digitalModePushButton.clicked.connect(self.restrictSettingsDigitalMode)
        self.ui.analogModePushButton.clicked.connect(self.restrictSettingsAnalogMode)
        self.ui.samplingDepthHorizontalSlider.valueChanged.connect(self.calculateSamplingTime)
        self.ui.samplingFrequencyComboBox.currentIndexChanged.connect(self.calculateSamplingTime)
        self.ui.samplingChannelsComboBox.currentIndexChanged.connect(self.calculateSamplingTime)
        self.ui.samplingChannelsComboBox.currentIndexChanged.connect(self.restrictTriggerChannels)
        # Sampling order
        self.ui.startSamplingPushButton.clicked.connect(self.sample)
        # Channel selectors
        self.ui.channel1CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel2CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel3CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel4CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel5CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel6CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel7CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel8CheckBox.stateChanged.connect(self.hideAndShowChannels)
        # Scroll Bar navigation
        self.ui.channelHorizontalScrollBar.sliderMoved.connect(self.horizontalSliderChanged)
        # Digital mode, by default
        self.ui.digitalModePushButton.animateClick()
        self.calculateSamplingTime()
        # Status informing label
        self.statusLabelTimer.timeout.connect(self.checkConnectedStatusAndShowInLabel)
        self.statusLabelTimer.start(500)
        self.ui.cursorInfoLabel.setVisible(False)

    # ---------- THREADING -- START SAMPLING ----------
    def startSamplingThread(self):
        self.samplingThread = QThread() 
        self.samplingWorker = SamplingWorker()
        self.samplingWorker.moveToThread(self.samplingThread)
        
        self.getConfigurationFromGUI()
        self.samplingWorker.samplingQueue.put(self.samplingSettings.parseSamplingStringFromConfig(), block=True, timeout=None)
        self.samplingWorker.timeoutQueue.put(self.samplingSettings.parseTimeoutStringFromConfig(), block=True, timeout=None)
        self.samplingWorker.voltageQueue.put(self.samplingSettings.parseVoltageStringFromConfig(), block=True, timeout=None)

        self.samplingThread.started.connect(self.samplingWorker.sample)         # When thread is created, start sampling
        self.samplingWorker.finished.connect(self.samplingThread.quit)          # When the job is finished, stop the thread
        self.samplingWorker.finished.connect(self.samplingWorker.deleteLater)   # Then, delete the object
        self.samplingThread.finished.connect(self.samplingThread.deleteLater)   # And the thread
        self.samplingWorker.samplingFinished.connect(self.samplingIsFinished)   # When samples are ready, go to callback
        self.samplingWorker.commandAcknowledged.connect(self.commandIsAcknowledged)
        self.samplingWorker.dataIncoming.connect(self.dataIsIncoming)
        self.samplingWorker.timeoutFinished.connect(self.timeoutIsFinished)
        self.samplingWorker.voltageFinished.connect(self.voltageIsFinished)
        
        self.samplingWorker.finished.connect(self.threadFinished)
        self.samplingThread.start()                                             # Get to work, when done, it should stop automatically

    # ---------- THREADING -- CALLBACKS ----------
    def voltageIsFinished(self, code):
        if code == 1:
            self.ui.connectionStatusLabel.setText("Estado: Configurando...")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #f6f7da; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
            self.ui.samplingProgressBar.setValue(5)
        else:
            QMessageBox.critical(self, "Error", "Hubo un error al comunicarse con el periférico", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)

    def timeoutIsFinished(self, code):
        if code == 1:
            self.ui.connectionStatusLabel.setText("Estado: Configurado!")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #f2f5bc; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
            self.ui.samplingProgressBar.setValue(15)
        else:
            QMessageBox.critical(self, "Error", "Hubo un error al comunicarse con el periférico", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)

    def commandIsAcknowledged(self):
        self.ui.connectionStatusLabel.setText("Estado: Muestreando...")
        self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #f1f5a2; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
        self.ui.samplingProgressBar.setValue(25)

    def dataIsIncoming(self, length:int):
        self.ui.connectionStatusLabel.setText("Estado: Recibiendo Datos")
        self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #f1f5a2; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
        progress = 25 + int(0.75*length/(1024*self.samplingSettings.depth))
        self.ui.samplingProgressBar.setValue(progress)

    def samplingIsFinished(self, code, data):
        if code == -1 or code == -2:
            self.ui.connectionStatusLabel.setText("Estado: Desconectado")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #ff4a4a; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
            QMessageBox.warning(self, "Desconexión", "Se ha reiniciado o desconectado el periférico", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
        elif code == -3:
            QMessageBox.information(self, "Timeout", "Se ha excedido el tiempo de espera indicado", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
        else:
            self.ui.connectionStatusLabel.setText("Estado: Conectado")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #4af792; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
            self.graphChannels(data)

    def threadFinished(self):
        self.statusLabelTimer.start()
        self.ui.samplingProgressBar.setValue(0)
    
    # ---------- GUI HOUSEKEEPING ----------
    def checkConnectedStatusAndShowInLabel(self):
        isConnected = self.communicationModule.checkConnected("VID_2E8A&PID_000A")
        if isConnected:
            self.ui.connectionStatusLabel.setText("Estado: Conectado")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #4af792; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
        else:
            self.ui.connectionStatusLabel.setText("Estado: Desconectado")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #ff4a4a; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
    
    def updateSamplingDepthLabel(self):
        value = self.ui.samplingDepthHorizontalSlider.value()
        self.ui.samplingDepthValueLabel.setText(str(value)+" [KiB]")
        return

    def restrictSettingsAnalogMode(self):
        self.samplingSettings.mode = SamplingMode.ANALOG
        self.ui.digitalModePushButton.setStyleSheet("QPushButton { background-color: #b3b3b3; color: #525151;}")
        self.ui.analogModePushButton.setStyleSheet("QPushButton { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #50b0fa); }")
        if self.ui.samplingFrequencyComboBox.count() == 17:
            for i in [16,15,14]:
                self.ui.samplingFrequencyComboBox.removeItem(i)
        
        if self.ui.samplingChannelsComboBox.count() == 4:
            for i in [3,2,1]:
                self.ui.samplingChannelsComboBox.removeItem(i)
        
        if self.ui.triggerChannelComboBox.count() == 8:
            for i in range(8, 0, -1):
                self.ui.triggerChannelComboBox.removeItem(i)
            self.ui.triggerChannelComboBox.setItemText(0, "8")

    def restrictSettingsDigitalMode(self):
        self.samplingSettings.mode = SamplingMode.DIGITAL
        self.ui.digitalModePushButton.setStyleSheet("QPushButton {  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #50b0fa);}")
        self.ui.analogModePushButton.setStyleSheet("QPushButton { background-color: #b3b3b3; color: #525151; }")
        if self.ui.samplingFrequencyComboBox.count() == 14:
            for i in [50,100,125]:
                self.ui.samplingFrequencyComboBox.addItem(str(i)+" [MHz]")
        
        if self.ui.samplingChannelsComboBox.count() == 1:
            for i in [2,4,8]:
                self.ui.samplingChannelsComboBox.addItem("1-"+str(i))
        
        if self.ui.triggerChannelComboBox.count() == 1:
            self.ui.triggerChannelComboBox.setItemText(0, "1")
            for i in range(2, 9):
                self.ui.triggerChannelComboBox.addItem(str(i))

    def restrictTriggerChannels(self):
        self.ui.triggerChannelComboBox.setMaxCount(0) 
        self.ui.triggerChannelComboBox.setMaxCount(8)
        if self.samplingSettings.mode == SamplingMode.DIGITAL:
            for i in range(pow(2, self.ui.samplingChannelsComboBox.currentIndex())):
                self.ui.triggerChannelComboBox.addItem(str(i+1))
        if self.samplingSettings.mode == SamplingMode.ANALOG:
            self.ui.triggerChannelComboBox.addItem("8")
    
    def calculateSamplingTime(self):
        # (8[bit/B] * 1024[B/KiB]  * depth [KiB])[bit] /(frecuencia [muestra/seg] * canales [bits/muestra]) [bit/seg]  
        bits = 8*1024*self.ui.samplingDepthHorizontalSlider.value()
        bitrate = pow(2, self.ui.samplingChannelsComboBox.currentIndex()) * self.samplingSettings.samplingFrequenciesLUT[self.ui.samplingFrequencyComboBox.currentIndex()]
        samplingTime = bits/bitrate
        infoString = ""
        if samplingTime < 1e-9:
            infoString = "menor a 1 [ns]"
        elif samplingTime < 1e-6:
            infoString =  str(round(samplingTime*1e9, 2)) +" [ns]" 
        elif samplingTime < 1e-3:
            infoString =  str(round(samplingTime*1e6, 2)) +" [us]"
        elif samplingTime < 1:
            infoString =  str(round(samplingTime*1e3, 2)) +" [ms]"
        else:
            infoString =  str(round(samplingTime, 2)) +" [s]"
        
        self.ui.estimatedSamplingTimeValueLabel.setText(infoString)

    def getConfigurationFromGUI(self):
        # sampling mode is acquired at button signal callback
        self.samplingSettings.frequency = self.ui.samplingFrequencyComboBox.currentIndex()
        self.samplingSettings.depth = self.ui.samplingDepthHorizontalSlider.value()
        self.samplingSettings.channels = pow(2, self.ui.samplingChannelsComboBox.currentIndex())
        self.samplingSettings.triggerMode = self.ui.triggerModeComboBox.currentIndex()
        self.samplingSettings.timeout = round(self.ui.triggerTimeoutDoubleSpinBox.value(), 2)
        self.samplingSettings.compareVoltage = round(self.ui.voltageThresholdDoubleSpinBox.value(), 2)
        if self.samplingSettings.mode == SamplingMode.ANALOG:
            self.samplingSettings.triggerChannel = 8
        else:
            self.samplingSettings.triggerChannel = self.ui.triggerChannelComboBox.currentIndex() + 1
    
    # ---------- USER INPUT ----------
    def sample(self):
        self.statusLabelTimer.stop()
        self.ui.samplingProgressBar.setValue(0)
        self.startSamplingThread()
        return

    def sidePanelSlideAnimation(self):
        width = self.ui.slideFrameContainer.width()
        if width == 0:
            newWidth = 200
        else:
            newWidth = 0
        self.configSlideAnimation.setDuration(250)
        self.configSlideAnimation.setStartValue(width)
        self.configSlideAnimation.setEndValue(newWidth)
        self.configSlideAnimation.setEasingCurve(QEasingCurve.InOutQuart)
        self.configSlideAnimation.start()

    def hideAndShowChannels(self):
        for index, channelCheckBox in enumerate(self.QCBChannelsList):
            if channelCheckBox.isChecked():
                self.QFrChannelsList[index].setVisible(True)
                self.plotter.canvases[index].setGeometry(0, 0, self.QGVChannelsList[index].width(), self.QGVChannelsList[index].height())
                self.plotter.canvases[index].draw()
            else:
                self.QFrChannelsList[index].setVisible(False)

    def startStopCursor(self):
        if not self.cursorIsActive:
            self.cursorIsActive = True
            for fig in self.plotter.figures:
                self.cursorCallbackIDs.append(fig.canvas.mpl_connect('motion_notify_event', self.cursorDrawAndCalculate))
            self.ui.cursorPushButton.setStyleSheet("QPushButton { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #50b0fa); }")
            self.ui.cursorInfoLabel.setVisible(True)
        else:
            self.cursorIsActive = False
            for index, fig in enumerate(self.plotter.figures):
                fig.canvas.mpl_disconnect(self.cursorCallbackIDs[index])
            self.cursorCallbackIDs = []
            for line in self.plotter.cursorLines:
                line.set_xdata([0])
                line.set_visible(False)
            self.plotter.axisCursorLines.set_xdata([0])
            self.plotter.axisCursorLines.set_visible(False)
            for canvas in self.plotter.canvases:
                canvas.draw()
            self.plotter.axisCanvas.draw()
            self.ui.cursorPushButton.setStyleSheet("")
            self.ui.cursorInfoLabel.setVisible(False)
    
    #  ---------- PLOTTING  ----------
    def graphChannels(self, data):
        self.plotter.treatData(rawData=data, channelNumber=self.samplingSettings.channels)
        self.ui.axisLabel.setText(self.plotter.setAxisMultiplier(samplingTime=self.samplingSettings.getSamplingTime()))
        self.plotter.plotDigitalChannels(freq=self.samplingSettings.samplingFrequenciesLUT[self.samplingSettings.frequency])
        self.plotter.plotDigitalAxis(freq=self.samplingSettings.samplingFrequenciesLUT[self.samplingSettings.frequency])
        for channelNumber in range(1, 9):
            ref = getattr(self.ui, "channel" + str(channelNumber) + "CheckBox")
            if channelNumber in range(1, self.samplingSettings.channels+1):
                ref.setChecked(True)
                ref.setEnabled(True)
            else:
                ref.setChecked(False)
                ref.setEnabled(False)
        self.ui.channelHorizontalScrollBar.setMaximum(self.plotter.channelLength)
        self.ui.channelHorizontalScrollBar.setValue(0)

        leftLim, rightLim = self.plotter.axs[0].get_xlim()
        upperBound = self.plotter.channelLength*self.plotter.axisMultiplier/self.samplingSettings.samplingFrequenciesLUT[self.samplingSettings.frequency]
        rangeLimDivs = (abs(leftLim-rightLim)/upperBound)*(len(self.plotter.dataBuffer[0]))
        self.ui.channelHorizontalScrollBar.setSingleStep(np.ceil(rangeLimDivs/10) if np.ceil(rangeLimDivs/10) > 2 else 2)
        self.ui.channelHorizontalScrollBar.setPageStep(np.ceil(rangeLimDivs) if np.ceil(rangeLimDivs) > 10 else 10)

    def resizeEvent(self, event):
        self.resizeSignal.emit()
    
    
    def resizeHandler(self):
        if self.firstResizeDone:
            for index, QGV in enumerate(self.QGVChannelsList):
                if self.QFrChannelsList[index].maximumHeight() > 0:
                    self.plotter.canvases[index].setGeometry(0, 0, QGV.width(), QGV.height())
                    self.plotter.canvases[index].draw()
            self.plotter.axisCanvas.setGeometry(0, 0, self.ui.axisGraphicsView.width(), self.ui.axisGraphicsView.height())
        else:
            self.firstResizeDone = True

    def digitalZoomInOut(self, event):

        if self.plotter.dataBuffer == []:
            return
        scrolledChannel = 0

        for index, canvas in enumerate(self.plotter.canvases):
            if canvas == event.canvas:
                scrolledChannel = index 
        
        if event.xdata is not None: 
            centerLim = event.xdata
        else:
            return
        
        leftLim, rightLim = self.plotter.axs[scrolledChannel].get_xlim()
        
        upperBound = self.plotter.channelLength*self.plotter.axisMultiplier/self.samplingSettings.samplingFrequenciesLUT[self.samplingSettings.frequency]

        if event.button == "up":
            leftLim = centerLim - ((centerLim-leftLim)*0.5)
            rightLim= centerLim + ((rightLim-centerLim)*0.5)
        elif event.button == "down":
            leftLim = centerLim - ((centerLim-leftLim)*2)
            rightLim= centerLim + ((rightLim-centerLim)*2)
        else:
            return

        if leftLim < 0:
            leftLim = 0 
        
        if rightLim > upperBound:
            rightLim = upperBound

        if abs(leftLim-rightLim) < (10*(self.plotter.axisMultiplier/self.samplingSettings.samplingFrequenciesLUT[self.samplingSettings.frequency])):
            return

        # Tarda 1 ms
        for axes in self.plotter.axs:
            axes.set_xlim(left=leftLim, right=rightLim)
        self.plotter.axisAxs.set_xlim(left=leftLim, right=rightLim)
        # Hasta Aca
        rangeLimDivs = (abs(leftLim-rightLim)/upperBound)*(self.plotter.channelLength)
        self.ui.channelHorizontalScrollBar.setSingleStep(np.ceil(rangeLimDivs/10) if np.ceil(rangeLimDivs/10) > 2 else 2)
        self.ui.channelHorizontalScrollBar.setPageStep(np.ceil(rangeLimDivs) if np.ceil(rangeLimDivs) > 10 else 10)
        
        self.ui.channelHorizontalScrollBar.setValue(np.ceil((centerLim/upperBound)*self.ui.channelHorizontalScrollBar.maximum()))
        
        for canvas in self.plotter.canvases:
            canvas.draw()
        self.plotter.axisCanvas.draw()

    def horizontalSliderChanged(self):
        if self.plotter.dataBuffer == []:
            return
        upperBound = self.plotter.channelLength*self.plotter.axisMultiplier/self.samplingSettings.samplingFrequenciesLUT[self.samplingSettings.frequency]
        leftLim, rightLim = self.plotter.axs[0].get_xlim()
        rangeLim = abs(rightLim-leftLim)
        
        centerValue = (self.ui.channelHorizontalScrollBar.value()/self.ui.channelHorizontalScrollBar.maximum())*upperBound
        
        leftLim=centerValue-(rangeLim/2)
        rightLim=centerValue+(rangeLim/2)
        
        if leftLim < 0:
            leftLim = 0
            rightLim = rangeLim
        elif rightLim > upperBound:
            leftLim = upperBound - rangeLim
            rightLim = upperBound
        
        for axes in self.plotter.axs:
            axes.set_xlim(left=leftLim, right=rightLim)
        self.plotter.axisAxs.set_xlim(left=leftLim, right=rightLim)

        for canvas in self.plotter.canvases:
            canvas.draw()
        self.plotter.axisCanvas.draw()
        
        

    def cursorDrawAndCalculate(self, event):
        if self.plotter.dataBuffer == []:
            return
        scrolledChannel = 0
        for arrayIndex, canvas in enumerate(self.plotter.canvases):
            if canvas == event.canvas:
                scrolledChannel = arrayIndex 
        if event.inaxes:
            
            index = min(np.searchsorted(self.plotter.xAxisData, event.xdata), len(self.plotter.dataBuffer[scrolledChannel]) - 1)
            
            if index != self.lastCursorIndex:
                self.lastCursorIndex = index
                
                for line in self.plotter.cursorLines:
                    line.set_xdata([self.plotter.xAxisData[self.lastCursorIndex]]) 
                    line.set_visible(True)
                self.plotter.axisCursorLines.set_xdata([self.plotter.xAxisData[self.lastCursorIndex]])
                self.plotter.axisCursorLines.set_visible(True)
                for canvas in self.plotter.canvases:
                    canvas.draw()
                self.plotter.axisCanvas.draw()
                
                
                value = self.plotter.dataBuffer[scrolledChannel][index]
                leftEdge = index-1
                rightEdge = index+1
                
                # 5ms o mas este while

                while (self.plotter.dataBuffer[scrolledChannel][leftEdge] == value) and leftEdge >= 0:
                    leftEdge -= 1
                
                
                # set text es barato
                if leftEdge == 0:
                    self.ui.cursorInfoLabel.setText("t: %s[%s], Δt: %s[%s], 1/Δt: %s[%s]" %(str(np.round(self.plotter.xAxisData[self.lastCursorIndex], 3)), self.plotter.axisUnitString, "?", self.plotter.axisUnitString, "?", "Hz"))
                    #return
                    

                #120 ms
                while (self.plotter.dataBuffer[scrolledChannel][rightEdge] == value) and rightEdge < len(self.plotter.dataBuffer[scrolledChannel])-1:
                    rightEdge += 1


                if rightEdge == len(self.plotter.dataBuffer[scrolledChannel])-1:
                    self.ui.cursorInfoLabel.setText("t: %s[%s], Δt: %s[%s], 1/Δt: %s[%s]" %(str(np.round(self.plotter.xAxisData[self.lastCursorIndex], 3)), self.plotter.axisUnitString, "?", self.plotter.axisUnitString, "?", "Hz"))
                    #return
                
                period = (rightEdge - leftEdge)*self.plotter.axisMultiplier/self.samplingSettings.samplingFrequenciesLUT[self.samplingSettings.frequency]
                frequency = (self.samplingSettings.samplingFrequenciesLUT[self.samplingSettings.frequency]/(rightEdge - leftEdge))
                
                
                if frequency > 1e6:
                    frequency /= 1e6
                    tempUnit = "MHz"
                elif frequency > 1e3:
                    frequency /= 1e3
                    tempUnit = "KHz"
                elif frequency > 1:
                    tempUnit = "Hz"
                elif frequency > 1e-3:
                    frequency *= 1e3
                    tempUnit = "mHz"

                
                self.ui.cursorInfoLabel.setText("t: %s[%s], Δt: %s[%s], 1/Δt: %s[%s]" %(str(np.round(self.plotter.xAxisData[self.lastCursorIndex], 3)), self.plotter.axisUnitString, str(np.round(period, 3)), self.plotter.axisUnitString, str(np.round(frequency, 3)), tempUnit))
                


        ''' 
        timer1 = time.perf_counter()
        timer2 = time.perf_counter()
        timer3 = time.perf_counter()
        print(str((timer2-timer1)*1000) + " milliseconds procesado")
        print(str((timer3-timer2)*1000) + " milliseconds dibujado")'''