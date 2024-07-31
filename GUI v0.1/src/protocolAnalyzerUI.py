from ui_protocolAnalyzerUI import Ui_Dialog
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Signal, Qt
from protocolAnalysis import *
from settings import *

class analyzerUI(QDialog):
    dataBuffer = []
    edgesBuffer = []
    framesDecoded = Signal(list)
    def __init__(self):
        super(analyzerUI, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.i2cAnalyzer = I2CAnalyzer()
        self.spiAnalyzer = SPIAnalyzer()
        self.uartAnalyzer = UARTAnalyzer()
        self.plainBinaryAnalyzer = PlainBinaryAnalyzer()
        self.ui.analyzePushButton.clicked.connect(self.analyze)
        self.ui.cancelPushButton.clicked.connect(self.hide)
        self.ui.ignoreCSCheckBox.toggled.connect(self.toggleCSComboBox)
       
    def updateUI(self, samplingSettings:SamplingSettings, data:list[list[int]], edges:list[dict]):
        self.samplingSettings = samplingSettings
        self.dataBuffer = data
        self.edgesBuffer = edges
        self.channelRoles = []
        self.channelRoles.append(None for _ in range(self.samplingSettings.channels))
        for comboBox in [self.ui.txLineComboBox, self.ui.SCKComboBox, self.ui.MISOComboBox, self.ui.MOSIComboBox, self.ui.CSComboBox, self.ui.SCLComboBox, self.ui.SDAComboBox]:
            comboBox.clear()
            for possibleChannel in range(1,self.samplingSettings.channels+1, 1):
                comboBox.addItem("Canal %s" %possibleChannel)
            comboBox.setMaxCount(self.samplingSettings.channels)

        if self.samplingSettings.channels >= 4:
            for index, comboBox in enumerate([self.ui.SCKComboBox, self.ui.MOSIComboBox, self.ui.MISOComboBox, self.ui.CSComboBox]):
                comboBox.setCurrentIndex(index)
        if self.samplingSettings.channels >= 2:
            for index, comboBox in enumerate([self.ui.SCLComboBox, self.ui.SDAComboBox]):
                comboBox.setCurrentIndex(index)
    
    def analyze(self):
        pageIndex = self.ui.protocolAnalyzerWidget.currentIndex()
        reverseBits = self.ui.flipMessageBits.isChecked()
        decodedFrames = []
        try:
            if pageIndex == 0:
                decodedFrames = self.plainBinaryAnalyzer.decode(
                    data=self.dataBuffer, 
                    reverse=reverseBits)
            elif pageIndex == 1:
                decodedFrames = self.uartAnalyzer.decode(
                    data=self.dataBuffer, 
                    edges=self.edgesBuffer, 
                    txLine=self.ui.txLineComboBox.currentIndex(),
                    baudRate=int(self.ui.baudRateComboBox.currentText()),
                    dataBits=int(self.ui.dataBitsComboBox.currentText()),
                    parityBits=([None, "even", "odd"])[self.ui.parityBitComboBox.currentIndex()],
                    stopBits=int(self.ui.stopBitsComboBox.currentText()),
                    samplingFrequency=self.samplingSettings.samplingFrequenciesLUT[self.samplingSettings.frequency],
                    reverseBits=reverseBits)
            elif pageIndex == 2:
                chipSelect = None if self.ui.ignoreCSCheckBox.isChecked() else self.ui.CSComboBox.currentIndex()
                if chipSelect:
                    usedChannels = [self.ui.SCKComboBox.currentIndex(), self.ui.MOSIComboBox.currentIndex(), self.ui.MISOComboBox.currentIndex(), self.ui.CSComboBox.currentIndex()]
                    if not (len(usedChannels) == len(set(usedChannels))):
                        QMessageBox.warning(self, "Advertencia", "Se ha asignado más de un rol por canal.\nRevise su configuración y vuelva a intentarlo", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
                        return
                else:
                    usedChannels = [self.ui.SCKComboBox.currentIndex(), self.ui.MOSIComboBox.currentIndex(), self.ui.MISOComboBox.currentIndex()]
                    if not (len(usedChannels) == len(set(usedChannels))):
                        QMessageBox.warning(self, "Advertencia", "Se ha asignado más de un rol por canal.\nRevise su configuración y vuelva a intentarlo", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
                        return
                decodedFrames = self.spiAnalyzer.decode(
                    data=self.dataBuffer,
                    edges=self.edgesBuffer,
                    SCK=self.ui.SCKComboBox.currentIndex(),
                    MOSI=self.ui.MOSIComboBox.currentIndex(),
                    MISO=self.ui.MISOComboBox.currentIndex(),
                    CS=chipSelect,
                    spiMode=self.ui.SPIModeComboBox.currentIndex(),
                    reverseBits=reverseBits)
            elif pageIndex == 3:
                if self.ui.SCLComboBox.currentIndex() == self.ui.SDAComboBox.currentIndex():
                        QMessageBox.warning(self, "Advertencia", "Se ha asignado más de un rol por canal.\nRevise su configuración y vuelva a intentarlo", buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.NoButton)
                        return
                decodedFrames = self.i2cAnalyzer.decode(
                    data=self.dataBuffer,
                    edges=self.edgesBuffer, 
                    SCL=self.ui.SCLComboBox.currentIndex(),
                    SDA=self.ui.SDAComboBox.currentIndex())
            else:
                pass
        except:
            print("Excepción!")
            return
        self.framesDecoded.emit(decodedFrames)
        return
    
    def toggleCSComboBox(self):
        self.ui.CSComboBox.setEnabled(not self.ui.ignoreCSCheckBox.isChecked())
        pass