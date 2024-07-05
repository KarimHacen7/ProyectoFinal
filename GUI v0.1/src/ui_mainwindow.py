# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QScrollArea,
    QScrollBar, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 757)
        MainWindow.setMinimumSize(QSize(950, 0))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/ButtonIcons/ico/square wave.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	color: #EEEEEE;\n"
"	background-color: #222831;\n"
"	font: 9pt \"Consolas\";\n"
"}\n"
".QPushButton, .QComboBox, QDoubleSpinBox\n"
"{\n"
"	background-color: #31363F;\n"
"	color:#EEEEEE\n"
"}\n"
"")
        MainWindow.setIconSize(QSize(100, 24))
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainFrame = QFrame(self.centralWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"QScrollArea QScrollBar::add-page:vertical\n"
"{\n"
"		background-color:#31363F;\n"
"}\n"
"\n"
"QScrollArea QScrollBar::sub-page:vertical\n"
"{\n"
"		background-color:#31363F;\n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:disabled\n"
"{\n"
"	background-color:#31363F;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.headerMainFrame = QFrame(self.mainFrame)
        self.headerMainFrame.setObjectName(u"headerMainFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerMainFrame.sizePolicy().hasHeightForWidth())
        self.headerMainFrame.setSizePolicy(sizePolicy)
        self.headerMainFrame.setMinimumSize(QSize(0, 30))
        self.headerMainFrame.setMaximumSize(QSize(16777215, 30))
        self.headerMainFrame.setFrameShape(QFrame.StyledPanel)
        self.headerMainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.headerMainFrame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.channelVisualizationFrame = QFrame(self.headerMainFrame)
        self.channelVisualizationFrame.setObjectName(u"channelVisualizationFrame")
        self.channelVisualizationFrame.setStyleSheet(u"QCheckBox:disabled\n"
"{\n"
"	color: rgba(255, 255, 255, 90);\n"
"}")
        self.channelVisualizationFrame.setFrameShape(QFrame.StyledPanel)
        self.channelVisualizationFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.channelVisualizationFrame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.channelVisualizationLabel = QLabel(self.channelVisualizationFrame)
        self.channelVisualizationLabel.setObjectName(u"channelVisualizationLabel")
        self.channelVisualizationLabel.setMinimumSize(QSize(0, 20))
        self.channelVisualizationLabel.setMaximumSize(QSize(16777215, 20))
        self.channelVisualizationLabel.setFont(font)
        self.channelVisualizationLabel.setStyleSheet(u"*{padding-right: 5px;}")
        self.channelVisualizationLabel.setWordWrap(False)

        self.horizontalLayout_14.addWidget(self.channelVisualizationLabel)

        self.channel1CheckBox = QCheckBox(self.channelVisualizationFrame)
        self.channel1CheckBox.setObjectName(u"channel1CheckBox")
        self.channel1CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel1CheckBox)

        self.channel2CheckBox = QCheckBox(self.channelVisualizationFrame)
        self.channel2CheckBox.setObjectName(u"channel2CheckBox")
        self.channel2CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel2CheckBox)

        self.channel3CheckBox = QCheckBox(self.channelVisualizationFrame)
        self.channel3CheckBox.setObjectName(u"channel3CheckBox")
        self.channel3CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel3CheckBox)

        self.channel4CheckBox = QCheckBox(self.channelVisualizationFrame)
        self.channel4CheckBox.setObjectName(u"channel4CheckBox")
        self.channel4CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel4CheckBox)

        self.channel5CheckBox = QCheckBox(self.channelVisualizationFrame)
        self.channel5CheckBox.setObjectName(u"channel5CheckBox")
        self.channel5CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel5CheckBox)

        self.channel6CheckBox = QCheckBox(self.channelVisualizationFrame)
        self.channel6CheckBox.setObjectName(u"channel6CheckBox")
        self.channel6CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel6CheckBox)

        self.channel7CheckBox = QCheckBox(self.channelVisualizationFrame)
        self.channel7CheckBox.setObjectName(u"channel7CheckBox")
        self.channel7CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel7CheckBox)

        self.channel8CheckBox = QCheckBox(self.channelVisualizationFrame)
        self.channel8CheckBox.setObjectName(u"channel8CheckBox")
        self.channel8CheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.channel8CheckBox)


        self.horizontalLayout_13.addWidget(self.channelVisualizationFrame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.clearProtocolAnalysisPushButton = QPushButton(self.headerMainFrame)
        self.clearProtocolAnalysisPushButton.setObjectName(u"clearProtocolAnalysisPushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clearProtocolAnalysisPushButton.sizePolicy().hasHeightForWidth())
        self.clearProtocolAnalysisPushButton.setSizePolicy(sizePolicy1)
        self.clearProtocolAnalysisPushButton.setMinimumSize(QSize(30, 30))
        self.clearProtocolAnalysisPushButton.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/ButtonIcons/ico/Clear Analyze.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearProtocolAnalysisPushButton.setIcon(icon1)
        self.clearProtocolAnalysisPushButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_13.addWidget(self.clearProtocolAnalysisPushButton)

        self.protocolAnalysisPushButton = QPushButton(self.headerMainFrame)
        self.protocolAnalysisPushButton.setObjectName(u"protocolAnalysisPushButton")
        sizePolicy1.setHeightForWidth(self.protocolAnalysisPushButton.sizePolicy().hasHeightForWidth())
        self.protocolAnalysisPushButton.setSizePolicy(sizePolicy1)
        self.protocolAnalysisPushButton.setMinimumSize(QSize(30, 30))
        self.protocolAnalysisPushButton.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/ButtonIcons/ico/Analyze.png", QSize(), QIcon.Normal, QIcon.Off)
        self.protocolAnalysisPushButton.setIcon(icon2)
        self.protocolAnalysisPushButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_13.addWidget(self.protocolAnalysisPushButton)

        self.fixedCursorsPushButton = QPushButton(self.headerMainFrame)
        self.fixedCursorsPushButton.setObjectName(u"fixedCursorsPushButton")
        sizePolicy1.setHeightForWidth(self.fixedCursorsPushButton.sizePolicy().hasHeightForWidth())
        self.fixedCursorsPushButton.setSizePolicy(sizePolicy1)
        self.fixedCursorsPushButton.setMinimumSize(QSize(30, 30))
        self.fixedCursorsPushButton.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/ButtonIcons/ico/Fixed Measurements.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fixedCursorsPushButton.setIcon(icon3)
        self.fixedCursorsPushButton.setIconSize(QSize(27, 27))

        self.horizontalLayout_13.addWidget(self.fixedCursorsPushButton)

        self.cursorPushButton = QPushButton(self.headerMainFrame)
        self.cursorPushButton.setObjectName(u"cursorPushButton")
        self.cursorPushButton.setMinimumSize(QSize(30, 30))
        self.cursorPushButton.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u":/ButtonIcons/ico/Crosshair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cursorPushButton.setIcon(icon4)
        self.cursorPushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.cursorPushButton)

        self.startSamplingPushButton = QPushButton(self.headerMainFrame)
        self.startSamplingPushButton.setObjectName(u"startSamplingPushButton")
        sizePolicy1.setHeightForWidth(self.startSamplingPushButton.sizePolicy().hasHeightForWidth())
        self.startSamplingPushButton.setSizePolicy(sizePolicy1)
        self.startSamplingPushButton.setMinimumSize(QSize(30, 30))
        self.startSamplingPushButton.setMaximumSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u":/ButtonIcons/ico/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startSamplingPushButton.setIcon(icon5)
        self.startSamplingPushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.startSamplingPushButton)

        self.configSliderPushButton = QPushButton(self.headerMainFrame)
        self.configSliderPushButton.setObjectName(u"configSliderPushButton")
        self.configSliderPushButton.setMinimumSize(QSize(30, 30))
        self.configSliderPushButton.setMaximumSize(QSize(30, 30))
        self.configSliderPushButton.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/ButtonIcons/ico/Three stripes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.configSliderPushButton.setIcon(icon6)
        self.configSliderPushButton.setIconSize(QSize(23, 23))

        self.horizontalLayout_13.addWidget(self.configSliderPushButton)


        self.verticalLayout_19.addWidget(self.headerMainFrame)

        self.logicAnalyzersScrollArea = QScrollArea(self.mainFrame)
        self.logicAnalyzersScrollArea.setObjectName(u"logicAnalyzersScrollArea")
        self.logicAnalyzersScrollArea.setStyleSheet(u"")
        self.logicAnalyzersScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.logicAnalyzersScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.logicAnalyzersScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 705, 659))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.axisFrame = QFrame(self.scrollAreaWidgetContents)
        self.axisFrame.setObjectName(u"axisFrame")
        self.axisFrame.setFrameShape(QFrame.StyledPanel)
        self.axisFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.axisFrame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.axisLabel = QLabel(self.axisFrame)
        self.axisLabel.setObjectName(u"axisLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.axisLabel.sizePolicy().hasHeightForWidth())
        self.axisLabel.setSizePolicy(sizePolicy2)
        self.axisLabel.setMinimumSize(QSize(64, 0))
        self.axisLabel.setMaximumSize(QSize(62, 16777215))
        self.axisLabel.setFont(font)
        self.axisLabel.setStyleSheet(u"*\n"
"{\n"
"\n"
"font: 9pt \"Consolas\";\n"
"}")

        self.horizontalLayout_18.addWidget(self.axisLabel)

        self.axisGraphicsView = QGraphicsView(self.axisFrame)
        self.axisGraphicsView.setObjectName(u"axisGraphicsView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.axisGraphicsView.sizePolicy().hasHeightForWidth())
        self.axisGraphicsView.setSizePolicy(sizePolicy3)
        self.axisGraphicsView.setMinimumSize(QSize(0, 50))
        self.axisGraphicsView.setMaximumSize(QSize(16777215, 50))
        self.axisGraphicsView.setFrameShadow(QFrame.Raised)
        self.axisGraphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.axisGraphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_18.addWidget(self.axisGraphicsView)


        self.verticalLayout_17.addWidget(self.axisFrame)

        self.channel1Frame = QFrame(self.scrollAreaWidgetContents)
        self.channel1Frame.setObjectName(u"channel1Frame")
        sizePolicy.setHeightForWidth(self.channel1Frame.sizePolicy().hasHeightForWidth())
        self.channel1Frame.setSizePolicy(sizePolicy)
        self.channel1Frame.setMaximumSize(QSize(16777215, 75))
        self.channel1Frame.setFrameShape(QFrame.StyledPanel)
        self.channel1Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.channel1Frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.channel1LabelFrame = QFrame(self.channel1Frame)
        self.channel1LabelFrame.setObjectName(u"channel1LabelFrame")
        sizePolicy2.setHeightForWidth(self.channel1LabelFrame.sizePolicy().hasHeightForWidth())
        self.channel1LabelFrame.setSizePolicy(sizePolicy2)
        self.channel1LabelFrame.setFrameShape(QFrame.StyledPanel)
        self.channel1LabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.channel1LabelFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.channel1IDLabel = QLabel(self.channel1LabelFrame)
        self.channel1IDLabel.setObjectName(u"channel1IDLabel")
        self.channel1IDLabel.setMinimumSize(QSize(62, 0))
        self.channel1IDLabel.setMaximumSize(QSize(62, 16777215))

        self.verticalLayout_10.addWidget(self.channel1IDLabel)

        self.channel1ProtocolLabel = QLabel(self.channel1LabelFrame)
        self.channel1ProtocolLabel.setObjectName(u"channel1ProtocolLabel")

        self.verticalLayout_10.addWidget(self.channel1ProtocolLabel)


        self.horizontalLayout_4.addWidget(self.channel1LabelFrame)

        self.channel1GraphicsView = QGraphicsView(self.channel1Frame)
        self.channel1GraphicsView.setObjectName(u"channel1GraphicsView")
        self.channel1GraphicsView.setFrameShadow(QFrame.Raised)
        self.channel1GraphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.channel1GraphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_4.addWidget(self.channel1GraphicsView)


        self.verticalLayout_17.addWidget(self.channel1Frame)

        self.channel2Frame = QFrame(self.scrollAreaWidgetContents)
        self.channel2Frame.setObjectName(u"channel2Frame")
        sizePolicy.setHeightForWidth(self.channel2Frame.sizePolicy().hasHeightForWidth())
        self.channel2Frame.setSizePolicy(sizePolicy)
        self.channel2Frame.setMaximumSize(QSize(16777215, 75))
        self.channel2Frame.setFont(font)
        self.channel2Frame.setFrameShape(QFrame.StyledPanel)
        self.channel2Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.channel2Frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.channel2LabelFrame = QFrame(self.channel2Frame)
        self.channel2LabelFrame.setObjectName(u"channel2LabelFrame")
        sizePolicy2.setHeightForWidth(self.channel2LabelFrame.sizePolicy().hasHeightForWidth())
        self.channel2LabelFrame.setSizePolicy(sizePolicy2)
        self.channel2LabelFrame.setFrameShape(QFrame.StyledPanel)
        self.channel2LabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.channel2LabelFrame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.channel2IDLabel = QLabel(self.channel2LabelFrame)
        self.channel2IDLabel.setObjectName(u"channel2IDLabel")
        self.channel2IDLabel.setMinimumSize(QSize(62, 0))
        self.channel2IDLabel.setMaximumSize(QSize(62, 16777215))

        self.verticalLayout_11.addWidget(self.channel2IDLabel)

        self.channel2ProtocolLabel = QLabel(self.channel2LabelFrame)
        self.channel2ProtocolLabel.setObjectName(u"channel2ProtocolLabel")

        self.verticalLayout_11.addWidget(self.channel2ProtocolLabel)


        self.horizontalLayout_5.addWidget(self.channel2LabelFrame)

        self.channel2GraphicsView = QGraphicsView(self.channel2Frame)
        self.channel2GraphicsView.setObjectName(u"channel2GraphicsView")
        self.channel2GraphicsView.setFrameShadow(QFrame.Raised)
        self.channel2GraphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.channel2GraphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_5.addWidget(self.channel2GraphicsView)


        self.verticalLayout_17.addWidget(self.channel2Frame)

        self.channel3Frame = QFrame(self.scrollAreaWidgetContents)
        self.channel3Frame.setObjectName(u"channel3Frame")
        sizePolicy.setHeightForWidth(self.channel3Frame.sizePolicy().hasHeightForWidth())
        self.channel3Frame.setSizePolicy(sizePolicy)
        self.channel3Frame.setMaximumSize(QSize(16777215, 75))
        self.channel3Frame.setFrameShape(QFrame.StyledPanel)
        self.channel3Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.channel3Frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.channel3LabelFrame = QFrame(self.channel3Frame)
        self.channel3LabelFrame.setObjectName(u"channel3LabelFrame")
        sizePolicy2.setHeightForWidth(self.channel3LabelFrame.sizePolicy().hasHeightForWidth())
        self.channel3LabelFrame.setSizePolicy(sizePolicy2)
        self.channel3LabelFrame.setFrameShape(QFrame.StyledPanel)
        self.channel3LabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.channel3LabelFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.channel3IDLabel = QLabel(self.channel3LabelFrame)
        self.channel3IDLabel.setObjectName(u"channel3IDLabel")
        self.channel3IDLabel.setMinimumSize(QSize(62, 0))
        self.channel3IDLabel.setMaximumSize(QSize(62, 16777215))

        self.verticalLayout_12.addWidget(self.channel3IDLabel)

        self.channel3ProtocolLabel = QLabel(self.channel3LabelFrame)
        self.channel3ProtocolLabel.setObjectName(u"channel3ProtocolLabel")

        self.verticalLayout_12.addWidget(self.channel3ProtocolLabel)


        self.horizontalLayout_6.addWidget(self.channel3LabelFrame)

        self.channel3GraphicsView = QGraphicsView(self.channel3Frame)
        self.channel3GraphicsView.setObjectName(u"channel3GraphicsView")
        self.channel3GraphicsView.setFrameShadow(QFrame.Raised)
        self.channel3GraphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.channel3GraphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_6.addWidget(self.channel3GraphicsView)


        self.verticalLayout_17.addWidget(self.channel3Frame)

        self.channel4Frame = QFrame(self.scrollAreaWidgetContents)
        self.channel4Frame.setObjectName(u"channel4Frame")
        sizePolicy.setHeightForWidth(self.channel4Frame.sizePolicy().hasHeightForWidth())
        self.channel4Frame.setSizePolicy(sizePolicy)
        self.channel4Frame.setMaximumSize(QSize(16777215, 75))
        self.channel4Frame.setFrameShape(QFrame.StyledPanel)
        self.channel4Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.channel4Frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.channel4LabelFrame = QFrame(self.channel4Frame)
        self.channel4LabelFrame.setObjectName(u"channel4LabelFrame")
        sizePolicy2.setHeightForWidth(self.channel4LabelFrame.sizePolicy().hasHeightForWidth())
        self.channel4LabelFrame.setSizePolicy(sizePolicy2)
        self.channel4LabelFrame.setFrameShape(QFrame.StyledPanel)
        self.channel4LabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.channel4LabelFrame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.channel4IDLabel = QLabel(self.channel4LabelFrame)
        self.channel4IDLabel.setObjectName(u"channel4IDLabel")
        self.channel4IDLabel.setMinimumSize(QSize(62, 0))
        self.channel4IDLabel.setMaximumSize(QSize(62, 16777215))

        self.verticalLayout_13.addWidget(self.channel4IDLabel)

        self.channel4ProtocolLabel = QLabel(self.channel4LabelFrame)
        self.channel4ProtocolLabel.setObjectName(u"channel4ProtocolLabel")

        self.verticalLayout_13.addWidget(self.channel4ProtocolLabel)


        self.horizontalLayout_7.addWidget(self.channel4LabelFrame)

        self.channel4GraphicsView = QGraphicsView(self.channel4Frame)
        self.channel4GraphicsView.setObjectName(u"channel4GraphicsView")
        self.channel4GraphicsView.setFrameShadow(QFrame.Raised)
        self.channel4GraphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.channel4GraphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_7.addWidget(self.channel4GraphicsView)


        self.verticalLayout_17.addWidget(self.channel4Frame)

        self.channel5Frame = QFrame(self.scrollAreaWidgetContents)
        self.channel5Frame.setObjectName(u"channel5Frame")
        sizePolicy.setHeightForWidth(self.channel5Frame.sizePolicy().hasHeightForWidth())
        self.channel5Frame.setSizePolicy(sizePolicy)
        self.channel5Frame.setMaximumSize(QSize(16777215, 75))
        self.channel5Frame.setFrameShape(QFrame.StyledPanel)
        self.channel5Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.channel5Frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.channel5LabelFrame = QFrame(self.channel5Frame)
        self.channel5LabelFrame.setObjectName(u"channel5LabelFrame")
        sizePolicy2.setHeightForWidth(self.channel5LabelFrame.sizePolicy().hasHeightForWidth())
        self.channel5LabelFrame.setSizePolicy(sizePolicy2)
        self.channel5LabelFrame.setFrameShape(QFrame.StyledPanel)
        self.channel5LabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.channel5LabelFrame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.channel5IDLabel = QLabel(self.channel5LabelFrame)
        self.channel5IDLabel.setObjectName(u"channel5IDLabel")
        self.channel5IDLabel.setMinimumSize(QSize(62, 0))
        self.channel5IDLabel.setMaximumSize(QSize(62, 16777215))

        self.verticalLayout_14.addWidget(self.channel5IDLabel)

        self.channel5ProtocolLabel = QLabel(self.channel5LabelFrame)
        self.channel5ProtocolLabel.setObjectName(u"channel5ProtocolLabel")

        self.verticalLayout_14.addWidget(self.channel5ProtocolLabel)


        self.horizontalLayout_8.addWidget(self.channel5LabelFrame)

        self.channel5GraphicsView = QGraphicsView(self.channel5Frame)
        self.channel5GraphicsView.setObjectName(u"channel5GraphicsView")
        self.channel5GraphicsView.setFrameShadow(QFrame.Raised)
        self.channel5GraphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.channel5GraphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_8.addWidget(self.channel5GraphicsView)


        self.verticalLayout_17.addWidget(self.channel5Frame)

        self.channel6Frame = QFrame(self.scrollAreaWidgetContents)
        self.channel6Frame.setObjectName(u"channel6Frame")
        sizePolicy.setHeightForWidth(self.channel6Frame.sizePolicy().hasHeightForWidth())
        self.channel6Frame.setSizePolicy(sizePolicy)
        self.channel6Frame.setMaximumSize(QSize(16777215, 75))
        self.channel6Frame.setFrameShape(QFrame.StyledPanel)
        self.channel6Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.channel6Frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.channel6LabelFrame = QFrame(self.channel6Frame)
        self.channel6LabelFrame.setObjectName(u"channel6LabelFrame")
        sizePolicy2.setHeightForWidth(self.channel6LabelFrame.sizePolicy().hasHeightForWidth())
        self.channel6LabelFrame.setSizePolicy(sizePolicy2)
        self.channel6LabelFrame.setFrameShape(QFrame.StyledPanel)
        self.channel6LabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.channel6LabelFrame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.channel6IDLabel = QLabel(self.channel6LabelFrame)
        self.channel6IDLabel.setObjectName(u"channel6IDLabel")
        self.channel6IDLabel.setMinimumSize(QSize(62, 0))
        self.channel6IDLabel.setMaximumSize(QSize(62, 16777215))

        self.verticalLayout_15.addWidget(self.channel6IDLabel)

        self.channel6ProtocolLabel = QLabel(self.channel6LabelFrame)
        self.channel6ProtocolLabel.setObjectName(u"channel6ProtocolLabel")

        self.verticalLayout_15.addWidget(self.channel6ProtocolLabel)


        self.horizontalLayout_9.addWidget(self.channel6LabelFrame)

        self.channel6GraphicsView = QGraphicsView(self.channel6Frame)
        self.channel6GraphicsView.setObjectName(u"channel6GraphicsView")
        self.channel6GraphicsView.setFrameShadow(QFrame.Raised)
        self.channel6GraphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.channel6GraphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_9.addWidget(self.channel6GraphicsView)


        self.verticalLayout_17.addWidget(self.channel6Frame)

        self.channel7Frame = QFrame(self.scrollAreaWidgetContents)
        self.channel7Frame.setObjectName(u"channel7Frame")
        sizePolicy.setHeightForWidth(self.channel7Frame.sizePolicy().hasHeightForWidth())
        self.channel7Frame.setSizePolicy(sizePolicy)
        self.channel7Frame.setMaximumSize(QSize(16777215, 75))
        self.channel7Frame.setFrameShape(QFrame.StyledPanel)
        self.channel7Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.channel7Frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.channel7LabelFrame = QFrame(self.channel7Frame)
        self.channel7LabelFrame.setObjectName(u"channel7LabelFrame")
        sizePolicy2.setHeightForWidth(self.channel7LabelFrame.sizePolicy().hasHeightForWidth())
        self.channel7LabelFrame.setSizePolicy(sizePolicy2)
        self.channel7LabelFrame.setFrameShape(QFrame.StyledPanel)
        self.channel7LabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.channel7LabelFrame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.channel7IDLabel = QLabel(self.channel7LabelFrame)
        self.channel7IDLabel.setObjectName(u"channel7IDLabel")
        self.channel7IDLabel.setMinimumSize(QSize(62, 0))
        self.channel7IDLabel.setMaximumSize(QSize(62, 16777215))

        self.verticalLayout_16.addWidget(self.channel7IDLabel)

        self.channel7ProtocolLabel = QLabel(self.channel7LabelFrame)
        self.channel7ProtocolLabel.setObjectName(u"channel7ProtocolLabel")

        self.verticalLayout_16.addWidget(self.channel7ProtocolLabel)


        self.horizontalLayout_10.addWidget(self.channel7LabelFrame)

        self.channel7GraphicsView = QGraphicsView(self.channel7Frame)
        self.channel7GraphicsView.setObjectName(u"channel7GraphicsView")
        self.channel7GraphicsView.setFrameShadow(QFrame.Raised)
        self.channel7GraphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.channel7GraphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_10.addWidget(self.channel7GraphicsView)


        self.verticalLayout_17.addWidget(self.channel7Frame)

        self.channel8Frame = QFrame(self.scrollAreaWidgetContents)
        self.channel8Frame.setObjectName(u"channel8Frame")
        sizePolicy.setHeightForWidth(self.channel8Frame.sizePolicy().hasHeightForWidth())
        self.channel8Frame.setSizePolicy(sizePolicy)
        self.channel8Frame.setMaximumSize(QSize(16777215, 75))
        self.channel8Frame.setFrameShape(QFrame.StyledPanel)
        self.channel8Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.channel8Frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.channel8LabelFrame = QFrame(self.channel8Frame)
        self.channel8LabelFrame.setObjectName(u"channel8LabelFrame")
        sizePolicy2.setHeightForWidth(self.channel8LabelFrame.sizePolicy().hasHeightForWidth())
        self.channel8LabelFrame.setSizePolicy(sizePolicy2)
        self.channel8LabelFrame.setFrameShape(QFrame.StyledPanel)
        self.channel8LabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.channel8LabelFrame)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.channel8IDLabel = QLabel(self.channel8LabelFrame)
        self.channel8IDLabel.setObjectName(u"channel8IDLabel")
        self.channel8IDLabel.setMinimumSize(QSize(62, 0))
        self.channel8IDLabel.setMaximumSize(QSize(62, 16777215))

        self.verticalLayout_18.addWidget(self.channel8IDLabel)

        self.channel8ProtocolLabel = QLabel(self.channel8LabelFrame)
        self.channel8ProtocolLabel.setObjectName(u"channel8ProtocolLabel")

        self.verticalLayout_18.addWidget(self.channel8ProtocolLabel)


        self.horizontalLayout_11.addWidget(self.channel8LabelFrame)

        self.channel8GraphicsView = QGraphicsView(self.channel8Frame)
        self.channel8GraphicsView.setObjectName(u"channel8GraphicsView")
        self.channel8GraphicsView.setFrameShadow(QFrame.Raised)
        self.channel8GraphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.channel8GraphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_11.addWidget(self.channel8GraphicsView)


        self.verticalLayout_17.addWidget(self.channel8Frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer)

        self.logicAnalyzersScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_19.addWidget(self.logicAnalyzersScrollArea)

        self.channelHorizontalScrollBar = QScrollBar(self.mainFrame)
        self.channelHorizontalScrollBar.setObjectName(u"channelHorizontalScrollBar")
        self.channelHorizontalScrollBar.setStyleSheet(u"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"	background:#31363F;\n"
"}")
        self.channelHorizontalScrollBar.setMaximum(1999)
        self.channelHorizontalScrollBar.setOrientation(Qt.Horizontal)

        self.verticalLayout_19.addWidget(self.channelHorizontalScrollBar)

        self.footerMainFrame = QFrame(self.mainFrame)
        self.footerMainFrame.setObjectName(u"footerMainFrame")
        self.footerMainFrame.setMinimumSize(QSize(0, 25))
        self.footerMainFrame.setFrameShape(QFrame.StyledPanel)
        self.footerMainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.footerMainFrame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 5, 0, 0)
        self.connectionStatusLabel = QLabel(self.footerMainFrame)
        self.connectionStatusLabel.setObjectName(u"connectionStatusLabel")
        font1 = QFont()
        font1.setFamilies([u"consolas"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.connectionStatusLabel.setFont(font1)
        self.connectionStatusLabel.setStyleSheet(u"*\n"
"{\n"
"background-color: #cd0f0f;\n"
"font-family: consolas;\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_12.addWidget(self.connectionStatusLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.cursorInfoLabel = QLabel(self.footerMainFrame)
        self.cursorInfoLabel.setObjectName(u"cursorInfoLabel")
        self.cursorInfoLabel.setStyleSheet(u"*\n"
"{\n"
"font-family: consolas;\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_12.addWidget(self.cursorInfoLabel)

        self.samplingProgressBar = QProgressBar(self.footerMainFrame)
        self.samplingProgressBar.setObjectName(u"samplingProgressBar")
        sizePolicy1.setHeightForWidth(self.samplingProgressBar.sizePolicy().hasHeightForWidth())
        self.samplingProgressBar.setSizePolicy(sizePolicy1)
        self.samplingProgressBar.setMinimumSize(QSize(300, 0))
        self.samplingProgressBar.setMaximumSize(QSize(300, 16777215))
        self.samplingProgressBar.setLayoutDirection(Qt.RightToLeft)
        self.samplingProgressBar.setValue(0)
        self.samplingProgressBar.setInvertedAppearance(True)

        self.horizontalLayout_12.addWidget(self.samplingProgressBar)


        self.verticalLayout_19.addWidget(self.footerMainFrame)


        self.horizontalLayout.addWidget(self.mainFrame)

        self.slideFrameContainer = QFrame(self.centralWidget)
        self.slideFrameContainer.setObjectName(u"slideFrameContainer")
        self.slideFrameContainer.setMaximumSize(QSize(200, 16777215))
        self.slideFrameContainer.setStyleSheet(u"")
        self.slideFrameContainer.setFrameShape(QFrame.StyledPanel)
        self.slideFrameContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.slideFrameContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.slideTabWidget = QTabWidget(self.slideFrameContainer)
        self.slideTabWidget.setObjectName(u"slideTabWidget")
        self.slideTabWidget.setStyleSheet(u"QTabBar::tab {\n"
"  	background: #222831;\n"
"	border: 5px solid #222831;\n"
"} \n"
"QTabBar::tab:selected { \n"
"  background: #31363F;\n"
"	border: 5px solid #31363F;\n"
"}\n"
"QTabWidget#slideTabWidget::pane\n"
"{\n"
"	border: none;\n"
"}\n"
"")
        self.samplingConfigTab = QWidget()
        self.samplingConfigTab.setObjectName(u"samplingConfigTab")
        self.samplingConfigTab.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.samplingConfigTab)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.samplingFrame = QFrame(self.samplingConfigTab)
        self.samplingFrame.setObjectName(u"samplingFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.samplingFrame.sizePolicy().hasHeightForWidth())
        self.samplingFrame.setSizePolicy(sizePolicy4)
        self.samplingFrame.setStyleSheet(u"QFrame#samplingChannelsFrame,\n"
"QFrame#samplingDepthFrame,\n"
"QFrame#samplingFrequencyFrame,\n"
"QFrame#samplingModeFrame,\n"
"QFrame#estimatedSamplingTimeFrame,\n"
"QFrame#triggerChannelFrame,\n"
"QFrame#triggerTimeoutFrame,\n"
"QFrame#voltageThresholdFrame\n"
"{\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius: 7px;\n"
"padding:5px;\n"
"padding-bottom:8px\n"
"}\n"
"")
        self.samplingFrame.setFrameShape(QFrame.StyledPanel)
        self.samplingFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.samplingFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.samplingModeFrame = QFrame(self.samplingFrame)
        self.samplingModeFrame.setObjectName(u"samplingModeFrame")
        self.samplingModeFrame.setStyleSheet(u"QFrame#samplingModeFrameContainer{\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"}")
        self.samplingModeFrame.setFrameShape(QFrame.StyledPanel)
        self.samplingModeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.samplingModeFrame)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.samplingTitleLabel = QLabel(self.samplingModeFrame)
        self.samplingTitleLabel.setObjectName(u"samplingTitleLabel")
        self.samplingTitleLabel.setFont(font)
        self.samplingTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.samplingTitleLabel)

        self.samplingModeButtonsFrame = QFrame(self.samplingModeFrame)
        self.samplingModeButtonsFrame.setObjectName(u"samplingModeButtonsFrame")
        self.samplingModeButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.samplingModeButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.samplingModeButtonsFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.digitalModePushButton = QPushButton(self.samplingModeButtonsFrame)
        self.digitalModePushButton.setObjectName(u"digitalModePushButton")
        self.digitalModePushButton.setMinimumSize(QSize(0, 25))
        self.digitalModePushButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.digitalModePushButton)

        self.analogModePushButton = QPushButton(self.samplingModeButtonsFrame)
        self.analogModePushButton.setObjectName(u"analogModePushButton")
        self.analogModePushButton.setMinimumSize(QSize(0, 25))
        self.analogModePushButton.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/ButtonIcons/ico/sine wave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.analogModePushButton.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.analogModePushButton)


        self.verticalLayout_8.addWidget(self.samplingModeButtonsFrame)


        self.verticalLayout_2.addWidget(self.samplingModeFrame)

        self.samplingFrequencyFrame = QFrame(self.samplingFrame)
        self.samplingFrequencyFrame.setObjectName(u"samplingFrequencyFrame")
        self.samplingFrequencyFrame.setFrameShape(QFrame.StyledPanel)
        self.samplingFrequencyFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.samplingFrequencyFrame)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.samplingFrequencyLabel = QLabel(self.samplingFrequencyFrame)
        self.samplingFrequencyLabel.setObjectName(u"samplingFrequencyLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.samplingFrequencyLabel.sizePolicy().hasHeightForWidth())
        self.samplingFrequencyLabel.setSizePolicy(sizePolicy5)
        self.samplingFrequencyLabel.setFont(font)
        self.samplingFrequencyLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.samplingFrequencyLabel)

        self.samplingFrequencyComboBox = QComboBox(self.samplingFrequencyFrame)
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.addItem("")
        self.samplingFrequencyComboBox.setObjectName(u"samplingFrequencyComboBox")
        self.samplingFrequencyComboBox.setMinimumSize(QSize(0, 25))
        self.samplingFrequencyComboBox.setFont(font)

        self.verticalLayout_5.addWidget(self.samplingFrequencyComboBox)


        self.verticalLayout_2.addWidget(self.samplingFrequencyFrame)

        self.samplingDepthFrame = QFrame(self.samplingFrame)
        self.samplingDepthFrame.setObjectName(u"samplingDepthFrame")
        self.samplingDepthFrame.setFrameShape(QFrame.StyledPanel)
        self.samplingDepthFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.samplingDepthFrame)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.samplingDepthTilteLabel = QLabel(self.samplingDepthFrame)
        self.samplingDepthTilteLabel.setObjectName(u"samplingDepthTilteLabel")
        sizePolicy5.setHeightForWidth(self.samplingDepthTilteLabel.sizePolicy().hasHeightForWidth())
        self.samplingDepthTilteLabel.setSizePolicy(sizePolicy5)
        self.samplingDepthTilteLabel.setFont(font)
        self.samplingDepthTilteLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.samplingDepthTilteLabel)

        self.samplingDepthHorizontalSlider = QSlider(self.samplingDepthFrame)
        self.samplingDepthHorizontalSlider.setObjectName(u"samplingDepthHorizontalSlider")
        self.samplingDepthHorizontalSlider.setMinimum(1)
        self.samplingDepthHorizontalSlider.setMaximum(192)
        self.samplingDepthHorizontalSlider.setValue(20)
        self.samplingDepthHorizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.samplingDepthHorizontalSlider)

        self.samplingDepthValueLabel = QLabel(self.samplingDepthFrame)
        self.samplingDepthValueLabel.setObjectName(u"samplingDepthValueLabel")
        sizePolicy.setHeightForWidth(self.samplingDepthValueLabel.sizePolicy().hasHeightForWidth())
        self.samplingDepthValueLabel.setSizePolicy(sizePolicy)
        self.samplingDepthValueLabel.setFont(font)
        self.samplingDepthValueLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.samplingDepthValueLabel)


        self.verticalLayout_2.addWidget(self.samplingDepthFrame)

        self.samplingChannelsFrame = QFrame(self.samplingFrame)
        self.samplingChannelsFrame.setObjectName(u"samplingChannelsFrame")
        self.samplingChannelsFrame.setFrameShape(QFrame.StyledPanel)
        self.samplingChannelsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.samplingChannelsFrame)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.samplingChannelsLabel = QLabel(self.samplingChannelsFrame)
        self.samplingChannelsLabel.setObjectName(u"samplingChannelsLabel")
        sizePolicy5.setHeightForWidth(self.samplingChannelsLabel.sizePolicy().hasHeightForWidth())
        self.samplingChannelsLabel.setSizePolicy(sizePolicy5)
        self.samplingChannelsLabel.setFont(font)
        self.samplingChannelsLabel.setAlignment(Qt.AlignCenter)
        self.samplingChannelsLabel.setWordWrap(True)

        self.horizontalLayout_15.addWidget(self.samplingChannelsLabel)

        self.samplingChannelsComboBox = QComboBox(self.samplingChannelsFrame)
        self.samplingChannelsComboBox.addItem("")
        self.samplingChannelsComboBox.addItem("")
        self.samplingChannelsComboBox.addItem("")
        self.samplingChannelsComboBox.addItem("")
        self.samplingChannelsComboBox.setObjectName(u"samplingChannelsComboBox")
        self.samplingChannelsComboBox.setMinimumSize(QSize(60, 25))
        self.samplingChannelsComboBox.setFont(font)

        self.horizontalLayout_15.addWidget(self.samplingChannelsComboBox)


        self.verticalLayout_2.addWidget(self.samplingChannelsFrame)

        self.estimatedSamplingTimeFrame = QFrame(self.samplingFrame)
        self.estimatedSamplingTimeFrame.setObjectName(u"estimatedSamplingTimeFrame")
        self.estimatedSamplingTimeFrame.setFrameShape(QFrame.StyledPanel)
        self.estimatedSamplingTimeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.estimatedSamplingTimeFrame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.estimatedSamplingTimeTitleLabel = QLabel(self.estimatedSamplingTimeFrame)
        self.estimatedSamplingTimeTitleLabel.setObjectName(u"estimatedSamplingTimeTitleLabel")
        self.estimatedSamplingTimeTitleLabel.setFont(font)
        self.estimatedSamplingTimeTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.estimatedSamplingTimeTitleLabel)

        self.estimatedSamplingTimeValueLabel = QLabel(self.estimatedSamplingTimeFrame)
        self.estimatedSamplingTimeValueLabel.setObjectName(u"estimatedSamplingTimeValueLabel")
        self.estimatedSamplingTimeValueLabel.setFont(font)
        self.estimatedSamplingTimeValueLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.estimatedSamplingTimeValueLabel)


        self.verticalLayout_2.addWidget(self.estimatedSamplingTimeFrame)

        self.triggerChannelFrame = QFrame(self.samplingFrame)
        self.triggerChannelFrame.setObjectName(u"triggerChannelFrame")
        self.triggerChannelFrame.setFrameShape(QFrame.StyledPanel)
        self.triggerChannelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.triggerChannelFrame)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.triggerChannelTitleLabel = QLabel(self.triggerChannelFrame)
        self.triggerChannelTitleLabel.setObjectName(u"triggerChannelTitleLabel")
        sizePolicy5.setHeightForWidth(self.triggerChannelTitleLabel.sizePolicy().hasHeightForWidth())
        self.triggerChannelTitleLabel.setSizePolicy(sizePolicy5)
        self.triggerChannelTitleLabel.setFont(font)
        self.triggerChannelTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.triggerChannelTitleLabel)

        self.triggerChannelButtonsFrame = QFrame(self.triggerChannelFrame)
        self.triggerChannelButtonsFrame.setObjectName(u"triggerChannelButtonsFrame")
        self.triggerChannelButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.triggerChannelButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.triggerChannelButtonsFrame)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.triggerChannelComboBox = QComboBox(self.triggerChannelButtonsFrame)
        self.triggerChannelComboBox.addItem("")
        self.triggerChannelComboBox.addItem("")
        self.triggerChannelComboBox.addItem("")
        self.triggerChannelComboBox.addItem("")
        self.triggerChannelComboBox.addItem("")
        self.triggerChannelComboBox.addItem("")
        self.triggerChannelComboBox.addItem("")
        self.triggerChannelComboBox.addItem("")
        self.triggerChannelComboBox.setObjectName(u"triggerChannelComboBox")
        sizePolicy1.setHeightForWidth(self.triggerChannelComboBox.sizePolicy().hasHeightForWidth())
        self.triggerChannelComboBox.setSizePolicy(sizePolicy1)
        self.triggerChannelComboBox.setMinimumSize(QSize(25, 25))
        self.triggerChannelComboBox.setMaximumSize(QSize(50, 16777215))
        self.triggerChannelComboBox.setFont(font)

        self.horizontalLayout_16.addWidget(self.triggerChannelComboBox)

        self.triggerModeComboBox = QComboBox(self.triggerChannelButtonsFrame)
        icon8 = QIcon()
        icon8.addFile(u":/ButtonIcons/ico/UNTRIGGERED.png", QSize(), QIcon.Normal, QIcon.Off)
        self.triggerModeComboBox.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/ButtonIcons/ico/RISING EDGE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.triggerModeComboBox.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addFile(u":/ButtonIcons/ico/FALLING EDGE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.triggerModeComboBox.addItem(icon10, "")
        icon11 = QIcon()
        icon11.addFile(u":/ButtonIcons/ico/LOW LEVEL.png", QSize(), QIcon.Normal, QIcon.Off)
        self.triggerModeComboBox.addItem(icon11, "")
        icon12 = QIcon()
        icon12.addFile(u":/ButtonIcons/ico/HIGH LEVEL.png", QSize(), QIcon.Normal, QIcon.Off)
        self.triggerModeComboBox.addItem(icon12, "")
        self.triggerModeComboBox.setObjectName(u"triggerModeComboBox")
        self.triggerModeComboBox.setMinimumSize(QSize(0, 25))
        self.triggerModeComboBox.setFont(font)

        self.horizontalLayout_16.addWidget(self.triggerModeComboBox)


        self.verticalLayout_20.addWidget(self.triggerChannelButtonsFrame)


        self.verticalLayout_2.addWidget(self.triggerChannelFrame)

        self.triggerTimeoutFrame = QFrame(self.samplingFrame)
        self.triggerTimeoutFrame.setObjectName(u"triggerTimeoutFrame")
        self.triggerTimeoutFrame.setFrameShape(QFrame.StyledPanel)
        self.triggerTimeoutFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.triggerTimeoutFrame)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.triggerTimeoutLabel = QLabel(self.triggerTimeoutFrame)
        self.triggerTimeoutLabel.setObjectName(u"triggerTimeoutLabel")
        self.triggerTimeoutLabel.setFont(font)
        self.triggerTimeoutLabel.setAlignment(Qt.AlignCenter)
        self.triggerTimeoutLabel.setWordWrap(True)

        self.horizontalLayout_17.addWidget(self.triggerTimeoutLabel)

        self.triggerTimeoutDoubleSpinBox = QDoubleSpinBox(self.triggerTimeoutFrame)
        self.triggerTimeoutDoubleSpinBox.setObjectName(u"triggerTimeoutDoubleSpinBox")
        self.triggerTimeoutDoubleSpinBox.setMinimumSize(QSize(80, 20))
        self.triggerTimeoutDoubleSpinBox.setMaximumSize(QSize(80, 16777215))
        self.triggerTimeoutDoubleSpinBox.setFont(font)
        self.triggerTimeoutDoubleSpinBox.setMinimum(0.300000000000000)
        self.triggerTimeoutDoubleSpinBox.setSingleStep(0.100000000000000)
        self.triggerTimeoutDoubleSpinBox.setValue(0.300000000000000)

        self.horizontalLayout_17.addWidget(self.triggerTimeoutDoubleSpinBox)


        self.verticalLayout_2.addWidget(self.triggerTimeoutFrame)

        self.voltageThresholdFrame = QFrame(self.samplingFrame)
        self.voltageThresholdFrame.setObjectName(u"voltageThresholdFrame")
        self.voltageThresholdFrame.setFrameShape(QFrame.StyledPanel)
        self.voltageThresholdFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.voltageThresholdFrame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.voltageThresholdLabel = QLabel(self.voltageThresholdFrame)
        self.voltageThresholdLabel.setObjectName(u"voltageThresholdLabel")
        self.voltageThresholdLabel.setFont(font)
        self.voltageThresholdLabel.setAcceptDrops(False)
        self.voltageThresholdLabel.setAlignment(Qt.AlignCenter)
        self.voltageThresholdLabel.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.voltageThresholdLabel)

        self.voltageThresholdDoubleSpinBox = QDoubleSpinBox(self.voltageThresholdFrame)
        self.voltageThresholdDoubleSpinBox.setObjectName(u"voltageThresholdDoubleSpinBox")
        self.voltageThresholdDoubleSpinBox.setMinimumSize(QSize(80, 20))
        self.voltageThresholdDoubleSpinBox.setMaximumSize(QSize(80, 16777215))
        self.voltageThresholdDoubleSpinBox.setFont(font)
        self.voltageThresholdDoubleSpinBox.setMaximum(3.300000000000000)
        self.voltageThresholdDoubleSpinBox.setSingleStep(0.010000000000000)
        self.voltageThresholdDoubleSpinBox.setValue(2.600000000000000)

        self.horizontalLayout_2.addWidget(self.voltageThresholdDoubleSpinBox)


        self.verticalLayout_2.addWidget(self.voltageThresholdFrame)

        self.slideFrameVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.slideFrameVerticalSpacer)


        self.verticalLayout_9.addWidget(self.samplingFrame)

        self.slideTabWidget.addTab(self.samplingConfigTab, "")
        self.analysisTab = QWidget()
        self.analysisTab.setObjectName(u"analysisTab")
        self.verticalLayout_23 = QVBoxLayout(self.analysisTab)
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.analysisFrame = QFrame(self.analysisTab)
        self.analysisFrame.setObjectName(u"analysisFrame")
        self.analysisFrame.setStyleSheet(u"QFrame#triggerAnalysisFrame,\n"
"QFrame#analogYLimEditFrame, \n"
"QFrame#fixedMeasurementFrame\n"
"{\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius: 7px;\n"
"padding:5px;\n"
"padding-bottom:8px\n"
"}")
        self.analysisFrame.setFrameShape(QFrame.StyledPanel)
        self.analysisFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.analysisFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.fixedMeasurementFrame = QFrame(self.analysisFrame)
        self.fixedMeasurementFrame.setObjectName(u"fixedMeasurementFrame")
        self.fixedMeasurementFrame.setFrameShape(QFrame.StyledPanel)
        self.fixedMeasurementFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.fixedMeasurementFrame)
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.fixedMeasurementTitleLabel = QLabel(self.fixedMeasurementFrame)
        self.fixedMeasurementTitleLabel.setObjectName(u"fixedMeasurementTitleLabel")
        sizePolicy5.setHeightForWidth(self.fixedMeasurementTitleLabel.sizePolicy().hasHeightForWidth())
        self.fixedMeasurementTitleLabel.setSizePolicy(sizePolicy5)
        self.fixedMeasurementTitleLabel.setFont(font)
        self.fixedMeasurementTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.fixedMeasurementTitleLabel)

        self.fixedMeasurementTime1Label = QLabel(self.fixedMeasurementFrame)
        self.fixedMeasurementTime1Label.setObjectName(u"fixedMeasurementTime1Label")
        self.fixedMeasurementTime1Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.fixedMeasurementTime1Label)

        self.fixedMeasurementTime2Label = QLabel(self.fixedMeasurementFrame)
        self.fixedMeasurementTime2Label.setObjectName(u"fixedMeasurementTime2Label")
        self.fixedMeasurementTime2Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.fixedMeasurementTime2Label)

        self.fixedMeasurementPeriodLabel = QLabel(self.fixedMeasurementFrame)
        self.fixedMeasurementPeriodLabel.setObjectName(u"fixedMeasurementPeriodLabel")
        self.fixedMeasurementPeriodLabel.setAlignment(Qt.AlignCenter)
        self.fixedMeasurementPeriodLabel.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.fixedMeasurementPeriodLabel)

        self.fixedMeasurementFrequencyLabel = QLabel(self.fixedMeasurementFrame)
        self.fixedMeasurementFrequencyLabel.setObjectName(u"fixedMeasurementFrequencyLabel")
        self.fixedMeasurementFrequencyLabel.setAlignment(Qt.AlignCenter)
        self.fixedMeasurementFrequencyLabel.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.fixedMeasurementFrequencyLabel)

        self.fixedMeasurementSamplesLabel = QLabel(self.fixedMeasurementFrame)
        self.fixedMeasurementSamplesLabel.setObjectName(u"fixedMeasurementSamplesLabel")
        self.fixedMeasurementSamplesLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.fixedMeasurementSamplesLabel)


        self.verticalLayout_4.addWidget(self.fixedMeasurementFrame)

        self.triggerAnalysisFrame = QFrame(self.analysisFrame)
        self.triggerAnalysisFrame.setObjectName(u"triggerAnalysisFrame")
        self.triggerAnalysisFrame.setFrameShape(QFrame.StyledPanel)
        self.triggerAnalysisFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.triggerAnalysisFrame)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.triggerAnalysisTitleLabel = QLabel(self.triggerAnalysisFrame)
        self.triggerAnalysisTitleLabel.setObjectName(u"triggerAnalysisTitleLabel")
        sizePolicy5.setHeightForWidth(self.triggerAnalysisTitleLabel.sizePolicy().hasHeightForWidth())
        self.triggerAnalysisTitleLabel.setSizePolicy(sizePolicy5)
        self.triggerAnalysisTitleLabel.setFont(font)
        self.triggerAnalysisTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.triggerAnalysisTitleLabel)

        self.triggerAnalysisSelectorFrame = QFrame(self.triggerAnalysisFrame)
        self.triggerAnalysisSelectorFrame.setObjectName(u"triggerAnalysisSelectorFrame")
        self.triggerAnalysisSelectorFrame.setFrameShape(QFrame.StyledPanel)
        self.triggerAnalysisSelectorFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.triggerAnalysisSelectorFrame)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.triggerAnalysisChannelComboBox = QComboBox(self.triggerAnalysisSelectorFrame)
        self.triggerAnalysisChannelComboBox.addItem("")
        self.triggerAnalysisChannelComboBox.addItem("")
        self.triggerAnalysisChannelComboBox.addItem("")
        self.triggerAnalysisChannelComboBox.addItem("")
        self.triggerAnalysisChannelComboBox.addItem("")
        self.triggerAnalysisChannelComboBox.addItem("")
        self.triggerAnalysisChannelComboBox.addItem("")
        self.triggerAnalysisChannelComboBox.addItem("")
        self.triggerAnalysisChannelComboBox.setObjectName(u"triggerAnalysisChannelComboBox")
        sizePolicy1.setHeightForWidth(self.triggerAnalysisChannelComboBox.sizePolicy().hasHeightForWidth())
        self.triggerAnalysisChannelComboBox.setSizePolicy(sizePolicy1)
        self.triggerAnalysisChannelComboBox.setMinimumSize(QSize(30, 25))
        self.triggerAnalysisChannelComboBox.setMaximumSize(QSize(50, 16777215))
        self.triggerAnalysisChannelComboBox.setFont(font)

        self.horizontalLayout_19.addWidget(self.triggerAnalysisChannelComboBox)

        self.triggerAnalysisModeComboBox = QComboBox(self.triggerAnalysisSelectorFrame)
        self.triggerAnalysisModeComboBox.addItem(icon9, "")
        self.triggerAnalysisModeComboBox.addItem(icon10, "")
        self.triggerAnalysisModeComboBox.addItem(icon11, "")
        self.triggerAnalysisModeComboBox.addItem(icon12, "")
        self.triggerAnalysisModeComboBox.setObjectName(u"triggerAnalysisModeComboBox")
        self.triggerAnalysisModeComboBox.setMinimumSize(QSize(0, 25))
        self.triggerAnalysisModeComboBox.setFont(font)

        self.horizontalLayout_19.addWidget(self.triggerAnalysisModeComboBox)


        self.verticalLayout_21.addWidget(self.triggerAnalysisSelectorFrame)

        self.triggerAnalysisButtonsFrame = QFrame(self.triggerAnalysisFrame)
        self.triggerAnalysisButtonsFrame.setObjectName(u"triggerAnalysisButtonsFrame")
        self.triggerAnalysisButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.triggerAnalysisButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.triggerAnalysisButtonsFrame)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.triggerAnalysisGoLeftButton = QPushButton(self.triggerAnalysisButtonsFrame)
        self.triggerAnalysisGoLeftButton.setObjectName(u"triggerAnalysisGoLeftButton")
        self.triggerAnalysisGoLeftButton.setMinimumSize(QSize(0, 25))
        self.triggerAnalysisGoLeftButton.setMaximumSize(QSize(16777215, 25))
        icon13 = QIcon()
        icon13.addFile(u":/ButtonIcons/ico/ArrowLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.triggerAnalysisGoLeftButton.setIcon(icon13)
        self.triggerAnalysisGoLeftButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_20.addWidget(self.triggerAnalysisGoLeftButton)

        self.triggerAnalysisGoRightButton = QPushButton(self.triggerAnalysisButtonsFrame)
        self.triggerAnalysisGoRightButton.setObjectName(u"triggerAnalysisGoRightButton")
        self.triggerAnalysisGoRightButton.setMinimumSize(QSize(0, 25))
        self.triggerAnalysisGoRightButton.setMaximumSize(QSize(16777215, 25))
        icon14 = QIcon()
        icon14.addFile(u":/ButtonIcons/ico/ArrowRight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.triggerAnalysisGoRightButton.setIcon(icon14)
        self.triggerAnalysisGoRightButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_20.addWidget(self.triggerAnalysisGoRightButton)


        self.verticalLayout_21.addWidget(self.triggerAnalysisButtonsFrame)

        self.triggerAnalysisReferenceLabel = QLabel(self.triggerAnalysisFrame)
        self.triggerAnalysisReferenceLabel.setObjectName(u"triggerAnalysisReferenceLabel")

        self.verticalLayout_21.addWidget(self.triggerAnalysisReferenceLabel)

        self.visorCenterRadioButton = QRadioButton(self.triggerAnalysisFrame)
        self.visorCenterRadioButton.setObjectName(u"visorCenterRadioButton")

        self.verticalLayout_21.addWidget(self.visorCenterRadioButton)

        self.lastCursorRadioButton = QRadioButton(self.triggerAnalysisFrame)
        self.lastCursorRadioButton.setObjectName(u"lastCursorRadioButton")

        self.verticalLayout_21.addWidget(self.lastCursorRadioButton)


        self.verticalLayout_4.addWidget(self.triggerAnalysisFrame)

        self.analogYLimEditFrame = QFrame(self.analysisFrame)
        self.analogYLimEditFrame.setObjectName(u"analogYLimEditFrame")
        self.analogYLimEditFrame.setFrameShape(QFrame.StyledPanel)
        self.analogYLimEditFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.analogYLimEditFrame)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.analogYLimEditTitleLabel = QLabel(self.analogYLimEditFrame)
        self.analogYLimEditTitleLabel.setObjectName(u"analogYLimEditTitleLabel")
        sizePolicy5.setHeightForWidth(self.analogYLimEditTitleLabel.sizePolicy().hasHeightForWidth())
        self.analogYLimEditTitleLabel.setSizePolicy(sizePolicy5)
        self.analogYLimEditTitleLabel.setFont(font)
        self.analogYLimEditTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.analogYLimEditTitleLabel)

        self.topYLimFrame = QFrame(self.analogYLimEditFrame)
        self.topYLimFrame.setObjectName(u"topYLimFrame")
        self.topYLimFrame.setFrameShape(QFrame.StyledPanel)
        self.topYLimFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.topYLimFrame)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.topYLimLabel = QLabel(self.topYLimFrame)
        self.topYLimLabel.setObjectName(u"topYLimLabel")
        self.topYLimLabel.setAlignment(Qt.AlignCenter)
        self.topYLimLabel.setWordWrap(True)

        self.horizontalLayout_23.addWidget(self.topYLimLabel)

        self.topYLimDoubleSpinBox = QDoubleSpinBox(self.topYLimFrame)
        self.topYLimDoubleSpinBox.setObjectName(u"topYLimDoubleSpinBox")
        sizePolicy1.setHeightForWidth(self.topYLimDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.topYLimDoubleSpinBox.setSizePolicy(sizePolicy1)
        self.topYLimDoubleSpinBox.setMinimumSize(QSize(80, 0))
        self.topYLimDoubleSpinBox.setMaximumSize(QSize(80, 16777215))
        self.topYLimDoubleSpinBox.setMinimum(0.010000000000000)
        self.topYLimDoubleSpinBox.setMaximum(5.000000000000000)
        self.topYLimDoubleSpinBox.setSingleStep(0.100000000000000)
        self.topYLimDoubleSpinBox.setValue(5.000000000000000)

        self.horizontalLayout_23.addWidget(self.topYLimDoubleSpinBox)


        self.verticalLayout_22.addWidget(self.topYLimFrame)

        self.botYLimFrame = QFrame(self.analogYLimEditFrame)
        self.botYLimFrame.setObjectName(u"botYLimFrame")
        self.botYLimFrame.setFrameShape(QFrame.StyledPanel)
        self.botYLimFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.botYLimFrame)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.bitYLimLabel = QLabel(self.botYLimFrame)
        self.bitYLimLabel.setObjectName(u"bitYLimLabel")
        self.bitYLimLabel.setAlignment(Qt.AlignCenter)
        self.bitYLimLabel.setWordWrap(True)

        self.horizontalLayout_24.addWidget(self.bitYLimLabel)

        self.botYLimDoubleSpinBox = QDoubleSpinBox(self.botYLimFrame)
        self.botYLimDoubleSpinBox.setObjectName(u"botYLimDoubleSpinBox")
        sizePolicy1.setHeightForWidth(self.botYLimDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.botYLimDoubleSpinBox.setSizePolicy(sizePolicy1)
        self.botYLimDoubleSpinBox.setMinimumSize(QSize(80, 0))
        self.botYLimDoubleSpinBox.setMaximumSize(QSize(80, 16777215))
        self.botYLimDoubleSpinBox.setMinimum(0.000000000000000)
        self.botYLimDoubleSpinBox.setMaximum(4.990000000000000)
        self.botYLimDoubleSpinBox.setSingleStep(0.100000000000000)
        self.botYLimDoubleSpinBox.setValue(0.000000000000000)

        self.horizontalLayout_24.addWidget(self.botYLimDoubleSpinBox)


        self.verticalLayout_22.addWidget(self.botYLimFrame)


        self.verticalLayout_4.addWidget(self.analogYLimEditFrame)

        self.triggerVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.triggerVerticalSpacer)


        self.verticalLayout_23.addWidget(self.analysisFrame)

        self.slideTabWidget.addTab(self.analysisTab, "")
        self.protocolTab = QWidget()
        self.protocolTab.setObjectName(u"protocolTab")
        self.verticalLayout_25 = QVBoxLayout(self.protocolTab)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, -1, 0, -1)
        self.protocolFrame = QFrame(self.protocolTab)
        self.protocolFrame.setObjectName(u"protocolFrame")
        self.protocolFrame.setStyleSheet(u"QFrame#bitInterpretationFrame,\n"
"QFrame#framesListFrame\n"
"{\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius: 7px;\n"
"padding:5px;\n"
"padding-bottom:8px\n"
"}")
        self.protocolFrame.setFrameShape(QFrame.StyledPanel)
        self.protocolFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.protocolFrame)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.bitInterpretationFrame = QFrame(self.protocolFrame)
        self.bitInterpretationFrame.setObjectName(u"bitInterpretationFrame")
        self.bitInterpretationFrame.setFrameShape(QFrame.NoFrame)
        self.bitInterpretationFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.bitInterpretationFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.binaryInterpretationRadioButton = QRadioButton(self.bitInterpretationFrame)
        self.binaryInterpretationRadioButton.setObjectName(u"binaryInterpretationRadioButton")
        self.binaryInterpretationRadioButton.setChecked(True)

        self.gridLayout_2.addWidget(self.binaryInterpretationRadioButton, 1, 0, 1, 1)

        self.interpretationLabel = QLabel(self.bitInterpretationFrame)
        self.interpretationLabel.setObjectName(u"interpretationLabel")
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.interpretationLabel.setFont(font2)
        self.interpretationLabel.setStyleSheet(u"*\n"
"{\n"
"font: 500 10pt \"Consolas\";\n"
"}")
        self.interpretationLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.interpretationLabel, 0, 0, 1, 1)

        self.ASCIIInterpretationRadioButton = QRadioButton(self.bitInterpretationFrame)
        self.ASCIIInterpretationRadioButton.setObjectName(u"ASCIIInterpretationRadioButton")

        self.gridLayout_2.addWidget(self.ASCIIInterpretationRadioButton, 4, 0, 1, 1)

        self.hexadecimalInterpretationRadioButton = QRadioButton(self.bitInterpretationFrame)
        self.hexadecimalInterpretationRadioButton.setObjectName(u"hexadecimalInterpretationRadioButton")

        self.gridLayout_2.addWidget(self.hexadecimalInterpretationRadioButton, 3, 0, 1, 1)

        self.decimalInterpretationRadioButton = QRadioButton(self.bitInterpretationFrame)
        self.decimalInterpretationRadioButton.setObjectName(u"decimalInterpretationRadioButton")

        self.gridLayout_2.addWidget(self.decimalInterpretationRadioButton, 2, 0, 1, 1)


        self.verticalLayout_26.addWidget(self.bitInterpretationFrame)

        self.framesListFrame = QFrame(self.protocolFrame)
        self.framesListFrame.setObjectName(u"framesListFrame")
        self.framesListFrame.setFrameShape(QFrame.NoFrame)
        self.framesListFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.framesListFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.FramesListLabel = QLabel(self.framesListFrame)
        self.FramesListLabel.setObjectName(u"FramesListLabel")
        self.FramesListLabel.setFont(font2)
        self.FramesListLabel.setStyleSheet(u"*\n"
"{\n"
"font: 500 10pt \"Consolas\";\n"
"}")
        self.FramesListLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.FramesListLabel, 0, 0, 1, 1)

        self.decodedFramesTableWidget = QTableWidget(self.framesListFrame)
        self.decodedFramesTableWidget.setObjectName(u"decodedFramesTableWidget")
        self.decodedFramesTableWidget.setStyleSheet(u"QTableView QTableCornerButton::section {\n"
"	border: 2px solid gray;	\n"
"	background-color: rgb(34, 40, 49);\n"
"}\n"
"QTableWidgetItem\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(34, 40, 49);\n"
"}\n"
"QTableWidgetItem::section:checked\n"
"{\n"
"	background-color: rgb(49, 54, 63);\n"
"	border: 4px solid #007ad9;\n"
"}\n"
"QHeaderView::section\n"
"{\n"
"	border: 2px solid gray;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(34, 40, 49);\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	background-color: rgb(49, 54, 63);\n"
"}")
        self.decodedFramesTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.decodedFramesTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.decodedFramesTableWidget.horizontalHeader().setStretchLastSection(False)
        self.decodedFramesTableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.decodedFramesTableWidget, 1, 0, 1, 1)


        self.verticalLayout_26.addWidget(self.framesListFrame)


        self.verticalLayout_25.addWidget(self.protocolFrame)

        self.slideTabWidget.addTab(self.protocolTab, "")

        self.verticalLayout.addWidget(self.slideTabWidget)

        self.slideFrameFooter = QFrame(self.slideFrameContainer)
        self.slideFrameFooter.setObjectName(u"slideFrameFooter")
        sizePolicy.setHeightForWidth(self.slideFrameFooter.sizePolicy().hasHeightForWidth())
        self.slideFrameFooter.setSizePolicy(sizePolicy)
        self.slideFrameFooter.setMinimumSize(QSize(0, 20))
        self.slideFrameFooter.setMaximumSize(QSize(16777215, 20))
        self.slideFrameFooter.setFrameShape(QFrame.StyledPanel)
        self.slideFrameFooter.setFrameShadow(QFrame.Raised)
        self.versionLabel = QLabel(self.slideFrameFooter)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setGeometry(QRect(50, 0, 101, 16))
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.versionLabel.sizePolicy().hasHeightForWidth())
        self.versionLabel.setSizePolicy(sizePolicy6)
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.versionLabel.setFont(font3)
        self.versionLabel.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.slideFrameFooter, 0, Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.slideFrameContainer)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        self.slideTabWidget.setCurrentIndex(0)
        self.samplingFrequencyComboBox.setCurrentIndex(13)
        self.samplingChannelsComboBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Proyecto Final", None))
        self.channelVisualizationLabel.setText(QCoreApplication.translate("MainWindow", u"Canales:", None))
        self.channel1CheckBox.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.channel2CheckBox.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.channel3CheckBox.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.channel4CheckBox.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.channel5CheckBox.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.channel6CheckBox.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.channel7CheckBox.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.channel8CheckBox.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.clearProtocolAnalysisPushButton.setText("")
        self.protocolAnalysisPushButton.setText("")
        self.fixedCursorsPushButton.setText("")
        self.cursorPushButton.setText("")
        self.startSamplingPushButton.setText("")
        self.configSliderPushButton.setText("")
        self.axisLabel.setText(QCoreApplication.translate("MainWindow", u"Tiempo:", None))
        self.channel1IDLabel.setText(QCoreApplication.translate("MainWindow", u"Canal 1", None))
        self.channel1ProtocolLabel.setText(QCoreApplication.translate("MainWindow", u"asd", None))
#if QT_CONFIG(accessibility)
        self.channel1GraphicsView.setAccessibleName(QCoreApplication.translate("MainWindow", u"Canal 1", None))
#endif // QT_CONFIG(accessibility)
        self.channel2IDLabel.setText(QCoreApplication.translate("MainWindow", u"Canal 2", None))
        self.channel2ProtocolLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(accessibility)
        self.channel2GraphicsView.setAccessibleName(QCoreApplication.translate("MainWindow", u"Canal 2", None))
#endif // QT_CONFIG(accessibility)
        self.channel3IDLabel.setText(QCoreApplication.translate("MainWindow", u"Canal 3", None))
        self.channel3ProtocolLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(accessibility)
        self.channel3GraphicsView.setAccessibleName(QCoreApplication.translate("MainWindow", u"Canal 3", None))
#endif // QT_CONFIG(accessibility)
        self.channel4IDLabel.setText(QCoreApplication.translate("MainWindow", u"Canal 4", None))
        self.channel4ProtocolLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(accessibility)
        self.channel4GraphicsView.setAccessibleName(QCoreApplication.translate("MainWindow", u"Canal 4", None))
#endif // QT_CONFIG(accessibility)
        self.channel5IDLabel.setText(QCoreApplication.translate("MainWindow", u"Canal 5", None))
        self.channel5ProtocolLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(accessibility)
        self.channel5GraphicsView.setAccessibleName(QCoreApplication.translate("MainWindow", u"Canal 5", None))
#endif // QT_CONFIG(accessibility)
        self.channel6IDLabel.setText(QCoreApplication.translate("MainWindow", u"Canal 6", None))
        self.channel6ProtocolLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(accessibility)
        self.channel6GraphicsView.setAccessibleName(QCoreApplication.translate("MainWindow", u"Canal 6", None))
#endif // QT_CONFIG(accessibility)
        self.channel7IDLabel.setText(QCoreApplication.translate("MainWindow", u"Canal 7", None))
        self.channel7ProtocolLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(accessibility)
        self.channel7GraphicsView.setAccessibleName(QCoreApplication.translate("MainWindow", u"Canal 7", None))
#endif // QT_CONFIG(accessibility)
        self.channel8IDLabel.setText(QCoreApplication.translate("MainWindow", u"Canal 8", None))
        self.channel8ProtocolLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(accessibility)
        self.channel8GraphicsView.setAccessibleName(QCoreApplication.translate("MainWindow", u"Canal 8", None))
#endif // QT_CONFIG(accessibility)
        self.connectionStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Estado: Desconectado", None))
        self.cursorInfoLabel.setText(QCoreApplication.translate("MainWindow", u"t: [], \u0394t: [], 1/\u0394t: []", None))
#if QT_CONFIG(accessibility)
        self.samplingConfigTab.setAccessibleName(QCoreApplication.translate("MainWindow", u"Muestreo", None))
#endif // QT_CONFIG(accessibility)
        self.samplingTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Modo de Muestreo", None))
        self.digitalModePushButton.setText(QCoreApplication.translate("MainWindow", u" Digital", None))
        self.analogModePushButton.setText(QCoreApplication.translate("MainWindow", u" Anal\u00f3gico", None))
        self.samplingFrequencyLabel.setText(QCoreApplication.translate("MainWindow", u"Frecuencia de Muestreo", None))
        self.samplingFrequencyComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1 [KHz]", None))
        self.samplingFrequencyComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2.5 [KHz]", None))
        self.samplingFrequencyComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"5 [KHz]", None))
        self.samplingFrequencyComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"10 [KHz]", None))
        self.samplingFrequencyComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"25 [KHz]", None))
        self.samplingFrequencyComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"50 [KHz]", None))
        self.samplingFrequencyComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"100 [KHz]", None))
        self.samplingFrequencyComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"250 [KHz]", None))
        self.samplingFrequencyComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"500 [KHz]", None))
        self.samplingFrequencyComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"1 [MHz]", None))
        self.samplingFrequencyComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"2 [MHz]", None))
        self.samplingFrequencyComboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"5 [MHz]", None))
        self.samplingFrequencyComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"10 [MHz]", None))
        self.samplingFrequencyComboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"25 [MHz]", None))
        self.samplingFrequencyComboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"50 [MHz]", None))
        self.samplingFrequencyComboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"100 [MHz]", None))
        self.samplingFrequencyComboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"125 [MHz]", None))

        self.samplingDepthTilteLabel.setText(QCoreApplication.translate("MainWindow", u"Profundidad de Muestreo", None))
        self.samplingDepthValueLabel.setText(QCoreApplication.translate("MainWindow", u"20 [KiB]", None))
        self.samplingChannelsLabel.setText(QCoreApplication.translate("MainWindow", u"Canales Muestreados", None))
        self.samplingChannelsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.samplingChannelsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1-2", None))
        self.samplingChannelsComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"1-4", None))
        self.samplingChannelsComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"1-8", None))

        self.estimatedSamplingTimeTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Tiempo de Muestreo", None))
        self.estimatedSamplingTimeValueLabel.setText(QCoreApplication.translate("MainWindow", u"Placeholder", None))
        self.triggerChannelTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Canal y Evento", None))
        self.triggerChannelComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.triggerChannelComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.triggerChannelComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.triggerChannelComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.triggerChannelComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.triggerChannelComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.triggerChannelComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.triggerChannelComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))

        self.triggerModeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Inmediato", None))
        self.triggerModeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Flanco Subida", None))
        self.triggerModeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Flanco Bajada", None))
        self.triggerModeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Nivel Bajo", None))
        self.triggerModeComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Nivel Alto", None))

        self.triggerTimeoutLabel.setText(QCoreApplication.translate("MainWindow", u"Tiempo de Espera", None))
        self.triggerTimeoutDoubleSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" [s]", None))
        self.voltageThresholdLabel.setText(QCoreApplication.translate("MainWindow", u"Umbral de Voltaje", None))
        self.voltageThresholdDoubleSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" [V]", None))
        self.slideTabWidget.setTabText(self.slideTabWidget.indexOf(self.samplingConfigTab), QCoreApplication.translate("MainWindow", u"Config.", None))
        self.fixedMeasurementTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Mediciones Fijas", None))
        self.fixedMeasurementTime1Label.setText(QCoreApplication.translate("MainWindow", u"t1: []", None))
        self.fixedMeasurementTime2Label.setText(QCoreApplication.translate("MainWindow", u"t2: []", None))
        self.fixedMeasurementPeriodLabel.setText(QCoreApplication.translate("MainWindow", u"\u0394t: []", None))
        self.fixedMeasurementFrequencyLabel.setText(QCoreApplication.translate("MainWindow", u"1/\u0394t: []", None))
        self.fixedMeasurementSamplesLabel.setText(QCoreApplication.translate("MainWindow", u"Muestras:", None))
        self.triggerAnalysisTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Buscar Evento por Canal", None))
        self.triggerAnalysisChannelComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.triggerAnalysisChannelComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.triggerAnalysisChannelComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.triggerAnalysisChannelComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.triggerAnalysisChannelComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.triggerAnalysisChannelComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.triggerAnalysisChannelComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.triggerAnalysisChannelComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))

        self.triggerAnalysisModeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Flanco Subida", None))
        self.triggerAnalysisModeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Flanco Bajada", None))
        self.triggerAnalysisModeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Nivel Bajo", None))
        self.triggerAnalysisModeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Nivel Alto", None))

        self.triggerAnalysisGoLeftButton.setText("")
        self.triggerAnalysisGoRightButton.setText("")
        self.triggerAnalysisReferenceLabel.setText(QCoreApplication.translate("MainWindow", u"Referencia:", None))
        self.visorCenterRadioButton.setText(QCoreApplication.translate("MainWindow", u"Centro del Visor", None))
        self.lastCursorRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u00daltimo Cursor", None))
        self.analogYLimEditTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Ajustar Eje Y", None))
        self.topYLimLabel.setText(QCoreApplication.translate("MainWindow", u"L\u00edmite Sup.", None))
        self.topYLimDoubleSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" [V]", None))
        self.bitYLimLabel.setText(QCoreApplication.translate("MainWindow", u"L\u00edmite Inf.", None))
        self.botYLimDoubleSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" [V]", None))
        self.slideTabWidget.setTabText(self.slideTabWidget.indexOf(self.analysisTab), QCoreApplication.translate("MainWindow", u"An\u00e1lisis", None))
        self.binaryInterpretationRadioButton.setText(QCoreApplication.translate("MainWindow", u"Binario", None))
        self.interpretationLabel.setText(QCoreApplication.translate("MainWindow", u"Mostrar datos como", None))
        self.ASCIIInterpretationRadioButton.setText(QCoreApplication.translate("MainWindow", u"ASCII", None))
        self.hexadecimalInterpretationRadioButton.setText(QCoreApplication.translate("MainWindow", u"Hexadecimal", None))
        self.decimalInterpretationRadioButton.setText(QCoreApplication.translate("MainWindow", u"Decimal", None))
        self.FramesListLabel.setText(QCoreApplication.translate("MainWindow", u"Lista de tramas", None))
        self.slideTabWidget.setTabText(self.slideTabWidget.indexOf(self.protocolTab), QCoreApplication.translate("MainWindow", u"Protocolo", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"ALyP GUI v1.0", None))
    # retranslateUi

