import time, threading
from settings import SamplingSettings, SamplingMode
from communication import CommunicationModule
from PySide6.QtWidgets import  QMainWindow, QMessageBox
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    communicationModule = CommunicationModule()
    samplingSettings = SamplingSettings()
    quitAppEvent = threading.Event()
    samplingLock = threading.Lock()
    lastTimeout = 0.1
    lastVoltage = 1.65
    initialBuffer = bytearray()


    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.configSliderPushButton.clicked.connect(self.sidePanelSlideAnimation)
        self.ui.samplingDepthHorizontalSlider.valueChanged.connect(self.updateSamplingDepthLabel)
        self.ui.digitalModePushButton.clicked.connect(self.restrictSettingsDigitalMode)
        self.ui.analogModePushButton.clicked.connect(self.restrictSettingsAnalogMode)
        
        self.ui.samplingDepthHorizontalSlider.valueChanged.connect(self.calculateSamplingTime)
        self.ui.samplingFrequencyComboBox.currentIndexChanged.connect(self.calculateSamplingTime)
        self.ui.samplingChannelsComboBox.currentIndexChanged.connect(self.calculateSamplingTime)
        self.ui.samplingChannelsComboBox.currentIndexChanged.connect(self.restrictTriggerChannels)
        
        self.ui.startSamplingPushButton.clicked.connect(self.sample)

        self.ui.digitalModePushButton.animateClick()
        self.calculateSamplingTime()

        self.deviceCheckThread = threading.Thread(target=self.checkConnectedStatusAndShowInLabel)
        self.deviceCheckThread.start()
        self.quitAppEvent.clear()


    def checkConnectedStatusAndShowInLabel(self):
        while not self.quitAppEvent.is_set():
            self.samplingLock.acquire()
            if self.communicationModule.checkConnected("VID_2E8A&PID_000A"):
                self.ui.connectionStatusLabel.setText("Estado: Conectado")
                self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #4af792; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
            else:
                self.ui.connectionStatusLabel.setText("Estado: Desconectado")
                self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #ff4a4a; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
            self.samplingLock.release()
            time.sleep(0.25)

    def sidePanelSlideAnimation(self):
        width = self.ui.slideFrameContainer.width()
        if width == 0:
            newWidth = 200
        else:
            newWidth = 0

        self.configSlideAnimation = QPropertyAnimation(self.ui.slideFrameContainer, b"maximumWidth")#Animate minimumWidht
        self.configSlideAnimation.setDuration(250)
        self.configSlideAnimation.setStartValue(width)
        self.configSlideAnimation.setEndValue(newWidth)
        self.configSlideAnimation.setEasingCurve(QEasingCurve.InOutQuart)
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
        self.samplingLock.acquire()
        self.ui.connectionStatusLabel.setText("Estado: Muestreando")
        self.ui.connectionStatusLabel.setStyleSheet(".QLabel{background-color: #ffea5e; font-family: consolas; border: 1px solid rgb(109, 109, 109); border-radius: 5px;}")
        self.getConfigurationFromGUI()

        if self.samplingSettings.timeout != self.lastTimeout:
            self.lastTimeout = self.samplingSettings.timeout
            if self.communicationModule.sendConfigCommand(self.samplingSettings.parseTimeoutStringFromConfig()) != 1:
                QMessageBox.error(self, "Error", "Hubo un error al comunicarse con el periférico", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
                return
        
        if self.samplingSettings.compareVoltage != self.lastVoltage:
            self.lastVoltage = self.samplingSettings.compareVoltage
            if self.communicationModule.sendConfigCommand(self.samplingSettings.parseVoltageStringFromConfig()) != 1:
                QMessageBox.error(self, "Error", "Hubo un error al comunicarse con el periférico", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
                return
            
        print(self.samplingSettings.parseSamplingStringFromConfig())
        self.initialBuffer = self.communicationModule.sendSamplingCommand(self.samplingSettings.parseSamplingStringFromConfig())
            
        self.samplingLock.release()
        
        if self.initialBuffer == -1 or self.initialBuffer == -2:
            QMessageBox.warning(self, "Desconexión", "Se ha reiniciado o desconectado el periférico", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
        elif self.initialBuffer == -3:
            QMessageBox.information(self, "Timeout", "Se ha excedido el tiempo de espera indicado", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
        else:
            self.graphChannels()
            

    def graphChannels(self):
        pass
