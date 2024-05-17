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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGraphicsView, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QScrollBar, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 782)
        MainWindow.setMinimumSize(QSize(950, 0))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/ButtonIcons/ico/square-wave.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(100, 24))
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(9)
        self.centralWidget.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainFrame = QFrame(self.centralWidget)
        self.mainFrame.setObjectName(u"mainFrame")
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

        self.cursorPushButton = QPushButton(self.headerMainFrame)
        self.cursorPushButton.setObjectName(u"cursorPushButton")
        self.cursorPushButton.setMinimumSize(QSize(30, 30))
        self.cursorPushButton.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/ButtonIcons/ico/mouse-crosshair-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cursorPushButton.setIcon(icon1)
        self.cursorPushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.cursorPushButton)

        self.startSamplingPushButton = QPushButton(self.headerMainFrame)
        self.startSamplingPushButton.setObjectName(u"startSamplingPushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.startSamplingPushButton.sizePolicy().hasHeightForWidth())
        self.startSamplingPushButton.setSizePolicy(sizePolicy1)
        self.startSamplingPushButton.setMinimumSize(QSize(30, 30))
        self.startSamplingPushButton.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/ButtonIcons/ico/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startSamplingPushButton.setIcon(icon2)
        self.startSamplingPushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.startSamplingPushButton)

        self.configSliderPushButton = QPushButton(self.headerMainFrame)
        self.configSliderPushButton.setObjectName(u"configSliderPushButton")
        self.configSliderPushButton.setMinimumSize(QSize(30, 30))
        self.configSliderPushButton.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/ButtonIcons/ico/Three stripes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.configSliderPushButton.setIcon(icon3)
        self.configSliderPushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.configSliderPushButton)


        self.verticalLayout_19.addWidget(self.headerMainFrame)

        self.logicAnalyzersScrollArea = QScrollArea(self.mainFrame)
        self.logicAnalyzersScrollArea.setObjectName(u"logicAnalyzersScrollArea")
        self.logicAnalyzersScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.logicAnalyzersScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.logicAnalyzersScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 705, 684))
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
        self.axisLabel.setMinimumSize(QSize(62, 0))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(8)
        self.axisLabel.setFont(font2)

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
        self.channel1IDLabel.setMinimumSize(QSize(25, 0))
        self.channel1IDLabel.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout_10.addWidget(self.channel1IDLabel)

        self.channel1ProtocolLabel = QLabel(self.channel1LabelFrame)
        self.channel1ProtocolLabel.setObjectName(u"channel1ProtocolLabel")

        self.verticalLayout_10.addWidget(self.channel1ProtocolLabel)


        self.horizontalLayout_4.addWidget(self.channel1LabelFrame)

        self.channel1GraphicsView = QGraphicsView(self.channel1Frame)
        self.channel1GraphicsView.setObjectName(u"channel1GraphicsView")
        self.channel1GraphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.channel1GraphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_4.addWidget(self.channel1GraphicsView)


        self.verticalLayout_17.addWidget(self.channel1Frame)

        self.channel2Frame = QFrame(self.scrollAreaWidgetContents)
        self.channel2Frame.setObjectName(u"channel2Frame")
        sizePolicy.setHeightForWidth(self.channel2Frame.sizePolicy().hasHeightForWidth())
        self.channel2Frame.setSizePolicy(sizePolicy)
        self.channel2Frame.setMaximumSize(QSize(16777215, 75))
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

        self.verticalLayout_11.addWidget(self.channel2IDLabel)

        self.channel2ProtocolLabel = QLabel(self.channel2LabelFrame)
        self.channel2ProtocolLabel.setObjectName(u"channel2ProtocolLabel")

        self.verticalLayout_11.addWidget(self.channel2ProtocolLabel)


        self.horizontalLayout_5.addWidget(self.channel2LabelFrame)

        self.channel2GraphicsView = QGraphicsView(self.channel2Frame)
        self.channel2GraphicsView.setObjectName(u"channel2GraphicsView")
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

        self.verticalLayout_12.addWidget(self.channel3IDLabel)

        self.channel3ProtocolLabel = QLabel(self.channel3LabelFrame)
        self.channel3ProtocolLabel.setObjectName(u"channel3ProtocolLabel")

        self.verticalLayout_12.addWidget(self.channel3ProtocolLabel)


        self.horizontalLayout_6.addWidget(self.channel3LabelFrame)

        self.channel3GraphicsView = QGraphicsView(self.channel3Frame)
        self.channel3GraphicsView.setObjectName(u"channel3GraphicsView")
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

        self.verticalLayout_13.addWidget(self.channel4IDLabel)

        self.channel4ProtocolLabel = QLabel(self.channel4LabelFrame)
        self.channel4ProtocolLabel.setObjectName(u"channel4ProtocolLabel")

        self.verticalLayout_13.addWidget(self.channel4ProtocolLabel)


        self.horizontalLayout_7.addWidget(self.channel4LabelFrame)

        self.channel4GraphicsView = QGraphicsView(self.channel4Frame)
        self.channel4GraphicsView.setObjectName(u"channel4GraphicsView")
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

        self.verticalLayout_14.addWidget(self.channel5IDLabel)

        self.channel5ProtocolLabel = QLabel(self.channel5LabelFrame)
        self.channel5ProtocolLabel.setObjectName(u"channel5ProtocolLabel")

        self.verticalLayout_14.addWidget(self.channel5ProtocolLabel)


        self.horizontalLayout_8.addWidget(self.channel5LabelFrame)

        self.channel5GraphicsView = QGraphicsView(self.channel5Frame)
        self.channel5GraphicsView.setObjectName(u"channel5GraphicsView")
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

        self.verticalLayout_15.addWidget(self.channel6IDLabel)

        self.channel6ProtocolLabel = QLabel(self.channel6LabelFrame)
        self.channel6ProtocolLabel.setObjectName(u"channel6ProtocolLabel")

        self.verticalLayout_15.addWidget(self.channel6ProtocolLabel)


        self.horizontalLayout_9.addWidget(self.channel6LabelFrame)

        self.channel6GraphicsView = QGraphicsView(self.channel6Frame)
        self.channel6GraphicsView.setObjectName(u"channel6GraphicsView")
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

        self.verticalLayout_16.addWidget(self.channel7IDLabel)

        self.channel7ProtocolLabel = QLabel(self.channel7LabelFrame)
        self.channel7ProtocolLabel.setObjectName(u"channel7ProtocolLabel")

        self.verticalLayout_16.addWidget(self.channel7ProtocolLabel)


        self.horizontalLayout_10.addWidget(self.channel7LabelFrame)

        self.channel7GraphicsView = QGraphicsView(self.channel7Frame)
        self.channel7GraphicsView.setObjectName(u"channel7GraphicsView")
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

        self.verticalLayout_18.addWidget(self.channel8IDLabel)

        self.channel8ProtocolLabel = QLabel(self.channel8LabelFrame)
        self.channel8ProtocolLabel.setObjectName(u"channel8ProtocolLabel")

        self.verticalLayout_18.addWidget(self.channel8ProtocolLabel)


        self.horizontalLayout_11.addWidget(self.channel8LabelFrame)

        self.channel8GraphicsView = QGraphicsView(self.channel8Frame)
        self.channel8GraphicsView.setObjectName(u"channel8GraphicsView")
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
        font3 = QFont()
        font3.setFamilies([u"consolas"])
        font3.setPointSize(9)
        self.connectionStatusLabel.setFont(font3)
        self.connectionStatusLabel.setStyleSheet(u"*\n"
"{\n"
"background-color: #ff4a4a;\n"
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
        self.slideTabWidget.setStyleSheet(u"QFrame#samplingChannelsFrame,\n"
"QFrame#samplingDepthFrame,\n"
"QFrame#samplingFrequencyFrame,\n"
"QFrame#samplingModeFrame\n"
"{\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius: 7px;\n"
"padding:5px;\n"
"padding-bottom:8px\n"
"}")
        self.samplingConfigTab = QWidget()
        self.samplingConfigTab.setObjectName(u"samplingConfigTab")
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
"QFrame#estimatedSamplingTimeFrame\n"
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
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        icon4 = QIcon()
        icon4.addFile(u":/ButtonIcons/ico/Sine-wave.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.analogModePushButton.setIcon(icon4)

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

        self.slideFrameVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.slideFrameVerticalSpacer)


        self.verticalLayout_9.addWidget(self.samplingFrame)

        self.slideTabWidget.addTab(self.samplingConfigTab, "")
        self.triggerTab = QWidget()
        self.triggerTab.setObjectName(u"triggerTab")
        self.verticalLayout_23 = QVBoxLayout(self.triggerTab)
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.triggerFrame = QFrame(self.triggerTab)
        self.triggerFrame.setObjectName(u"triggerFrame")
        self.triggerFrame.setStyleSheet(u"QFrame#triggerChannelFrame,\n"
"QFrame#triggerTimeoutFrame,\n"
"QFrame#voltageThresholdFrame\n"
"{\n"
"border: 1px solid rgb(109, 109, 109);\n"
"border-radius: 7px;\n"
"padding:5px;\n"
"padding-bottom:8px\n"
"}")
        self.triggerFrame.setFrameShape(QFrame.StyledPanel)
        self.triggerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.triggerFrame)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.triggerChannelFrame = QFrame(self.triggerFrame)
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
        icon5 = QIcon()
        icon5.addFile(u":/ButtonIcons/ico/UNTRIGGERED.png", QSize(), QIcon.Normal, QIcon.Off)
        self.triggerModeComboBox.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/ButtonIcons/ico/RISING EDGE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.triggerModeComboBox.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/ButtonIcons/ico/FALLING EDGE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.triggerModeComboBox.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u":/ButtonIcons/ico/LOW LEVEL.png", QSize(), QIcon.Normal, QIcon.Off)
        self.triggerModeComboBox.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/ButtonIcons/ico/HIGH LEVEL.png", QSize(), QIcon.Normal, QIcon.Off)
        self.triggerModeComboBox.addItem(icon9, "")
        self.triggerModeComboBox.setObjectName(u"triggerModeComboBox")
        self.triggerModeComboBox.setMinimumSize(QSize(0, 25))
        self.triggerModeComboBox.setFont(font)

        self.horizontalLayout_16.addWidget(self.triggerModeComboBox)


        self.verticalLayout_20.addWidget(self.triggerChannelButtonsFrame)


        self.verticalLayout_7.addWidget(self.triggerChannelFrame)

        self.triggerTimeoutFrame = QFrame(self.triggerFrame)
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
        self.triggerTimeoutDoubleSpinBox.setFont(font1)
        self.triggerTimeoutDoubleSpinBox.setMinimum(0.300000000000000)
        self.triggerTimeoutDoubleSpinBox.setSingleStep(0.100000000000000)
        self.triggerTimeoutDoubleSpinBox.setValue(0.300000000000000)

        self.horizontalLayout_17.addWidget(self.triggerTimeoutDoubleSpinBox)


        self.verticalLayout_7.addWidget(self.triggerTimeoutFrame)

        self.voltageThresholdFrame = QFrame(self.triggerFrame)
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
        self.voltageThresholdDoubleSpinBox.setFont(font1)
        self.voltageThresholdDoubleSpinBox.setMaximum(3.300000000000000)
        self.voltageThresholdDoubleSpinBox.setSingleStep(0.010000000000000)
        self.voltageThresholdDoubleSpinBox.setValue(2.600000000000000)

        self.horizontalLayout_2.addWidget(self.voltageThresholdDoubleSpinBox)


        self.verticalLayout_7.addWidget(self.voltageThresholdFrame)

        self.triggerVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.triggerVerticalSpacer)


        self.verticalLayout_23.addWidget(self.triggerFrame)

        self.slideTabWidget.addTab(self.triggerTab, "")

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
        font4 = QFont()
        font4.setFamilies([u"Consolas"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setUnderline(False)
        self.versionLabel.setFont(font4)
        self.versionLabel.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.slideFrameFooter, 0, Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.slideFrameContainer)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        self.slideTabWidget.setCurrentIndex(0)
        self.samplingFrequencyComboBox.setCurrentIndex(16)
        self.samplingChannelsComboBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Proyecto Final", None))
        self.channelVisualizationLabel.setText(QCoreApplication.translate("MainWindow", u"Visualizar Canales", None))
        self.channel1CheckBox.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.channel2CheckBox.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.channel3CheckBox.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.channel4CheckBox.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.channel5CheckBox.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.channel6CheckBox.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.channel7CheckBox.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.channel8CheckBox.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.cursorPushButton.setText("")
        self.startSamplingPushButton.setText("")
        self.configSliderPushButton.setText("")
        self.axisLabel.setText(QCoreApplication.translate("MainWindow", u"Tiempo:", None))
        self.channel1IDLabel.setText(QCoreApplication.translate("MainWindow", u"Canal 1", None))
        self.channel1ProtocolLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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
        self.digitalModePushButton.setText(QCoreApplication.translate("MainWindow", u"Digital", None))
        self.analogModePushButton.setText(QCoreApplication.translate("MainWindow", u"Anal\u00f3gico", None))
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
        self.slideTabWidget.setTabText(self.slideTabWidget.indexOf(self.samplingConfigTab), QCoreApplication.translate("MainWindow", u"Muestreo", None))
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
        self.slideTabWidget.setTabText(self.slideTabWidget.indexOf(self.triggerTab), QCoreApplication.translate("MainWindow", u"Gatillado", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"ALyP GUI v0.1", None))
    # retranslateUi

