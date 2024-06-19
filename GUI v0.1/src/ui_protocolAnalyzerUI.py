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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(408, 291)
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
        self.mainVerticalFrame = QFrame(self.centralwidget)
        self.mainVerticalFrame.setObjectName(u"mainVerticalFrame")
        self.mainVerticalFrame.setFrameShape(QFrame.StyledPanel)
        self.mainVerticalFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainVerticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(self.mainVerticalFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"QLabel\n"
"{\n"
"	font: 700 15pt \"Consolas\";\n"
"}")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.centralHorizontalFrame = QFrame(self.mainVerticalFrame)
        self.centralHorizontalFrame.setObjectName(u"centralHorizontalFrame")
        self.centralHorizontalFrame.setStyleSheet(u"QFrame#bitInterpretationFrame\n"
"{\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralHorizontalFrame.setFrameShape(QFrame.StyledPanel)
        self.centralHorizontalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.centralHorizontalFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.protocolAnalyzerWidget = QTabWidget(self.centralHorizontalFrame)
        self.protocolAnalyzerWidget.setObjectName(u"protocolAnalyzerWidget")
        self.protocolAnalyzerWidget.setStyleSheet(u"QTabBar::tab {\n"
"  background: #222831;\n"
"\n"
"} \n"
"QTabBar::tab:selected { \n"
"  background: #31363F;\n"
"}\n"
"QTabWidget::pane\n"
"{\n"
"	border: 1px solid rgb(109, 109, 109);\n"
"	border-radius: 5px;\n"
"	background: #222831;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.simpleBinaryTab = QWidget()
        self.simpleBinaryTab.setObjectName(u"simpleBinaryTab")
        self.gridLayout = QGridLayout(self.simpleBinaryTab)
        self.gridLayout.setObjectName(u"gridLayout")
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
        self.formLayout_3 = QFormLayout(self.UARTTab)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.baudRateLabel = QLabel(self.UARTTab)
        self.baudRateLabel.setObjectName(u"baudRateLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.baudRateLabel)

        self.baudRateComboBox = QComboBox(self.UARTTab)
        self.baudRateComboBox.addItem("")
        self.baudRateComboBox.addItem("")
        self.baudRateComboBox.addItem("")
        self.baudRateComboBox.addItem("")
        self.baudRateComboBox.addItem("")
        self.baudRateComboBox.addItem("")
        self.baudRateComboBox.addItem("")
        self.baudRateComboBox.addItem("")
        self.baudRateComboBox.addItem("")
        self.baudRateComboBox.addItem("")
        self.baudRateComboBox.addItem("")
        self.baudRateComboBox.setObjectName(u"baudRateComboBox")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.baudRateComboBox)

        self.dataBitsLabel = QLabel(self.UARTTab)
        self.dataBitsLabel.setObjectName(u"dataBitsLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.dataBitsLabel)

        self.dataBitsComboBox = QComboBox(self.UARTTab)
        self.dataBitsComboBox.addItem("")
        self.dataBitsComboBox.addItem("")
        self.dataBitsComboBox.addItem("")
        self.dataBitsComboBox.addItem("")
        self.dataBitsComboBox.addItem("")
        self.dataBitsComboBox.setObjectName(u"dataBitsComboBox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.dataBitsComboBox)

        self.parityBitsLabel = QLabel(self.UARTTab)
        self.parityBitsLabel.setObjectName(u"parityBitsLabel")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.parityBitsLabel)

        self.parityBitComboBox = QComboBox(self.UARTTab)
        self.parityBitComboBox.addItem("")
        self.parityBitComboBox.addItem("")
        self.parityBitComboBox.addItem("")
        self.parityBitComboBox.setObjectName(u"parityBitComboBox")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.parityBitComboBox)

        self.stopBitsLabel = QLabel(self.UARTTab)
        self.stopBitsLabel.setObjectName(u"stopBitsLabel")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.stopBitsLabel)

        self.stopBitsComboBox = QComboBox(self.UARTTab)
        self.stopBitsComboBox.addItem("")
        self.stopBitsComboBox.addItem("")
        self.stopBitsComboBox.setObjectName(u"stopBitsComboBox")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.stopBitsComboBox)

        self.txLineLabel = QLabel(self.UARTTab)
        self.txLineLabel.setObjectName(u"txLineLabel")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.txLineLabel)

        self.txLineComboBox = QComboBox(self.UARTTab)
        self.txLineComboBox.setObjectName(u"txLineComboBox")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.txLineComboBox)

        self.protocolAnalyzerWidget.addTab(self.UARTTab, "")
        self.SPITab = QWidget()
        self.SPITab.setObjectName(u"SPITab")
        self.formLayout = QFormLayout(self.SPITab)
        self.formLayout.setObjectName(u"formLayout")
        self.SCKLabel = QLabel(self.SPITab)
        self.SCKLabel.setObjectName(u"SCKLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.SCKLabel)

        self.SCKComboBox = QComboBox(self.SPITab)
        self.SCKComboBox.setObjectName(u"SCKComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.SCKComboBox)

        self.SPIModeComboBox = QComboBox(self.SPITab)
        self.SPIModeComboBox.addItem("")
        self.SPIModeComboBox.addItem("")
        self.SPIModeComboBox.addItem("")
        self.SPIModeComboBox.addItem("")
        self.SPIModeComboBox.setObjectName(u"SPIModeComboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.SPIModeComboBox)

        self.MOSILabel = QLabel(self.SPITab)
        self.MOSILabel.setObjectName(u"MOSILabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.MOSILabel)

        self.MOSIComboBox = QComboBox(self.SPITab)
        self.MOSIComboBox.setObjectName(u"MOSIComboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.MOSIComboBox)

        self.MISOLabel = QLabel(self.SPITab)
        self.MISOLabel.setObjectName(u"MISOLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.MISOLabel)

        self.MISOComboBox = QComboBox(self.SPITab)
        self.MISOComboBox.setObjectName(u"MISOComboBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.MISOComboBox)

        self.CSLabel = QLabel(self.SPITab)
        self.CSLabel.setObjectName(u"CSLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.CSLabel)

        self.CSComboBox = QComboBox(self.SPITab)
        self.CSComboBox.setObjectName(u"CSComboBox")
        self.CSComboBox.setStyleSheet(u"QComboBox:!enabled{\n"
"    color: rgba(238, 238, 238, 127);\n"
"}\n"
"")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.CSComboBox)

        self.ignoreCSCheckBox = QCheckBox(self.SPITab)
        self.ignoreCSCheckBox.setObjectName(u"ignoreCSCheckBox")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.ignoreCSCheckBox)

        self.protocolAnalyzerWidget.addTab(self.SPITab, "")
        self.I2CTab = QWidget()
        self.I2CTab.setObjectName(u"I2CTab")
        self.I2CTab.setStyleSheet(u"")
        self.formLayout_2 = QFormLayout(self.I2CTab)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.SCLLabel = QLabel(self.I2CTab)
        self.SCLLabel.setObjectName(u"SCLLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SCLLabel.sizePolicy().hasHeightForWidth())
        self.SCLLabel.setSizePolicy(sizePolicy)
        self.SCLLabel.setMinimumSize(QSize(0, 0))
        self.SCLLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.SCLLabel)

        self.SCLComboBox = QComboBox(self.I2CTab)
        self.SCLComboBox.setObjectName(u"SCLComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SCLComboBox.sizePolicy().hasHeightForWidth())
        self.SCLComboBox.setSizePolicy(sizePolicy1)
        self.SCLComboBox.setMinimumSize(QSize(100, 0))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.SCLComboBox)

        self.SDALabel = QLabel(self.I2CTab)
        self.SDALabel.setObjectName(u"SDALabel")
        sizePolicy.setHeightForWidth(self.SDALabel.sizePolicy().hasHeightForWidth())
        self.SDALabel.setSizePolicy(sizePolicy)
        self.SDALabel.setMinimumSize(QSize(0, 0))
        self.SDALabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.SDALabel)

        self.SDAComboBox = QComboBox(self.I2CTab)
        self.SDAComboBox.setObjectName(u"SDAComboBox")
        sizePolicy1.setHeightForWidth(self.SDAComboBox.sizePolicy().hasHeightForWidth())
        self.SDAComboBox.setSizePolicy(sizePolicy1)
        self.SDAComboBox.setMinimumSize(QSize(100, 0))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.SDAComboBox)

        self.protocolAnalyzerWidget.addTab(self.I2CTab, "")

        self.horizontalLayout_2.addWidget(self.protocolAnalyzerWidget)


        self.verticalLayout.addWidget(self.centralHorizontalFrame)

        self.pushButtonFrame = QFrame(self.mainVerticalFrame)
        self.pushButtonFrame.setObjectName(u"pushButtonFrame")
        self.pushButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.pushButtonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.pushButtonFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.flipMessageBits = QCheckBox(self.pushButtonFrame)
        self.flipMessageBits.setObjectName(u"flipMessageBits")

        self.horizontalLayout.addWidget(self.flipMessageBits)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.analyzePushButton = QPushButton(self.pushButtonFrame)
        self.analyzePushButton.setObjectName(u"analyzePushButton")

        self.horizontalLayout.addWidget(self.analyzePushButton)

        self.cancelPushButton = QPushButton(self.pushButtonFrame)
        self.cancelPushButton.setObjectName(u"cancelPushButton")

        self.horizontalLayout.addWidget(self.cancelPushButton)


        self.verticalLayout.addWidget(self.pushButtonFrame)


        self.verticalLayout_2.addWidget(self.mainVerticalFrame)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.protocolAnalyzerWidget.setCurrentIndex(3)
        self.baudRateComboBox.setCurrentIndex(4)
        self.dataBitsComboBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Agregar Analizador", None))
        self.titleLabel.setText(QCoreApplication.translate("mainWindow", u"Agregar un Analizador", None))
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
        self.baudRateLabel.setText(QCoreApplication.translate("mainWindow", u"Baud Rate", None))
        self.baudRateComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"300", None))
        self.baudRateComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"1200", None))
        self.baudRateComboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"2400", None))
        self.baudRateComboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"4800", None))
        self.baudRateComboBox.setItemText(4, QCoreApplication.translate("mainWindow", u"9600", None))
        self.baudRateComboBox.setItemText(5, QCoreApplication.translate("mainWindow", u"19200", None))
        self.baudRateComboBox.setItemText(6, QCoreApplication.translate("mainWindow", u"38400", None))
        self.baudRateComboBox.setItemText(7, QCoreApplication.translate("mainWindow", u"57600", None))
        self.baudRateComboBox.setItemText(8, QCoreApplication.translate("mainWindow", u"115200", None))
        self.baudRateComboBox.setItemText(9, QCoreApplication.translate("mainWindow", u"230400", None))
        self.baudRateComboBox.setItemText(10, QCoreApplication.translate("mainWindow", u"250000", None))

        self.baudRateComboBox.setCurrentText(QCoreApplication.translate("mainWindow", u"9600", None))
        self.dataBitsLabel.setText(QCoreApplication.translate("mainWindow", u"Bits de Datos", None))
        self.dataBitsComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"5", None))
        self.dataBitsComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"6", None))
        self.dataBitsComboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"7", None))
        self.dataBitsComboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"8", None))
        self.dataBitsComboBox.setItemText(4, QCoreApplication.translate("mainWindow", u"9", None))

        self.parityBitsLabel.setText(QCoreApplication.translate("mainWindow", u"Bits de Paridad", None))
        self.parityBitComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"Ninguno", None))
        self.parityBitComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"Par", None))
        self.parityBitComboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"Impar", None))

        self.stopBitsLabel.setText(QCoreApplication.translate("mainWindow", u"Bits de Stop", None))
        self.stopBitsComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"1", None))
        self.stopBitsComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"2", None))

        self.txLineLabel.setText(QCoreApplication.translate("mainWindow", u"Transmisor", None))
        self.protocolAnalyzerWidget.setTabText(self.protocolAnalyzerWidget.indexOf(self.UARTTab), QCoreApplication.translate("mainWindow", u"UART/USART", None))
        self.SCKLabel.setText(QCoreApplication.translate("mainWindow", u"Clock", None))
        self.SPIModeComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"Pol 0, Fase 0 ", None))
        self.SPIModeComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"Pol 0, Fase 1", None))
        self.SPIModeComboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"Pol 1, Fase 0", None))
        self.SPIModeComboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"Pol 1, Fase 1", None))

        self.MOSILabel.setText(QCoreApplication.translate("mainWindow", u"Master Out/Slave In", None))
        self.MISOLabel.setText(QCoreApplication.translate("mainWindow", u"Master In/Slave Out", None))
        self.CSLabel.setText(QCoreApplication.translate("mainWindow", u"Chip Select", None))
        self.ignoreCSCheckBox.setText(QCoreApplication.translate("mainWindow", u"Ignorar Chip Select", None))
        self.protocolAnalyzerWidget.setTabText(self.protocolAnalyzerWidget.indexOf(self.SPITab), QCoreApplication.translate("mainWindow", u"SPI", None))
        self.SCLLabel.setText(QCoreApplication.translate("mainWindow", u"SCL    ", None))
        self.SDALabel.setText(QCoreApplication.translate("mainWindow", u"SDA    ", None))
        self.protocolAnalyzerWidget.setTabText(self.protocolAnalyzerWidget.indexOf(self.I2CTab), QCoreApplication.translate("mainWindow", u"I2C", None))
        self.flipMessageBits.setText(QCoreApplication.translate("mainWindow", u"Invertir Bits", None))
        self.analyzePushButton.setText(QCoreApplication.translate("mainWindow", u"Analizar", None))
        self.cancelPushButton.setText(QCoreApplication.translate("mainWindow", u"Cancelar", None))
    # retranslateUi

