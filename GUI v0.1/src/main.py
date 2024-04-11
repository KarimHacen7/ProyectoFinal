import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from ui_mainwindow import Ui_MainWindow
from enum import Enum

class samplingSettings():
    def __init__(self):
        self.mode = Enum('samplingMode', ['Digital', 'Analog'])
        self.triggerMode = Enum('triggerModes', ['Untriggered', 'Rising', 'Falling', 'LowLevel', 'HighLevel'])
        self.channels = 8
        self.triggerChannel = 1
        self.frequency = 16
        self.depth = 192
        self.timeout = 0.1
        self.compareVoltage = 1.65
        return
    

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.configSliderPushButton.clicked.connect(self.sidePanelSlideAnimation)
        self.ui.samplingDepthHorizontalSlider.valueChanged.connect(self.updateSamplingDepthLabel)
        self.ui.digitalModePushButton.clicked.connect(self.restrictSettingsDigitalMode)
        self.ui.analogModePushButton.clicked.connect(self.restrictSettingsAnalogMode)

        self.ui.digitalModePushButton.animateClick()

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





if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())