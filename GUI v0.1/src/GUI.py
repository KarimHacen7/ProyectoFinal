from settings import SamplingSettings, SamplingMode
from communication import CommunicationModule, SamplingWorker
from plotting import Plotter
from PySide6.QtWidgets import  QMainWindow, QLabel, QMessageBox, QGraphicsScene, QGraphicsView,  QCheckBox
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer, QThread, Signal
from ui_mainwindow import Ui_MainWindow
from matplotlib.backend_bases import MouseEvent, FigureCanvasBase
import numpy as np
import time

class MainWindow(QMainWindow):
    initialBuffer = bytearray()
    statusLabelTimer = QTimer()
    communicationModule = CommunicationModule()
    samplingSettings = SamplingSettings()
    plotter = Plotter()
    resizeSignal = Signal()
    QGVChannelsList = [] # QGraphicsView Reference List
    QCBChannelsList = [] # QCheckBox Reference List
    QFrChannelsList = [] # QFrame Reference List
    QGSChannelsList = [] # QGraphicsView Reference List
    selectedSamplingMode = SamplingMode.DIGITAL
    cursorCallbackIDs = []
    firstResizeDone = False
    cursorIsActive = False
    samplingOngoing = False
    lastCursorIndex = 0
    # Could not put it in plotting.py without silently crashing
    for i in range(8):
        QGSChannelsList.append(QGraphicsScene())
    QGSAxis = QGraphicsScene()
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
        for index, item in enumerate(self.QGVChannelsList):
            item.setScene(self.QGSChannelsList[index])
            self.QGSChannelsList[index].addWidget(self.plotter.channelPlots[index].canvas)
        self.ui.axisGraphicsView.setScene(self.QGSAxis)
        self.QGSAxis.addWidget(self.plotter.axisPlot.canvas)
        
        
        # Zoom in and out signals
        for channel in self.plotter.channelPlots:
            channel.canvas.mpl_connect('scroll_event', self.zoomInOut)
            channel.canvas.mpl_connect('button_press_event', self.displaceOnClick)

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
        #for checkBox in self.QCBChannelsList:
        #    checkBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel1CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel2CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel3CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel4CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel5CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel6CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel7CheckBox.stateChanged.connect(self.hideAndShowChannels)
        self.ui.channel8CheckBox.stateChanged.connect(self.hideAndShowChannels)
        # Scroll Bar navigation
        self.ui.channelHorizontalScrollBar.valueChanged.connect(self.horizontalSliderChanged)
        # Signal Analysis
        self.ui.triggerAnalysisGoLeftButton.clicked.connect(lambda: self.searchAndFocusOnEdges("left"))
        self.ui.triggerAnalysisGoRightButton.clicked.connect(lambda: self.searchAndFocusOnEdges("right"))
        self.ui.botYLimDoubleSpinBox.valueChanged.connect(lambda: self.changeAnalogYLims("bot"))
        self.ui.topYLimDoubleSpinBox.valueChanged.connect(lambda: self.changeAnalogYLims("top"))
        # Digital mode, by default
        self.ui.digitalModePushButton.animateClick()
        self.ui.lastCursorRadioButton.setChecked(True)
        self.calculateSamplingTime()
        # Status informing label
        self.statusLabelTimer.timeout.connect(self.checkConnectedStatusAndShowInLabel)
        self.statusLabelTimer.start(500)
        self.ui.cursorInfoLabel.setVisible(False)
        for item in dir(self.ui):
            ref = getattr(self.ui, item)
            if isinstance(ref, QLabel) and (item.find("Protocol") != -1):
                ref.setVisible(False)
        self.ui.triggerFrame.setVisible(False)
        

    # ---------- THREADING -- START SAMPLING ----------
    def startSamplingThread(self):
        self.getConfigurationFromGUI() # do not move further as it creates a race condition
        self.samplingOngoing = True
        self.samplingThread = QThread() 
        self.samplingWorker = SamplingWorker()
        self.samplingWorker.moveToThread(self.samplingThread)
        
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
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #64a832; font-family: consolas; border: 1px solid #31363F; border-radius: 5px;}")
            self.ui.samplingProgressBar.setValue(5)
        else:
            QMessageBox.critical(self, "Error", "Hubo un error al comunicarse con el periférico", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)

    def timeoutIsFinished(self, code):
        if code == 1:
            self.ui.connectionStatusLabel.setText("Estado: Configurado!")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #8da832; font-family: consolas; border: 1px solid #31363F; border-radius: 5px;}")
            self.ui.samplingProgressBar.setValue(15)
        else:
            QMessageBox.critical(self, "Error", "Hubo un error al comunicarse con el periférico", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)

    def commandIsAcknowledged(self):
        self.ui.connectionStatusLabel.setText("Estado: Muestreando...")
        self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #a88932; font-family: consolas; border: 1px solid #31363F; border-radius: 5px;}")
        self.ui.samplingProgressBar.setValue(25)

    def dataIsIncoming(self, length:int):
        self.ui.connectionStatusLabel.setText("Estado: Muestreando...")
        self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #a88932; font-family: consolas; border: 1px solid #31363F; border-radius: 5px;}")
        progress = 25 + int(0.75*length/(1024*self.samplingSettings.depth))
        self.ui.samplingProgressBar.setValue(progress)

    def samplingIsFinished(self, code, data):
        if code == -1 or code == -2:
            self.ui.connectionStatusLabel.setText("Estado: Desconectado")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #cd0f0f; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
            QMessageBox.warning(self, "Desconexión", "Se ha reiniciado o desconectado el periférico", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
        elif code == -3:
            QMessageBox.information(self, "Timeout", "Se ha excedido el tiempo de espera indicado", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
        else:
            self.ui.connectionStatusLabel.setText("Estado: Conectado")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #15984c; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
            self.graphChannels(data)

    def threadFinished(self):
        self.samplingOngoing = False
        self.statusLabelTimer.start()
        self.ui.samplingProgressBar.setValue(0)

    # ---------- GUI HOUSEKEEPING ----------
    def checkConnectedStatusAndShowInLabel(self):
        isConnected = self.communicationModule.checkConnected("VID_2E8A&PID_000A")
        if isConnected:
            self.ui.connectionStatusLabel.setText("Estado: Conectado")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #15984c; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
        else:
            self.ui.connectionStatusLabel.setText("Estado: Desconectado")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #cd0f0f; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")

    def updateSamplingDepthLabel(self):
        value = self.ui.samplingDepthHorizontalSlider.value()
        self.ui.samplingDepthValueLabel.setText(str(value)+" [KiB]")
        return

    def restrictSettingsAnalogMode(self):
        self.selectedSamplingMode = SamplingMode.ANALOG
        self.ui.digitalModePushButton.setStyleSheet("QPushButton { background-color: #b3b3b3; color: #525151;}")
        self.ui.analogModePushButton.setStyleSheet("QPushButton { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #222831, stop: 1 #0081cc); }")
        if self.ui.samplingFrequencyComboBox.count() == 17:
            for i in [16,15,14]:
                self.ui.samplingFrequencyComboBox.removeItem(i)
        
        if self.ui.samplingChannelsComboBox.count() == 4:
            for i in [3,2,1]:
                self.ui.samplingChannelsComboBox.removeItem(i)
        
        if self.ui.triggerChannelComboBox.count() == 8:
            for i in range(8, 0, -1):
                print(i)
                self.ui.triggerChannelComboBox.removeItem(i)
            self.ui.triggerChannelComboBox.setItemText(0, "8")

    def restrictSettingsDigitalMode(self):
        self.selectedSamplingMode  = SamplingMode.DIGITAL
        self.ui.digitalModePushButton.setStyleSheet("QPushButton {  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #222831, stop: 1 #0081cc);}")
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
        if self.selectedSamplingMode == SamplingMode.DIGITAL:
            for i in range(pow(2, self.ui.samplingChannelsComboBox.currentIndex())):
                self.ui.triggerChannelComboBox.addItem(str(i+1))
        if self.selectedSamplingMode == SamplingMode.ANALOG:
            self.ui.triggerChannelComboBox.addItem("8")

    def calculateSamplingTime(self):
        # (8[bit/B] * 1024[B/KiB]  * depth [KiB])[bit] /(frecuencia [muestra/seg] * canales [bits/muestra]) [bit/seg]  
        bits = 8*1024*self.ui.samplingDepthHorizontalSlider.value()
        bitrate = pow(2, self.ui.samplingChannelsComboBox.currentIndex()) * self.samplingSettings.samplingFrequenciesLUT[self.ui.samplingFrequencyComboBox.currentIndex()]
        samplingTime = bits/bitrate
        if self.selectedSamplingMode == SamplingMode.ANALOG:
            samplingTime /= 8 
            pass
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
        self.samplingSettings.mode = self.selectedSamplingMode
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
    
    def restrictAnalysisOptions(self):
        self.ui.triggerAnalysisChannelComboBox.setMaxCount(0)
        self.ui.triggerAnalysisChannelComboBox.setMaxCount(8)
        if self.samplingSettings.mode == SamplingMode.DIGITAL:
            for i in range(self.samplingSettings.channels):
                self.ui.triggerAnalysisChannelComboBox.addItem(str(i+1))
        elif self.samplingSettings.mode == SamplingMode.ANALOG:
            self.ui.triggerAnalysisChannelComboBox.addItem("8")


    # ---------- USER INPUT ----------
    def sample(self):
        self.statusLabelTimer.stop()
        self.ui.samplingProgressBar.setValue(0)
        if not self.samplingOngoing:
            self.startSamplingThread()
        else:
            QMessageBox.information(self, "Información", "Ya hay una orden de muestreo en proceso!", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
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
                self.plotter.channelPlots[index].isVisible = True
                self.QFrChannelsList[index].setVisible(True)
            else:
                self.plotter.channelPlots[index].isVisible = False
                self.QFrChannelsList[index].setVisible(False)
        self.drawCanvasesAndAxes(flush=False)

    def startStopCursor(self):
        if not self.cursorIsActive:
            self.cursorIsActive = True
            for channel in self.plotter.channelPlots:
                self.cursorCallbackIDs.append(channel.canvas.mpl_connect('motion_notify_event', self.cursorDrawAndCalculate))
            self.ui.cursorPushButton.setStyleSheet("QPushButton { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #222831, stop: 1 #0081cc); }")
            self.ui.cursorInfoLabel.setVisible(True)
        else:
            self.cursorIsActive = False
            for index, channel in enumerate(self.plotter.channelPlots):
                channel.canvas.mpl_disconnect(self.cursorCallbackIDs[index])
                channel.cursorLine.set_xdata([0])
                channel.cursorLine.set_visible(False)
            self.cursorCallbackIDs = []
            self.plotter.axisPlot.cursorLine.set_xdata([0])
            self.plotter.axisPlot.cursorLine.set_visible(False)
            
            self.drawCanvasesAndAxes(flush=False)
            
            self.ui.cursorPushButton.setStyleSheet("")
            self.ui.cursorInfoLabel.setVisible(False)
    
    #  ---------- PLOTTING  ----------
    def graphChannels(self, data):
        self.plotter.processAndPlot(rawdata=data, samplingSettings=self.samplingSettings)
        self.drawCanvasesAndAxes(flush=False)
        self.ui.triggerFrame.setVisible(True)
        
        if self.samplingSettings.mode == SamplingMode.DIGITAL:
            self.plotter.axisPlot.isVisible = True
            self.ui.axisFrame.setVisible(True)
            self.ui.channel1Frame.setFixedHeight(75)
            self.resizeSignal.emit()
            self.ui.triggerAnalysisFrame.setVisible(True)
            self.ui.analogYLimEditFrame.setVisible(False)
        elif self.samplingSettings.mode == SamplingMode.ANALOG:
            self.plotter.axisPlot.isVisible = False
            self.ui.axisFrame.setVisible(False)
            self.ui.channel1Frame.setFixedHeight(300)
            self.resizeSignal.emit()
            self.ui.triggerAnalysisFrame.setVisible(False)
            self.ui.analogYLimEditFrame.setVisible(True)
        

        for checkbox in self.QCBChannelsList:
            if int(checkbox.text()) in range(1, self.samplingSettings.channels+1):
                checkbox.setChecked(True)
                checkbox.setEnabled(True)
            else:
                checkbox.setChecked(False)
                checkbox.setEnabled(False)
        
        self.ui.channelHorizontalScrollBar.setMaximum(self.plotter.channelLengthInSamples)
        self.ui.channelHorizontalScrollBar.blockSignals(True)
        self.ui.channelHorizontalScrollBar.setValue(0)
        self.ui.channelHorizontalScrollBar.blockSignals(False)

        leftLim, rightLim = self.plotter.channelPlots[0].axes.get_xlim()
        rangeLimDivs = (abs(leftLim-rightLim)/self.plotter.channelLengthInUnit)*self.plotter.channelLengthInSamples
        self.ui.channelHorizontalScrollBar.setSingleStep(np.ceil(rangeLimDivs/10) if np.ceil(rangeLimDivs/10) > 2 else 2)
        self.ui.channelHorizontalScrollBar.setPageStep(np.ceil(rangeLimDivs) if np.ceil(rangeLimDivs) > 10 else 10)
        self.restrictAnalysisOptions()

    def resizeEvent(self, event):
        self.resizeSignal.emit()

    def resizeHandler(self):
        if self.firstResizeDone:
            for index, channel in enumerate(self.plotter.channelPlots):
                channel.canvas.setGeometry(0, 0, self.QGVChannelsList[index].width(), self.QGVChannelsList[index].height())
            self.plotter.axisPlot.canvas.setGeometry(0, 0, self.ui.axisGraphicsView.width(), self.ui.axisGraphicsView.height())
            self.drawCanvasesAndAxes(flush=False)
        else:
            self.firstResizeDone = True

    def zoomInOut(self, event):
        if self.plotter.plottingInProcess:
            return
        if self.plotter.dataBuffer == []:
            return
        scrolledChannel = 0

        for index, channel in enumerate(self.plotter.channelPlots):
            if channel.canvas == event.canvas:
                scrolledChannel = index 
        
        if event.xdata is not None: 
            centerLim = event.xdata
        else:
            return
        
        leftLim, rightLim = self.plotter.channelPlots[scrolledChannel].axes.get_xlim()
        
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
        
        if rightLim > self.plotter.channelLengthInUnit:
            rightLim = self.plotter.channelLengthInUnit

        # hacer esto mas claro
        if abs(leftLim-rightLim) < (20*(self.plotter.timeUnitMultiplier/self.samplingSettings.samplingFrequenciesLUT[self.samplingSettings.frequency])):
            return

        # Tarda 1 ms
        for channel in self.plotter.channelPlots:
            channel.axes.set_xlim(left=leftLim, right=rightLim)
        self.plotter.axisPlot.axes.set_xlim(left=leftLim, right=rightLim)
        # Hasta Aca
        rangeLimDivs = (abs(leftLim-rightLim)/self.plotter.channelLengthInUnit)*(self.plotter.channelLengthInSamples)
        self.ui.channelHorizontalScrollBar.setSingleStep(np.ceil(rangeLimDivs/10) if np.ceil(rangeLimDivs/10) > 2 else 2)
        self.ui.channelHorizontalScrollBar.setPageStep(np.ceil(rangeLimDivs) if np.ceil(rangeLimDivs) > 10 else 10)
        self.ui.channelHorizontalScrollBar.blockSignals(True)
        self.ui.channelHorizontalScrollBar.setValue(np.ceil((centerLim/self.plotter.channelLengthInUnit)*self.ui.channelHorizontalScrollBar.maximum()))
        self.ui.channelHorizontalScrollBar.blockSignals(False)
        self.drawCanvasesAndAxes(flush=True)

    def horizontalSliderChanged(self):
        if self.plotter.plottingInProcess:
            return
        if self.plotter.dataBuffer == []:
            return
        
        leftLim, rightLim = self.plotter.channelPlots[0].axes.get_xlim()
        rangeLim = abs(rightLim-leftLim)
        
        centerValue = (self.ui.channelHorizontalScrollBar.value()/self.ui.channelHorizontalScrollBar.maximum())*self.plotter.channelLengthInUnit
        
        leftLim=centerValue-(rangeLim/2)
        rightLim=centerValue+(rangeLim/2)
        
        if leftLim < 0:
            leftLim = 0
            rightLim = rangeLim
        elif rightLim > self.plotter.channelLengthInUnit:
            leftLim = self.plotter.channelLengthInUnit - rangeLim
            rightLim = self.plotter.channelLengthInUnit
        
        for channel in self.plotter.channelPlots:
            channel.axes.set_xlim(left=leftLim, right=rightLim)
        self.plotter.axisPlot.axes.set_xlim(left=leftLim, right=rightLim)

        self.drawCanvasesAndAxes(flush=False)

    def cursorDrawAndCalculate(self, event):
        if self.plotter.plottingInProcess:
            return
        if self.plotter.dataBuffer == []:
            return
        scrolledChannel = 0
        for index, channel in enumerate(self.plotter.channelPlots):
            if channel.canvas == event.canvas:
                scrolledChannel = index 
        
        if event.inaxes:
            index = min(np.searchsorted(self.plotter.xAxisData, event.xdata), len(self.plotter.dataBuffer[scrolledChannel]) - 1)
            
            if index != self.lastCursorIndex:
                self.lastCursorIndex = index
                for channel in self.plotter.channelPlots:
                    channel.cursorLine.set_xdata([self.plotter.xAxisData[self.lastCursorIndex]]) 
                    channel.cursorLine.set_visible(True)
                self.plotter.axisPlot.cursorLine.set_xdata([self.plotter.xAxisData[self.lastCursorIndex]])
                self.plotter.axisPlot.cursorLine.set_visible(True)
                
                for channel in self.plotter.channelPlots:
                    channel.figure.canvas.restore_region(channel.background)
                    channel.axes.draw_artist(channel.cursorLine)
                    channel.figure.canvas.blit(channel.axes.bbox)                
                
                self.plotter.axisPlot.figure.canvas.restore_region(self.plotter.axisPlot.background)
                self.plotter.axisPlot.axes.draw_artist(self.plotter.axisPlot.cursorLine)
                self.plotter.axisPlot.figure.canvas.blit(self.plotter.axisPlot.axes.bbox)
                
                # Esto hace que no se ejecute el resto de la rutina hasta que dejes quieto el cursor
                # self.drawCanvasesAndAxes(flush=True)
                # Tener en cuenta  a la hora de incorporarlo

                if self.samplingSettings.mode == SamplingMode.DIGITAL:
                    if len(self.plotter.edgesBuffer[scrolledChannel]) <= 1:
                        self.ui.cursorInfoLabel.setText("t: %s[%s], Δt: %s[%s], 1/Δt: %s[%s]" %(str(np.round(self.plotter.xAxisData[self.lastCursorIndex], 3)), self.plotter.timeUnitString, "?", self.plotter.timeUnitString, "?", "Hz"))
                    elif (index < self.plotter.edgesBuffer[scrolledChannel][0]["1"]) or (index > self.plotter.edgesBuffer[scrolledChannel][-1]["2"]):
                        self.ui.cursorInfoLabel.setText("t: %s[%s], Δt: %s[%s], 1/Δt: %s[%s]" %(str(np.round(self.plotter.xAxisData[self.lastCursorIndex], 3)), self.plotter.timeUnitString, "?", self.plotter.timeUnitString, "?", "Hz"))
                    else:
                        for i in range(len(self.plotter.edgesBuffer[scrolledChannel])-1):
                            pastEdge = self.plotter.edgesBuffer[scrolledChannel][i]
                            nextEdge = self.plotter.edgesBuffer[scrolledChannel][i+1]
                            if index > pastEdge["1"] and index < nextEdge["2"]:
                                periodInUnit = ((nextEdge["2"] - pastEdge["1"])/self.plotter.channelLengthInSamples)*self.plotter.channelLengthInUnit
                                frequency = 1/(((nextEdge["2"] - pastEdge["1"])/self.plotter.channelLengthInSamples)*self.plotter.channelLengthInSeconds)
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
                                self.ui.cursorInfoLabel.setText("t: %s[%s], Δt: %s[%s], 1/Δt: %s[%s]" %(str(np.round(self.plotter.xAxisData[self.lastCursorIndex], 3)), self.plotter.timeUnitString, str(np.round(periodInUnit, 3)), self.plotter.timeUnitString, str(np.round(frequency, 3)), tempUnit))
                else:
                    self.ui.cursorInfoLabel.setText("t: %s[%s], V: %s[%s]" %(str(np.round(self.plotter.xAxisData[self.lastCursorIndex], 3)), self.plotter.timeUnitString, self.plotter.dataBuffer[0][self.lastCursorIndex], "V"))

    def displaceOnClick(self, event):
        if self.plotter.plottingInProcess:
            return
        if self.plotter.dataBuffer == [] or not event.inaxes:
            return
        
        leftLim, rightLim = self.plotter.channelPlots[0].axes.get_xlim()
        rangeLim = abs(rightLim-leftLim)
        
        centerValue = event.xdata
        leftLim=centerValue-(rangeLim/2)
        rightLim=centerValue+(rangeLim/2)
        
        if leftLim < 0:
            leftLim = 0
            rightLim = rangeLim
        elif rightLim > self.plotter.channelLengthInUnit:
            leftLim = self.plotter.channelLengthInUnit - rangeLim
            rightLim = self.plotter.channelLengthInUnit
        
        for channel in self.plotter.channelPlots:
            channel.axes.set_xlim(left=leftLim, right=rightLim)
        self.plotter.axisPlot.axes.set_xlim(left=leftLim, right=rightLim)

        self.drawCanvasesAndAxes(flush=True)

        self.ui.channelHorizontalScrollBar.blockSignals(True)
        self.ui.channelHorizontalScrollBar.setValue(np.ceil((centerValue/self.plotter.channelLengthInUnit)*self.ui.channelHorizontalScrollBar.maximum()))
        self.ui.channelHorizontalScrollBar.blockSignals(False)

    def drawCanvasesAndAxes(self, flush=bool):
        
        if self.samplingSettings.mode == SamplingMode.ANALOG:
            leftLim, rightLim = self.plotter.channelPlots[0].axes.get_xlim()
        else:
            leftLim, rightLim = self.plotter.axisPlot.axes.get_xlim()
        
        rangeLim = abs(rightLim-leftLim)
        index = np.searchsorted(self.plotter.axisIncrements, rangeLim/25)
        step = self.plotter.axisIncrements[index]
        stringStep=str(step)
        stepDecimals = stringStep[::-1].find('.') if stringStep[::-1].find('.') != -1 else 0
        tickStart = np.round(leftLim, decimals=(stepDecimals-1)) if stepDecimals > 0 else np.round(leftLim, decimals=(stepDecimals))
        newTicks = np.arange(start=tickStart, stop=np.round(rightLim, decimals=stepDecimals), step=step)
        newTicks = np.round(newTicks, decimals=stepDecimals)
        newTicks = np.insert(arr=newTicks, obj=0, values=(tickStart-step))
        newTicks = np.insert(arr=newTicks, obj=0, values=(tickStart-(2*step)))

        
        majorTicks = []
        minorTicks = []
        for index, newTick in enumerate(newTicks):
            if (index % 3 == 0) and (newTick >= leftLim+(0.05*rangeLim)) and (newTick <= leftLim+(0.95*rangeLim)):
                majorTicks.append(newTick)
            elif (newTick >= leftLim+(0.01*rangeLim)) and (newTick <= leftLim+(0.99*rangeLim)):
                minorTicks.append(newTick)
            else:
                pass
        
        if self.samplingSettings.mode == SamplingMode.ANALOG:
            self.plotter.channelPlots[0].axes.set_xticks(majorTicks, minor=False)
            self.plotter.channelPlots[0].axes.set_xticks(minorTicks, minor=True)
            self.plotter.channelPlots[0].axes.xaxis.set_major_formatter('{x} %s' %self.plotter.timeUnitString)
        else:
            self.plotter.axisPlot.axes.set_xticks(majorTicks, minor=False)
            self.plotter.axisPlot.axes.set_xticks(minorTicks, minor=True)
            self.plotter.axisPlot.axes.xaxis.set_major_formatter('{x} %s' %self.plotter.timeUnitString)
        
        self.plotter.plottingInProcess = True    
        for channel in self.plotter.channelPlots:
            if channel.isVisible:
                channel.canvas.draw()
        if self.plotter.axisPlot.isVisible:
            self.plotter.axisPlot.canvas.draw()
        
        if flush:
            for channel in self.plotter.channelPlots:
                channel.canvas.flush_events()
            self.plotter.axisPlot.canvas.flush_events()
        
        for channel in self.plotter.channelPlots:
            if channel.isVisible:
                channel.background = channel.figure.canvas.copy_from_bbox(channel.axes.bbox)
        if self.plotter.axisPlot.isVisible:
            self.plotter.axisPlot.background = self.plotter.axisPlot.figure.canvas.copy_from_bbox(self.plotter.axisPlot.axes.bbox) 
        
        self.plotter.plottingInProcess = False

    def changeAnalogYLims(self, changed:str):
        if self.plotter.dataBuffer == [] or self.samplingSettings.mode == SamplingMode.DIGITAL:
            return
        topLim = self.ui.topYLimDoubleSpinBox.value()
        botLim = self.ui.botYLimDoubleSpinBox.value()
        if (botLim >= topLim) and (changed == "top"):
            self.ui.topYLimDoubleSpinBox.blockSignals(True)
            self.ui.topYLimDoubleSpinBox.setValue(botLim + 0.1)
            self.ui.topYLimDoubleSpinBox.blockSignals(False)
        elif (botLim >= topLim) and (changed == "bot"):
            self.ui.botYLimDoubleSpinBox.blockSignals(True)
            self.ui.botYLimDoubleSpinBox.setValue(topLim - 0.1)
            self.ui.botYLimDoubleSpinBox.blockSignals(False)
        else:
            self.plotter.channelPlots[0].axes.set_ylim(top=topLim, bottom=botLim)
            self.drawCanvasesAndAxes(flush=True)
            pass

    #  ---------- SIGNAL ANALYSIS  ----------
    def searchAndFocusOnEdges(self, direction:str):
        self.ui.triggerAnalysisGoLeftButton.setEnabled(False)
        self.ui.triggerAnalysisGoRightButton.setEnabled(False)
        if self.plotter.edgesBuffer == []:
            return
        
        channel = self.ui.triggerAnalysisChannelComboBox.currentIndex()
        leftLim, rightLim = self.plotter.channelPlots[channel].axes.get_xlim()
        rangeLim = (rightLim-leftLim)
        centerLim = leftLim+(rangeLim)/2
        if self.ui.visorCenterRadioButton.isChecked():
            index = min(np.searchsorted(self.plotter.xAxisData, centerLim), len(self.plotter.dataBuffer[channel]) - 1)
        else:
            index = self.lastCursorIndex
        result = None
        event = self.ui.triggerAnalysisModeComboBox.currentIndex()
        if (event == 0 or event == 1) and len(self.plotter.edgesBuffer[channel]) == 0:
            pass

        elif event == 0 and direction == "right":
            for edge in self.plotter.edgesBuffer[channel]:
                if edge["2"] > index and edge["type"] == "R":
                    result = edge["2"]
                    break
        elif event == 0 and direction == "left":
            for edge in reversed(self.plotter.edgesBuffer[channel]):
                if edge["1"] < index and edge["type"] == "R":
                    result = edge["1"]
                    break
        elif event == 1 and direction == "right":
            for edge in self.plotter.edgesBuffer[channel]:
                if edge["2"] > index and edge["type"] == "F":
                    result = edge["2"]
                    break
        elif event == 1 and direction == "left":
            for edge in reversed(self.plotter.edgesBuffer[channel]):
                if edge["1"] < index and edge["type"] == "F":
                    result = edge["1"]
                    break
        elif event == 2 and direction == "right":
            for j, value in enumerate(self.plotter.dataBuffer[channel]):
                if (value == 0) and (j > index):
                    result = j
                    break
        elif event == 2 and direction == "left":
            for j, value in reversed(list(enumerate(self.plotter.dataBuffer[channel]))): # no funca
                if (value == 0) and (j < index):
                    result = j
                    break
        elif event == 3 and direction == "right":
            for j, value in enumerate(self.plotter.dataBuffer[channel]):
                if (value == 1) and (j > index):
                    result = j
                    break
        elif event == 3 and direction == "left":
            for j, value in reversed(list(enumerate(self.plotter.dataBuffer[channel]))):
                if (value == 1) and (j < index):
                    result = j
                    break
        
        if result == None:
            QMessageBox.information(self, "Información", "No se ha encontrado un evento como el solicitado", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
        else:
            centerLim = self.plotter.xAxisData[result]
            leftLim=centerLim-(rangeLim/2)
            rightLim=centerLim+(rangeLim/2)
            if leftLim < 0:
                leftLim = 0
                rightLim = rangeLim
            elif rightLim > self.plotter.channelLengthInUnit:
                leftLim = self.plotter.channelLengthInUnit - rangeLim
                rightLim = self.plotter.channelLengthInUnit

            for channelPlot in self.plotter.channelPlots:
                channelPlot.axes.set_xlim(left=leftLim, right=rightLim)
            self.plotter.axisPlot.axes.set_xlim(left=leftLim, right=rightLim)

            self.drawCanvasesAndAxes(flush=True)

            self.ui.channelHorizontalScrollBar.blockSignals(True)
            self.ui.channelHorizontalScrollBar.setValue(np.ceil((centerLim/self.plotter.channelLengthInUnit)*self.ui.channelHorizontalScrollBar.maximum()))
            self.ui.channelHorizontalScrollBar.blockSignals(False)

            fakeEvent = MouseEvent(name = 'motion_notify_event', canvas=self.plotter.channelPlots[channel].canvas, x=0, y=0)
            fakeEvent.xdata = centerLim

            fakeEvent.inaxes = self.plotter.channelPlots[channel].axes
            if not self.cursorIsActive:
                self.startStopCursor()
            self.cursorDrawAndCalculate(fakeEvent)
        self.ui.triggerAnalysisGoLeftButton.setEnabled(True)
        self.ui.triggerAnalysisGoRightButton.setEnabled(True)
