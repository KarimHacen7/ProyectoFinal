# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'protocolAnalyzerUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(351, 290)
        mainWindow.setStyleSheet(u"*{\n"
"	color: #EEEEEE;\n"
"	background-color: #222831;\n"
"	font: 9pt \"Consolas\";\n"
"}\n"
".QPushButton, .QComboBox, QDoubleSpinBox\n"
"{\n"
"	background-color: #31363F;\n"
"	color:#EEEEEE\n"
"}")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel\n"
"{\n"
"	font: 700 15pt \"Consolas\";\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.protocolAnalyzerWidget = QTabWidget(self.frame)
        self.protocolAnalyzerWidget.setObjectName(u"protocolAnalyzerWidget")
        self.protocolAnalyzerWidget.setStyleSheet(u"QTabBar::tab {\n"
"  background: #222831;\n"
"} \n"
"QTabBar::tab:selected { \n"
"  background: #31363F;\n"
"}\n"
"QTabWidget::pane\n"
"{\n"
"	border: none;\n"
"	background: #222831;\n"
"}\n"
"\n"
"\n"
"")
        self.simpleBinaryTab = QWidget()
        self.simpleBinaryTab.setObjectName(u"simpleBinaryTab")
        self.gridLayout = QGridLayout(self.simpleBinaryTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bitPonderationFrame = QFrame(self.simpleBinaryTab)
        self.bitPonderationFrame.setObjectName(u"bitPonderationFrame")
        self.bitPonderationFrame.setFrameShape(QFrame.StyledPanel)
        self.bitPonderationFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bitPonderationFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bitPonderationLabel = QLabel(self.bitPonderationFrame)
        self.bitPonderationLabel.setObjectName(u"bitPonderationLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bitPonderationLabel.sizePolicy().hasHeightForWidth())
        self.bitPonderationLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.bitPonderationLabel)

        self.channel1MSBRadioButton = QRadioButton(self.bitPonderationFrame)
        self.channel1MSBRadioButton.setObjectName(u"channel1MSBRadioButton")
        self.channel1MSBRadioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.channel1MSBRadioButton)

        self.channel1LSBRadioButton = QRadioButton(self.bitPonderationFrame)
        self.channel1LSBRadioButton.setObjectName(u"channel1LSBRadioButton")
        self.channel1LSBRadioButton.setChecked(False)

        self.verticalLayout_3.addWidget(self.channel1LSBRadioButton)


        self.gridLayout.addWidget(self.bitPonderationFrame, 1, 1, 1, 1)

        self.bitInterpretationFrame = QFrame(self.simpleBinaryTab)
        self.bitInterpretationFrame.setObjectName(u"bitInterpretationFrame")
        self.bitInterpretationFrame.setFrameShape(QFrame.StyledPanel)
        self.bitInterpretationFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.bitInterpretationFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.interpretationLabel = QLabel(self.bitInterpretationFrame)
        self.interpretationLabel.setObjectName(u"interpretationLabel")

        self.verticalLayout_4.addWidget(self.interpretationLabel)

        self.binaryInterpretationRadioButton = QRadioButton(self.bitInterpretationFrame)
        self.binaryInterpretationRadioButton.setObjectName(u"binaryInterpretationRadioButton")
        self.binaryInterpretationRadioButton.setChecked(True)

        self.verticalLayout_4.addWidget(self.binaryInterpretationRadioButton)

        self.decimalInterpretationRadioButton = QRadioButton(self.bitInterpretationFrame)
        self.decimalInterpretationRadioButton.setObjectName(u"decimalInterpretationRadioButton")

        self.verticalLayout_4.addWidget(self.decimalInterpretationRadioButton)

        self.hexadecimalInterpretationRadioButton = QRadioButton(self.bitInterpretationFrame)
        self.hexadecimalInterpretationRadioButton.setObjectName(u"hexadecimalInterpretationRadioButton")

        self.verticalLayout_4.addWidget(self.hexadecimalInterpretationRadioButton)

        self.ASCIIInterpretationRadioButton = QRadioButton(self.bitInterpretationFrame)
        self.ASCIIInterpretationRadioButton.setObjectName(u"ASCIIInterpretationRadioButton")

        self.verticalLayout_4.addWidget(self.ASCIIInterpretationRadioButton)


        self.gridLayout.addWidget(self.bitInterpretationFrame, 1, 0, 1, 1)

        self.channelSelectionFrame = QFrame(self.simpleBinaryTab)
        self.channelSelectionFrame.setObjectName(u"channelSelectionFrame")
        self.channelSelectionFrame.setStyleSheet(u"QCheckBox:disabled\n"
"{\n"
"	color: rgba(255, 255, 255, 90);\n"
"}")
        self.channelSelectionFrame.setFrameShape(QFrame.StyledPanel)
        self.channelSelectionFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.channelSelectionFrame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.channelSelectionLabel = QLabel(self.channelSelectionFrame)
        self.channelSelectionLabel.setObjectName(u"channelSelectionLabel")
        self.channelSelectionLabel.setMinimumSize(QSize(0, 20))
        self.channelSelectionLabel.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.channelSelectionLabel.setFont(font1)
        self.channelSelectionLabel.setStyleSheet(u"*{padding-right: 5px;}")
        self.channelSelectionLabel.setWordWrap(False)

        self.horizontalLayout_14.addWidget(self.channelSelectionLabel)

        self.channel1CheckBox = QCheckBox(self.channelSelectionFrame)
        self.channel1CheckBox.setObjectName(u"channel1CheckBox")
        self.channel1CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel1CheckBox)

        self.channel2CheckBox = QCheckBox(self.channelSelectionFrame)
        self.channel2CheckBox.setObjectName(u"channel2CheckBox")
        self.channel2CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel2CheckBox)

        self.channel3CheckBox = QCheckBox(self.channelSelectionFrame)
        self.channel3CheckBox.setObjectName(u"channel3CheckBox")
        self.channel3CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel3CheckBox)

        self.channel4CheckBox = QCheckBox(self.channelSelectionFrame)
        self.channel4CheckBox.setObjectName(u"channel4CheckBox")
        self.channel4CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel4CheckBox)

        self.channel5CheckBox = QCheckBox(self.channelSelectionFrame)
        self.channel5CheckBox.setObjectName(u"channel5CheckBox")
        self.channel5CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel5CheckBox)

        self.channel6CheckBox = QCheckBox(self.channelSelectionFrame)
        self.channel6CheckBox.setObjectName(u"channel6CheckBox")
        self.channel6CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel6CheckBox)

        self.channel7CheckBox = QCheckBox(self.channelSelectionFrame)
        self.channel7CheckBox.setObjectName(u"channel7CheckBox")
        self.channel7CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel7CheckBox)

        self.channel8CheckBox = QCheckBox(self.channelSelectionFrame)
        self.channel8CheckBox.setObjectName(u"channel8CheckBox")
        self.channel8CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel8CheckBox)


        self.gridLayout.addWidget(self.channelSelectionFrame, 0, 0, 1, 2)

        self.protocolAnalyzerWidget.addTab(self.simpleBinaryTab, "")
        self.UARTTab = QWidget()
        self.UARTTab.setObjectName(u"UARTTab")
        self.verticalLayout_5 = QVBoxLayout(self.UARTTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.UARTTab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.comboBox = QComboBox(self.UARTTab)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.label_4 = QLabel(self.UARTTab)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.comboBox_2 = QComboBox(self.UARTTab)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_2)

        self.label_3 = QLabel(self.UARTTab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.comboBox_3 = QComboBox(self.UARTTab)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_3)

        self.label_5 = QLabel(self.UARTTab)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.comboBox_4 = QComboBox(self.UARTTab)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox_4)

        self.comboBox_5 = QComboBox(self.UARTTab)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBox_5)

        self.comboBox_6 = QComboBox(self.UARTTab)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.comboBox_6)

        self.label_6 = QLabel(self.UARTTab)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.UARTTab)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)


        self.verticalLayout_5.addLayout(self.formLayout)

        self.protocolAnalyzerWidget.addTab(self.UARTTab, "")
        self.SPITab = QWidget()
        self.SPITab.setObjectName(u"SPITab")
        self.verticalLayout_6 = QVBoxLayout(self.SPITab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.comboBox_7 = QComboBox(self.SPITab)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_7)

        self.label_9 = QLabel(self.SPITab)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.comboBox_8 = QComboBox(self.SPITab)
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.comboBox_8)

        self.label_10 = QLabel(self.SPITab)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.comboBox_9 = QComboBox(self.SPITab)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.comboBox_9)

        self.label_11 = QLabel(self.SPITab)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.comboBox_10 = QComboBox(self.SPITab)
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.comboBox_10)

        self.checkBox = QCheckBox(self.SPITab)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.checkBox)

        self.comboBox_11 = QComboBox(self.SPITab)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox_11)

        self.label_8 = QLabel(self.SPITab)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)


        self.verticalLayout_6.addLayout(self.formLayout_2)

        self.protocolAnalyzerWidget.addTab(self.SPITab, "")
        self.I2CTab = QWidget()
        self.I2CTab.setObjectName(u"I2CTab")
        self.I2CTab.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.I2CTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.formLayout_3.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_3.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_13 = QLabel(self.I2CTab)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setMinimumSize(QSize(75, 0))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.comboBox_13 = QComboBox(self.I2CTab)
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setMinimumSize(QSize(100, 0))

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.comboBox_13)

        self.label_12 = QLabel(self.I2CTab)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(75, 0))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.comboBox_12 = QComboBox(self.I2CTab)
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setMinimumSize(QSize(100, 0))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.comboBox_12)


        self.gridLayout_2.addLayout(self.formLayout_3, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.protocolAnalyzerWidget.addTab(self.I2CTab, "")

        self.verticalLayout.addWidget(self.protocolAnalyzerWidget)

        self.pushButtonFrame = QFrame(self.frame)
        self.pushButtonFrame.setObjectName(u"pushButtonFrame")
        self.pushButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.pushButtonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.pushButtonFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.analyzePushButton = QPushButton(self.pushButtonFrame)
        self.analyzePushButton.setObjectName(u"analyzePushButton")

        self.horizontalLayout.addWidget(self.analyzePushButton)

        self.cancelPushButton = QPushButton(self.pushButtonFrame)
        self.cancelPushButton.setObjectName(u"cancelPushButton")

        self.horizontalLayout.addWidget(self.cancelPushButton)


        self.verticalLayout.addWidget(self.pushButtonFrame)


        self.verticalLayout_2.addWidget(self.frame)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.protocolAnalyzerWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(4)
        self.comboBox_2.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Agregar Analizador", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Agregar un Analizador", None))
        self.bitPonderationLabel.setText(QCoreApplication.translate("mainWindow", u"Ponderaci\u00f3n de Bits", None))
        self.channel1MSBRadioButton.setText(QCoreApplication.translate("mainWindow", u"Canal 1 MSB", None))
        self.channel1LSBRadioButton.setText(QCoreApplication.translate("mainWindow", u"Canal 1 LSB", None))
        self.interpretationLabel.setText(QCoreApplication.translate("mainWindow", u"Interpretado", None))
        self.binaryInterpretationRadioButton.setText(QCoreApplication.translate("mainWindow", u"Binario", None))
        self.decimalInterpretationRadioButton.setText(QCoreApplication.translate("mainWindow", u"Decimal", None))
        self.hexadecimalInterpretationRadioButton.setText(QCoreApplication.translate("mainWindow", u"Hexadecimal", None))
        self.ASCIIInterpretationRadioButton.setText(QCoreApplication.translate("mainWindow", u"ASCII", None))
        self.channelSelectionLabel.setText(QCoreApplication.translate("mainWindow", u"Canales:", None))
        self.channel1CheckBox.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.channel2CheckBox.setText(QCoreApplication.translate("mainWindow", u"2", None))
        self.channel3CheckBox.setText(QCoreApplication.translate("mainWindow", u"3", None))
        self.channel4CheckBox.setText(QCoreApplication.translate("mainWindow", u"4", None))
        self.channel5CheckBox.setText(QCoreApplication.translate("mainWindow", u"5", None))
        self.channel6CheckBox.setText(QCoreApplication.translate("mainWindow", u"6", None))
        self.channel7CheckBox.setText(QCoreApplication.translate("mainWindow", u"7", None))
        self.channel8CheckBox.setText(QCoreApplication.translate("mainWindow", u"8", None))
        self.protocolAnalyzerWidget.setTabText(self.protocolAnalyzerWidget.indexOf(self.simpleBinaryTab), QCoreApplication.translate("mainWindow", u"Paralelo", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Baud Rate", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"300", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"1200", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"2400", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"4800", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("mainWindow", u"9600", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("mainWindow", u"19200", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("mainWindow", u"38400", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("mainWindow", u"57600", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("mainWindow", u"115200", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("mainWindow", u"9600", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"Bits de Datos", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("mainWindow", u"5", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("mainWindow", u"6", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("mainWindow", u"7", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("mainWindow", u"8", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("mainWindow", u"9", None))

        self.label_3.setText(QCoreApplication.translate("mainWindow", u"Bits de Paridad", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("mainWindow", u"Ninguno", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("mainWindow", u"Par", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("mainWindow", u"Impar", None))

        self.label_5.setText(QCoreApplication.translate("mainWindow", u"Bits de Stop", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("mainWindow", u"1", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("mainWindow", u"2", None))

        self.label_6.setText(QCoreApplication.translate("mainWindow", u"Transmisor", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"Receptor", None))
        self.protocolAnalyzerWidget.setTabText(self.protocolAnalyzerWidget.indexOf(self.UARTTab), QCoreApplication.translate("mainWindow", u"UART/USART", None))
        self.label_9.setText(QCoreApplication.translate("mainWindow", u"Master In/Slave Out", None))
        self.label_10.setText(QCoreApplication.translate("mainWindow", u"Master Out/Slave In", None))
        self.label_11.setText(QCoreApplication.translate("mainWindow", u"Chip Select", None))
        self.checkBox.setText(QCoreApplication.translate("mainWindow", u"Ignorar Chip Select", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("mainWindow", u"Pol 0, Fase 0 ", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("mainWindow", u"Pol 0, Fase 1", None))
        self.comboBox_11.setItemText(2, QCoreApplication.translate("mainWindow", u"Pol 1, Fase 0", None))
        self.comboBox_11.setItemText(3, QCoreApplication.translate("mainWindow", u"Pol 1, Fase 1", None))

        self.label_8.setText(QCoreApplication.translate("mainWindow", u"Clock", None))
        self.protocolAnalyzerWidget.setTabText(self.protocolAnalyzerWidget.indexOf(self.SPITab), QCoreApplication.translate("mainWindow", u"SPI", None))
        self.label_13.setText(QCoreApplication.translate("mainWindow", u"SDA", None))
        self.label_12.setText(QCoreApplication.translate("mainWindow", u"SCL", None))
        self.protocolAnalyzerWidget.setTabText(self.protocolAnalyzerWidget.indexOf(self.I2CTab), QCoreApplication.translate("mainWindow", u"I2C", None))
        self.analyzePushButton.setText(QCoreApplication.translate("mainWindow", u"Analizar", None))
        self.cancelPushButton.setText(QCoreApplication.translate("mainWindow", u"Cancelar", None))
    # retranslateUi

