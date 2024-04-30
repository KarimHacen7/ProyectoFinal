from settings import SamplingSettings, SamplingMode
from communication import CommunicationModule, SamplingWorker
from plotting import Plotter
from PySide6.QtWidgets import  QMainWindow, QMessageBox, QGraphicsScene, QGraphicsView, QCheckBox
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer, QThread, QSize, Signal
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    statusLabelTimer = QTimer()
    communicationModule = CommunicationModule()
    samplingSettings = SamplingSettings()
    plotter = Plotter()
    initialBuffer = bytearray()
    QGVReferenceList = [] # QGraphicsViewReferenceList
    resizeSignal = Signal()
    visualizedChannels = [1,2,3,4,5,6,7,8]
    dataBuffer = []
    resizeCount = 10
                        
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.configSlideAnimation = QPropertyAnimation(self.ui.slideFrameContainer, b"maximumWidth")#Animate minimumWidht
        
        self.configSlideAnimation.finished.connect(self.resizeHandler)
        self.resizeSignal.connect(self.resizeHandler)
        
        self.ui.configSliderPushButton.clicked.connect(self.sidePanelSlideAnimation)
        self.ui.samplingDepthHorizontalSlider.valueChanged.connect(self.updateSamplingDepthLabel)
        self.ui.digitalModePushButton.clicked.connect(self.restrictSettingsDigitalMode)
        self.ui.analogModePushButton.clicked.connect(self.restrictSettingsAnalogMode)
        
        self.ui.samplingDepthHorizontalSlider.valueChanged.connect(self.calculateSamplingTime)
        self.ui.samplingFrequencyComboBox.currentIndexChanged.connect(self.calculateSamplingTime)
        self.ui.samplingChannelsComboBox.currentIndexChanged.connect(self.calculateSamplingTime)
        self.ui.samplingChannelsComboBox.currentIndexChanged.connect(self.restrictTriggerChannels)
        
        self.ui.startSamplingPushButton.clicked.connect(self.sample)
        
        self.ui.channel1CheckBox.stateChanged.connect(self.hideChannels)
        self.ui.channel2CheckBox.stateChanged.connect(self.hideChannels)
        self.ui.channel3CheckBox.stateChanged.connect(self.hideChannels)
        self.ui.channel4CheckBox.stateChanged.connect(self.hideChannels)
        self.ui.channel5CheckBox.stateChanged.connect(self.hideChannels)
        self.ui.channel6CheckBox.stateChanged.connect(self.hideChannels)
        self.ui.channel7CheckBox.stateChanged.connect(self.hideChannels)
        self.ui.channel8CheckBox.stateChanged.connect(self.hideChannels)


        self.statusLabelTimer.timeout.connect(self.checkConnectedStatusAndShowInLabel)

        self.ui.digitalModePushButton.animateClick()
        self.calculateSamplingTime()

        self.statusLabelTimer.start(500)

        for item in dir(self.ui):
            ref = getattr(self.ui, item)
            if isinstance(ref, QGraphicsView):
                self.QGVReferenceList.append(ref)
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resizeSignal.emit()

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
    
    def checkConnectedStatusAndShowInLabel(self):
        isConnected = self.communicationModule.checkConnected("VID_2E8A&PID_000A")
        if isConnected:
            self.ui.connectionStatusLabel.setText("Estado: Conectado")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #4af792; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
        else:
            self.ui.connectionStatusLabel.setText("Estado: Desconectado")
            self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #ff4a4a; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")

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
        self.resizeCount = 10
        self.configSlideAnimation.start()

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

    def sample(self):
        self.statusLabelTimer.stop()
        self.ui.samplingProgressBar.setValue(0)
        self.startSamplingThread()
        return
        

    def graphChannels(self, data):
        self.dataBuffer = self.plotter.treatData(rawData=data, channelNumber=self.samplingSettings.channels)
        height = 75
        width = self.ui.channel1GraphicsView.size().width()
        for index, channel in enumerate(self.dataBuffer):
            temp = self.plotter.plotChannel(data=channel, size=(width/100, height/100), color="#FF0000")
            tempScene = QGraphicsScene()
            tempScene.addWidget(temp)
            self.QGVReferenceList[index].setScene(tempScene)

        for channelNumber in range(1, 9):
            ref = getattr(self.ui, "channel" + str(channelNumber) + "CheckBox")
            if channelNumber in range(1, self.samplingSettings.channels+1):
                ref.setChecked(True)
                ref.setEnabled(True)
            else:
                ref.setChecked(False)
                ref.setEnabled(False)
    
    def resizeHandler(self):
        if self.resizeCount < 10:
            self.resizeCount += 1
            return
        else:
            self.resizeCount = 0
            height = 75
            width = self.ui.channel1GraphicsView.size().width()
            if (len(self.dataBuffer) != 0):
                for index, channel in enumerate(self.dataBuffer):
                    temp = self.plotter.plotChannel(data=channel, size=(width/100, height/100), color="#FF0000")
                    tempScene = QGraphicsScene()
                    tempScene.addWidget(temp)
                    self.QGVReferenceList[index].setScene(tempScene)
            else:
                return
        
    def hideChannels(self):
        self.visualizedChannels.clear()
        for item in dir(self.ui):
            ref = getattr(self.ui, item)
            if (item.find("channel") != -1) and (isinstance(ref, QCheckBox)) and (ref.isChecked()):
                try:
                    self.visualizedChannels.append(int(ref.text()))
                except:
                    print("No le cambies el nombre o el texto a los checkbox!")
                    return
        for channelNumber in range(1, 9):
            ref = getattr(self.ui, "channel" + str(channelNumber) + "Frame")
            if channelNumber in self.visualizedChannels:
                ref.setMaximumHeight(75)
            else:
                ref.setMaximumHeight(0)









