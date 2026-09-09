# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'marine_app_final.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet(u"\n"
"* { font-family: Barlow, Segoe UI, Arial, sans-serif; font-size: 13px; }\n"
"QMainWindow, QWidget#centralwidget { background: #f4f6fb; }\n"
"QWidget#navbar { background: #fff; border-bottom: 1px solid #d0d8ee; min-height: 62px; max-height: 62px; }\n"
"QPushButton#logoBtn { background: transparent; border: none; font-size: 15px; font-weight: 700; color: #0c0d11; }\n"
"QPushButton#navBtn { background: transparent; border: none; font-size: 14px; color: #6070a0; padding: 6px 14px; border-radius: 6px; }\n"
"QPushButton#navBtn:hover { color: #0c0d11; }\n"
"QPushButton#ctaBtn { background: #3d5cd8; color: #fff; border: none; border-radius: 100px; padding: 8px 20px; font-weight: 600; }\n"
"QPushButton#ctaBtn:hover { background: #2e48b8; }\n"
"QWidget#heroSection { background: qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 #0c0d11,stop:0.6 #1a2340,stop:1 #263668); min-height: 480px; }\n"
"QLabel#heroTitle { color: #fff; font-size: 42px; font-weight: 800; background: transparent; }\n"
"QLabel#heroSub { color: rgba(255,"
                        "255,255,0.6); font-size: 15px; background: transparent; }\n"
"QLabel#heroEyebrow { color: rgba(255,255,255,0.5); font-size: 12px; background: transparent; }\n"
"QLabel#statVal { color: #fff; font-size: 28px; font-weight: 800; background: transparent; }\n"
"QLabel#statLabel { color: rgba(255,255,255,0.5); font-size: 12px; background: transparent; }\n"
"QPushButton#heroPrimary { background: #3d5cd8; color: #fff; border: none; border-radius: 100px; padding: 12px 26px; font-size: 14px; font-weight: 600; }\n"
"QPushButton#heroPrimary:hover { background: #2e48b8; }\n"
"QPushButton#heroGhost { background: transparent; color: rgba(255,255,255,0.85); border: 1px solid rgba(255,255,255,0.25); border-radius: 100px; padding: 12px 24px; font-size: 14px; }\n"
"QLabel#sectionTitle { color: #0c0d11; font-size: 24px; font-weight: 700; background: transparent; }\n"
"QLabel#sectionEyebrow { color: #6070a0; font-size: 12px; font-weight: 500; background: transparent; }\n"
"QLabel#capTitle { color: #0c0d11; font-size: 14px; font-we"
                        "ight: 700; background: transparent; }\n"
"QLabel#capDesc { color: #6070a0; font-size: 12px; background: transparent; }\n"
"QFrame#capCard { background: #fff; border: 1px solid #d0d8ee; border-radius: 10px; }\n"
"QWidget#pageHeader { background: #fff; border-bottom: 1px solid #d0d8ee; }\n"
"QLabel#pageTitle { color: #0c0d11; font-size: 24px; font-weight: 700; background: transparent; }\n"
"QLabel#pageSub { color: #6070a0; font-size: 13px; background: transparent; }\n"
"QLabel#pageEyebrow { color: #6070a0; font-size: 12px; background: transparent; }\n"
"QPushButton#btnPrimary { background: #3d5cd8; color: #fff; border: none; border-radius: 100px; padding: 10px 22px; font-weight: 600; }\n"
"QPushButton#btnPrimary:hover { background: #2e48b8; }\n"
"QTableWidget { background: #fff; border: 1px solid #d0d8ee; border-radius: 10px; gridline-color: #d0d8ee; }\n"
"QTableWidget::item { padding: 10px 14px; }\n"
"QTableWidget::item:selected { background: #e8edf8; color: #0c0d11; }\n"
"QHeaderView::section { background: #f4"
                        "f6fb; color: #6070a0; font-size: 10px; font-weight: 700; padding: 8px 14px; border: none; border-bottom: 1px solid #d0d8ee; }\n"
"QLineEdit, QComboBox { background: #fff; border: 1px solid #d0d8ee; border-radius: 8px; padding: 8px 12px; color: #0c0d11; }\n"
"QLineEdit:focus, QComboBox:focus { border-color: #3d5cd8; }\n"
"QCheckBox { spacing: 8px; color: #0c0d11; }\n"
"QCheckBox::indicator { width: 16px; height: 16px; border-radius: 4px; border: 1.5px solid #d0d8ee; background: #fff; }\n"
"QCheckBox::indicator:checked { background: #3d5cd8; border-color: #3d5cd8; }\n"
"QSlider::groove:horizontal { height: 4px; background: #d0d8ee; border-radius: 2px; }\n"
"QSlider::handle:horizontal { background: #3d5cd8; width: 14px; height: 14px; margin: -5px 0; border-radius: 7px; }\n"
"QSlider::sub-page:horizontal { background: #3d5cd8; border-radius: 2px; }\n"
"QScrollBar:vertical { width: 4px; background: transparent; }\n"
"QScrollBar::handle:vertical { background: #8090c8; border-radius: 2px; min-height: 24px; }\n"
"QScr"
                        "ollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }\n"
"  ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.navbar = QWidget(self.centralwidget)
        self.navbar.setObjectName(u"navbar")
        self.hboxLayout = QHBoxLayout(self.navbar)
        self.hboxLayout.setSpacing(4)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(48, 0, 48, 0)
        self.logoBtn = QPushButton(self.navbar)
        self.logoBtn.setObjectName(u"logoBtn")

        self.hboxLayout.addWidget(self.logoBtn)

        self.spacerItem = QSpacerItem(40, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerItem)

        self.navHome = QPushButton(self.navbar)
        self.navHome.setObjectName(u"navHome")

        self.hboxLayout.addWidget(self.navHome)

        self.navAnalyze = QPushButton(self.navbar)
        self.navAnalyze.setObjectName(u"navAnalyze")

        self.hboxLayout.addWidget(self.navAnalyze)

        self.navMap = QPushButton(self.navbar)
        self.navMap.setObjectName(u"navMap")

        self.hboxLayout.addWidget(self.navMap)

        self.navReports = QPushButton(self.navbar)
        self.navReports.setObjectName(u"navReports")

        self.hboxLayout.addWidget(self.navReports)

        self.navDataset = QPushButton(self.navbar)
        self.navDataset.setObjectName(u"navDataset")

        self.hboxLayout.addWidget(self.navDataset)

        self.navConfig = QPushButton(self.navbar)
        self.navConfig.setObjectName(u"navConfig")

        self.hboxLayout.addWidget(self.navConfig)

        self.spacerItem1 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerItem1)

        self.ctaBtn = QPushButton(self.navbar)
        self.ctaBtn.setObjectName(u"ctaBtn")

        self.hboxLayout.addWidget(self.ctaBtn)


        self.mainLayout.addWidget(self.navbar)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.vboxLayout = QVBoxLayout(self.homePage)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.heroSection = QWidget(self.homePage)
        self.heroSection.setObjectName(u"heroSection")
        self.vboxLayout1 = QVBoxLayout(self.heroSection)
        self.vboxLayout1.setSpacing(14)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.vboxLayout1.setContentsMargins(48, 72, 48, 64)
        self.heroEyebrow = QLabel(self.heroSection)
        self.heroEyebrow.setObjectName(u"heroEyebrow")

        self.vboxLayout1.addWidget(self.heroEyebrow)

        self.heroTitle = QLabel(self.heroSection)
        self.heroTitle.setObjectName(u"heroTitle")

        self.vboxLayout1.addWidget(self.heroTitle)

        self.heroSub = QLabel(self.heroSection)
        self.heroSub.setObjectName(u"heroSub")
        self.heroSub.setWordWrap(True)

        self.vboxLayout1.addWidget(self.heroSub)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setSpacing(12)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.heroAnalyzeBtn = QPushButton(self.heroSection)
        self.heroAnalyzeBtn.setObjectName(u"heroAnalyzeBtn")

        self.hboxLayout1.addWidget(self.heroAnalyzeBtn)

        self.heroMapBtn = QPushButton(self.heroSection)
        self.heroMapBtn.setObjectName(u"heroMapBtn")

        self.hboxLayout1.addWidget(self.heroMapBtn)

        self.spacerItem2 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout1.addItem(self.spacerItem2)


        self.vboxLayout1.addLayout(self.hboxLayout1)

        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setSpacing(0)
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.vboxLayout2 = QVBoxLayout()
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.vboxLayout2.setContentsMargins(0, 28, 32, 0)
        self.s0v = QLabel(self.heroSection)
        self.s0v.setObjectName(u"s0v")

        self.vboxLayout2.addWidget(self.s0v)

        self.s0l = QLabel(self.heroSection)
        self.s0l.setObjectName(u"s0l")

        self.vboxLayout2.addWidget(self.s0l)


        self.hboxLayout2.addLayout(self.vboxLayout2)

        self.vboxLayout3 = QVBoxLayout()
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.vboxLayout3.setContentsMargins(32, 28, 32, 0)
        self.s1v = QLabel(self.heroSection)
        self.s1v.setObjectName(u"s1v")

        self.vboxLayout3.addWidget(self.s1v)

        self.s1l = QLabel(self.heroSection)
        self.s1l.setObjectName(u"s1l")

        self.vboxLayout3.addWidget(self.s1l)


        self.hboxLayout2.addLayout(self.vboxLayout3)

        self.vboxLayout4 = QVBoxLayout()
        self.vboxLayout4.setObjectName(u"vboxLayout4")
        self.vboxLayout4.setContentsMargins(32, 28, 32, 0)
        self.s2v = QLabel(self.heroSection)
        self.s2v.setObjectName(u"s2v")

        self.vboxLayout4.addWidget(self.s2v)

        self.s2l = QLabel(self.heroSection)
        self.s2l.setObjectName(u"s2l")

        self.vboxLayout4.addWidget(self.s2l)


        self.hboxLayout2.addLayout(self.vboxLayout4)

        self.vboxLayout5 = QVBoxLayout()
        self.vboxLayout5.setObjectName(u"vboxLayout5")
        self.vboxLayout5.setContentsMargins(32, 28, 0, 0)
        self.s3v = QLabel(self.heroSection)
        self.s3v.setObjectName(u"s3v")

        self.vboxLayout5.addWidget(self.s3v)

        self.s3l = QLabel(self.heroSection)
        self.s3l.setObjectName(u"s3l")

        self.vboxLayout5.addWidget(self.s3l)


        self.hboxLayout2.addLayout(self.vboxLayout5)

        self.spacerItem3 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout2.addItem(self.spacerItem3)


        self.vboxLayout1.addLayout(self.hboxLayout2)


        self.vboxLayout.addWidget(self.heroSection)

        self.capsSection = QWidget(self.homePage)
        self.capsSection.setObjectName(u"capsSection")
        self.vboxLayout6 = QVBoxLayout(self.capsSection)
        self.vboxLayout6.setSpacing(18)
        self.vboxLayout6.setObjectName(u"vboxLayout6")
        self.vboxLayout6.setContentsMargins(48, 48, 48, 48)
        self.label = QLabel(self.capsSection)
        self.label.setObjectName(u"label")

        self.vboxLayout6.addWidget(self.label)

        self.label1 = QLabel(self.capsSection)
        self.label1.setObjectName(u"label1")

        self.vboxLayout6.addWidget(self.label1)

        self.hboxLayout3 = QHBoxLayout()
        self.hboxLayout3.setSpacing(16)
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.c0 = QFrame(self.capsSection)
        self.c0.setObjectName(u"c0")
        self.vboxLayout7 = QVBoxLayout(self.c0)
        self.vboxLayout7.setObjectName(u"vboxLayout7")
        self.vboxLayout7.setContentsMargins(20, 22, 20, 22)
        self.label2 = QLabel(self.c0)
        self.label2.setObjectName(u"label2")

        self.vboxLayout7.addWidget(self.label2)

        self.label3 = QLabel(self.c0)
        self.label3.setObjectName(u"label3")
        self.label3.setWordWrap(True)

        self.vboxLayout7.addWidget(self.label3)


        self.hboxLayout3.addWidget(self.c0)

        self.c1 = QFrame(self.capsSection)
        self.c1.setObjectName(u"c1")
        self.vboxLayout8 = QVBoxLayout(self.c1)
        self.vboxLayout8.setObjectName(u"vboxLayout8")
        self.vboxLayout8.setContentsMargins(20, 22, 20, 22)
        self.label4 = QLabel(self.c1)
        self.label4.setObjectName(u"label4")

        self.vboxLayout8.addWidget(self.label4)

        self.label5 = QLabel(self.c1)
        self.label5.setObjectName(u"label5")
        self.label5.setWordWrap(True)

        self.vboxLayout8.addWidget(self.label5)


        self.hboxLayout3.addWidget(self.c1)

        self.c2 = QFrame(self.capsSection)
        self.c2.setObjectName(u"c2")
        self.vboxLayout9 = QVBoxLayout(self.c2)
        self.vboxLayout9.setObjectName(u"vboxLayout9")
        self.vboxLayout9.setContentsMargins(20, 22, 20, 22)
        self.label6 = QLabel(self.c2)
        self.label6.setObjectName(u"label6")

        self.vboxLayout9.addWidget(self.label6)

        self.label7 = QLabel(self.c2)
        self.label7.setObjectName(u"label7")
        self.label7.setWordWrap(True)

        self.vboxLayout9.addWidget(self.label7)


        self.hboxLayout3.addWidget(self.c2)

        self.c3 = QFrame(self.capsSection)
        self.c3.setObjectName(u"c3")
        self.vboxLayout10 = QVBoxLayout(self.c3)
        self.vboxLayout10.setObjectName(u"vboxLayout10")
        self.vboxLayout10.setContentsMargins(20, 22, 20, 22)
        self.label8 = QLabel(self.c3)
        self.label8.setObjectName(u"label8")

        self.vboxLayout10.addWidget(self.label8)

        self.label9 = QLabel(self.c3)
        self.label9.setObjectName(u"label9")
        self.label9.setWordWrap(True)

        self.vboxLayout10.addWidget(self.label9)


        self.hboxLayout3.addWidget(self.c3)


        self.vboxLayout6.addLayout(self.hboxLayout3)


        self.vboxLayout.addWidget(self.capsSection)

        self.spacerItem4 = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.spacerItem4)

        self.stackedWidget.addWidget(self.homePage)
        self.analyzePage = QWidget()
        self.analyzePage.setObjectName(u"analyzePage")
        self.vboxLayout11 = QVBoxLayout(self.analyzePage)
        self.vboxLayout11.setSpacing(0)
        self.vboxLayout11.setObjectName(u"vboxLayout11")
        self.vboxLayout11.setContentsMargins(0, 0, 0, 0)
        self.analyzeHeader = QWidget(self.analyzePage)
        self.analyzeHeader.setObjectName(u"analyzeHeader")
        self.hboxLayout4 = QHBoxLayout(self.analyzeHeader)
        self.hboxLayout4.setObjectName(u"hboxLayout4")
        self.hboxLayout4.setContentsMargins(48, 28, 48, 20)
        self.vboxLayout12 = QVBoxLayout()
        self.vboxLayout12.setSpacing(3)
        self.vboxLayout12.setObjectName(u"vboxLayout12")
        self.label10 = QLabel(self.analyzeHeader)
        self.label10.setObjectName(u"label10")

        self.vboxLayout12.addWidget(self.label10)

        self.label11 = QLabel(self.analyzeHeader)
        self.label11.setObjectName(u"label11")

        self.vboxLayout12.addWidget(self.label11)

        self.label12 = QLabel(self.analyzeHeader)
        self.label12.setObjectName(u"label12")

        self.vboxLayout12.addWidget(self.label12)


        self.hboxLayout4.addLayout(self.vboxLayout12)

        self.spacerItem5 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout4.addItem(self.spacerItem5)

        self.runDetectionBtn = QPushButton(self.analyzeHeader)
        self.runDetectionBtn.setObjectName(u"runDetectionBtn")

        self.hboxLayout4.addWidget(self.runDetectionBtn)


        self.vboxLayout11.addWidget(self.analyzeHeader)

        self.label13 = QLabel(self.analyzePage)
        self.label13.setObjectName(u"label13")
        self.label13.setAlignment(Qt.AlignCenter)

        self.vboxLayout11.addWidget(self.label13)

        self.spacerItem6 = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout11.addItem(self.spacerItem6)

        self.stackedWidget.addWidget(self.analyzePage)
        self.mapPage = QWidget()
        self.mapPage.setObjectName(u"mapPage")
        self.vboxLayout13 = QVBoxLayout(self.mapPage)
        self.vboxLayout13.setSpacing(0)
        self.vboxLayout13.setObjectName(u"vboxLayout13")
        self.vboxLayout13.setContentsMargins(0, 0, 0, 0)
        self.mapHeader = QWidget(self.mapPage)
        self.mapHeader.setObjectName(u"mapHeader")
        self.hboxLayout5 = QHBoxLayout(self.mapHeader)
        self.hboxLayout5.setObjectName(u"hboxLayout5")
        self.hboxLayout5.setContentsMargins(48, 28, 48, 20)
        self.vboxLayout14 = QVBoxLayout()
        self.vboxLayout14.setSpacing(3)
        self.vboxLayout14.setObjectName(u"vboxLayout14")
        self.label14 = QLabel(self.mapHeader)
        self.label14.setObjectName(u"label14")

        self.vboxLayout14.addWidget(self.label14)

        self.label15 = QLabel(self.mapHeader)
        self.label15.setObjectName(u"label15")

        self.vboxLayout14.addWidget(self.label15)

        self.label16 = QLabel(self.mapHeader)
        self.label16.setObjectName(u"label16")

        self.vboxLayout14.addWidget(self.label16)


        self.hboxLayout5.addLayout(self.vboxLayout14)


        self.vboxLayout13.addWidget(self.mapHeader)

        self.label17 = QLabel(self.mapPage)
        self.label17.setObjectName(u"label17")
        self.label17.setAlignment(Qt.AlignCenter)

        self.vboxLayout13.addWidget(self.label17)

        self.spacerItem7 = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout13.addItem(self.spacerItem7)

        self.stackedWidget.addWidget(self.mapPage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.vboxLayout15 = QVBoxLayout(self.reportsPage)
        self.vboxLayout15.setSpacing(0)
        self.vboxLayout15.setObjectName(u"vboxLayout15")
        self.vboxLayout15.setContentsMargins(0, 0, 0, 0)
        self.reportsHeader = QWidget(self.reportsPage)
        self.reportsHeader.setObjectName(u"reportsHeader")
        self.hboxLayout6 = QHBoxLayout(self.reportsHeader)
        self.hboxLayout6.setObjectName(u"hboxLayout6")
        self.hboxLayout6.setContentsMargins(48, 28, 48, 20)
        self.vboxLayout16 = QVBoxLayout()
        self.vboxLayout16.setSpacing(3)
        self.vboxLayout16.setObjectName(u"vboxLayout16")
        self.label18 = QLabel(self.reportsHeader)
        self.label18.setObjectName(u"label18")

        self.vboxLayout16.addWidget(self.label18)

        self.label19 = QLabel(self.reportsHeader)
        self.label19.setObjectName(u"label19")

        self.vboxLayout16.addWidget(self.label19)

        self.label20 = QLabel(self.reportsHeader)
        self.label20.setObjectName(u"label20")

        self.vboxLayout16.addWidget(self.label20)


        self.hboxLayout6.addLayout(self.vboxLayout16)

        self.spacerItem8 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout6.addItem(self.spacerItem8)

        self.generateReportBtn = QPushButton(self.reportsHeader)
        self.generateReportBtn.setObjectName(u"generateReportBtn")

        self.hboxLayout6.addWidget(self.generateReportBtn)


        self.vboxLayout15.addWidget(self.reportsHeader)

        self.reportsContent = QWidget(self.reportsPage)
        self.reportsContent.setObjectName(u"reportsContent")
        self.vboxLayout17 = QVBoxLayout(self.reportsContent)
        self.vboxLayout17.setObjectName(u"vboxLayout17")
        self.vboxLayout17.setContentsMargins(48, 24, 48, 24)
        self.reportsTable = QTableWidget(self.reportsContent)
        self.reportsTable.setObjectName(u"reportsTable")
        self.reportsTable.setColumnCount(6)
        self.reportsTable.setRowCount(4)

        self.vboxLayout17.addWidget(self.reportsTable)


        self.vboxLayout15.addWidget(self.reportsContent)

        self.stackedWidget.addWidget(self.reportsPage)
        self.datasetPage = QWidget()
        self.datasetPage.setObjectName(u"datasetPage")
        self.vboxLayout18 = QVBoxLayout(self.datasetPage)
        self.vboxLayout18.setSpacing(0)
        self.vboxLayout18.setObjectName(u"vboxLayout18")
        self.vboxLayout18.setContentsMargins(0, 0, 0, 0)
        self.datasetHeader = QWidget(self.datasetPage)
        self.datasetHeader.setObjectName(u"datasetHeader")
        self.hboxLayout7 = QHBoxLayout(self.datasetHeader)
        self.hboxLayout7.setObjectName(u"hboxLayout7")
        self.hboxLayout7.setContentsMargins(48, 28, 48, 20)
        self.vboxLayout19 = QVBoxLayout()
        self.vboxLayout19.setSpacing(3)
        self.vboxLayout19.setObjectName(u"vboxLayout19")
        self.label21 = QLabel(self.datasetHeader)
        self.label21.setObjectName(u"label21")

        self.vboxLayout19.addWidget(self.label21)

        self.label22 = QLabel(self.datasetHeader)
        self.label22.setObjectName(u"label22")

        self.vboxLayout19.addWidget(self.label22)

        self.label23 = QLabel(self.datasetHeader)
        self.label23.setObjectName(u"label23")

        self.vboxLayout19.addWidget(self.label23)


        self.hboxLayout7.addLayout(self.vboxLayout19)

        self.spacerItem9 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout7.addItem(self.spacerItem9)

        self.importDatasetBtn = QPushButton(self.datasetHeader)
        self.importDatasetBtn.setObjectName(u"importDatasetBtn")

        self.hboxLayout7.addWidget(self.importDatasetBtn)


        self.vboxLayout18.addWidget(self.datasetHeader)

        self.datasetPlaceholder = QLabel(self.datasetPage)
        self.datasetPlaceholder.setObjectName(u"datasetPlaceholder")
        self.datasetPlaceholder.setAlignment(Qt.AlignCenter)

        self.vboxLayout18.addWidget(self.datasetPlaceholder)

        self.spacerItem10 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout18.addItem(self.spacerItem10)

        self.stackedWidget.addWidget(self.datasetPage)
        self.configPage = QWidget()
        self.configPage.setObjectName(u"configPage")
        self.vboxLayout20 = QVBoxLayout(self.configPage)
        self.vboxLayout20.setSpacing(0)
        self.vboxLayout20.setObjectName(u"vboxLayout20")
        self.vboxLayout20.setContentsMargins(0, 0, 0, 0)
        self.configHeader = QWidget(self.configPage)
        self.configHeader.setObjectName(u"configHeader")
        self.vboxLayout21 = QVBoxLayout(self.configHeader)
        self.vboxLayout21.setObjectName(u"vboxLayout21")
        self.vboxLayout21.setContentsMargins(48, 28, 48, 20)
        self.label24 = QLabel(self.configHeader)
        self.label24.setObjectName(u"label24")

        self.vboxLayout21.addWidget(self.label24)

        self.label25 = QLabel(self.configHeader)
        self.label25.setObjectName(u"label25")

        self.vboxLayout21.addWidget(self.label25)

        self.label26 = QLabel(self.configHeader)
        self.label26.setObjectName(u"label26")

        self.vboxLayout21.addWidget(self.label26)


        self.vboxLayout20.addWidget(self.configHeader)

        self.configPlaceholder = QLabel(self.configPage)
        self.configPlaceholder.setObjectName(u"configPlaceholder")
        self.configPlaceholder.setAlignment(Qt.AlignCenter)

        self.vboxLayout20.addWidget(self.configPlaceholder)

        self.spacerItem11 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout20.addItem(self.spacerItem11)

        self.stackedWidget.addWidget(self.configPage)

        self.mainLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MarineVision", None))
        self.logoBtn.setText(QCoreApplication.translate("MainWindow", u"MarineVision", None))
        self.navHome.setObjectName(QCoreApplication.translate("MainWindow", u"navBtn", None))
        self.navHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.navAnalyze.setObjectName(QCoreApplication.translate("MainWindow", u"navBtn", None))
        self.navAnalyze.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.navMap.setObjectName(QCoreApplication.translate("MainWindow", u"navBtn", None))
        self.navMap.setText(QCoreApplication.translate("MainWindow", u"Map", None))
        self.navReports.setObjectName(QCoreApplication.translate("MainWindow", u"navBtn", None))
        self.navReports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.navDataset.setObjectName(QCoreApplication.translate("MainWindow", u"navBtn", None))
        self.navDataset.setText(QCoreApplication.translate("MainWindow", u"Dataset", None))
        self.navConfig.setObjectName(QCoreApplication.translate("MainWindow", u"navBtn", None))
        self.navConfig.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.ctaBtn.setText(QCoreApplication.translate("MainWindow", u"Analyze Data", None))
        self.heroEyebrow.setText(QCoreApplication.translate("MainWindow", u"\u25c9  MarineVision \u00b7 Underwater Intelligence", None))
        self.heroTitle.setText(QCoreApplication.translate("MainWindow", u"AI-Powered Sonar Detection & Mapping", None))
        self.heroSub.setText(QCoreApplication.translate("MainWindow", u"Real-time underwater debris detection using YOLOv8 trained on side-scan sonar imagery.", None))
        self.heroAnalyzeBtn.setObjectName(QCoreApplication.translate("MainWindow", u"heroPrimary", None))
        self.heroAnalyzeBtn.setText(QCoreApplication.translate("MainWindow", u"Analyze Sonar Data", None))
        self.heroMapBtn.setObjectName(QCoreApplication.translate("MainWindow", u"heroGhost", None))
        self.heroMapBtn.setText(QCoreApplication.translate("MainWindow", u"View Mission Map", None))
        self.s0v.setObjectName(QCoreApplication.translate("MainWindow", u"statVal", None))
        self.s0v.setText(QCoreApplication.translate("MainWindow", u"595", None))
        self.s0l.setObjectName(QCoreApplication.translate("MainWindow", u"statLabel", None))
        self.s0l.setText(QCoreApplication.translate("MainWindow", u"Sonar Frames", None))
        self.s1v.setObjectName(QCoreApplication.translate("MainWindow", u"statVal", None))
        self.s1v.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.s1l.setObjectName(QCoreApplication.translate("MainWindow", u"statLabel", None))
        self.s1l.setText(QCoreApplication.translate("MainWindow", u"Object Classes", None))
        self.s2v.setObjectName(QCoreApplication.translate("MainWindow", u"statVal", None))
        self.s2v.setText(QCoreApplication.translate("MainWindow", u"87.7%", None))
        self.s2l.setObjectName(QCoreApplication.translate("MainWindow", u"statLabel", None))
        self.s2l.setText(QCoreApplication.translate("MainWindow", u"Avg Confidence", None))
        self.s3v.setObjectName(QCoreApplication.translate("MainWindow", u"statVal", None))
        self.s3v.setText(QCoreApplication.translate("MainWindow", u"124ms", None))
        self.s3l.setObjectName(QCoreApplication.translate("MainWindow", u"statLabel", None))
        self.s3l.setText(QCoreApplication.translate("MainWindow", u"Inference Time", None))
        self.label.setObjectName(QCoreApplication.translate("MainWindow", u"sectionEyebrow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u25c9  Platform Capabilities", None))
        self.label1.setObjectName(QCoreApplication.translate("MainWindow", u"sectionTitle", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"What MarineVision can do", None))
        self.c0.setObjectName(QCoreApplication.translate("MainWindow", u"capCard", None))
        self.label2.setObjectName(QCoreApplication.translate("MainWindow", u"capTitle", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"Real-time Sonar Analysis", None))
        self.label3.setObjectName(QCoreApplication.translate("MainWindow", u"capDesc", None))
        self.label3.setText(QCoreApplication.translate("MainWindow", u"Process side-scan sonar with AI in under 200ms per frame.", None))
        self.c1.setObjectName(QCoreApplication.translate("MainWindow", u"capCard", None))
        self.label4.setObjectName(QCoreApplication.translate("MainWindow", u"capTitle", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"Multi-class Detection", None))
        self.label5.setObjectName(QCoreApplication.translate("MainWindow", u"capDesc", None))
        self.label5.setText(QCoreApplication.translate("MainWindow", u"Identify pipelines, shipwrecks, ghost nets, mines with YOLOv8.", None))
        self.c2.setObjectName(QCoreApplication.translate("MainWindow", u"capCard", None))
        self.label6.setObjectName(QCoreApplication.translate("MainWindow", u"capTitle", None))
        self.label6.setText(QCoreApplication.translate("MainWindow", u"Geospatial Mapping", None))
        self.label7.setObjectName(QCoreApplication.translate("MainWindow", u"capDesc", None))
        self.label7.setText(QCoreApplication.translate("MainWindow", u"Plot detections on maps with GPS-accurate coordinates.", None))
        self.c3.setObjectName(QCoreApplication.translate("MainWindow", u"capCard", None))
        self.label8.setObjectName(QCoreApplication.translate("MainWindow", u"capTitle", None))
        self.label8.setText(QCoreApplication.translate("MainWindow", u"Mission Reporting", None))
        self.label9.setObjectName(QCoreApplication.translate("MainWindow", u"capDesc", None))
        self.label9.setText(QCoreApplication.translate("MainWindow", u"Auto-generate PDF, CSV, JSON reports with detection metadata.", None))
        self.analyzeHeader.setObjectName(QCoreApplication.translate("MainWindow", u"pageHeader", None))
        self.label10.setObjectName(QCoreApplication.translate("MainWindow", u"pageEyebrow", None))
        self.label10.setText(QCoreApplication.translate("MainWindow", u"\u25c9  Analysis Pipeline", None))
        self.label11.setObjectName(QCoreApplication.translate("MainWindow", u"pageTitle", None))
        self.label11.setText(QCoreApplication.translate("MainWindow", u"Analyze Sonar Data", None))
        self.label12.setObjectName(QCoreApplication.translate("MainWindow", u"pageSub", None))
        self.label12.setText(QCoreApplication.translate("MainWindow", u"Load a sonar image or mission log and run AI detection.", None))
        self.runDetectionBtn.setObjectName(QCoreApplication.translate("MainWindow", u"btnPrimary", None))
        self.runDetectionBtn.setText(QCoreApplication.translate("MainWindow", u"Run Detection", None))
        self.label13.setText(QCoreApplication.translate("MainWindow", u"Sonar canvas and detection results shown here.", None))
        self.label13.setStyleSheet(QCoreApplication.translate("MainWindow", u"color:#6070a0;font-size:14px;", None))
        self.mapHeader.setObjectName(QCoreApplication.translate("MainWindow", u"pageHeader", None))
        self.label14.setObjectName(QCoreApplication.translate("MainWindow", u"pageEyebrow", None))
        self.label14.setText(QCoreApplication.translate("MainWindow", u"\u25c9  Geospatial View", None))
        self.label15.setObjectName(QCoreApplication.translate("MainWindow", u"pageTitle", None))
        self.label15.setText(QCoreApplication.translate("MainWindow", u"Mission Map", None))
        self.label16.setObjectName(QCoreApplication.translate("MainWindow", u"pageSub", None))
        self.label16.setText(QCoreApplication.translate("MainWindow", u"View detections on a geospatial map with sonar tracks.", None))
        self.label17.setText(QCoreApplication.translate("MainWindow", u"[ Integrate Folium or QWebEngineView here ]", None))
        self.label17.setStyleSheet(QCoreApplication.translate("MainWindow", u"color:#6070a0;font-size:14px;", None))
        self.reportsHeader.setObjectName(QCoreApplication.translate("MainWindow", u"pageHeader", None))
        self.label18.setObjectName(QCoreApplication.translate("MainWindow", u"pageEyebrow", None))
        self.label18.setText(QCoreApplication.translate("MainWindow", u"\u25c9  Mission Output", None))
        self.label19.setObjectName(QCoreApplication.translate("MainWindow", u"pageTitle", None))
        self.label19.setText(QCoreApplication.translate("MainWindow", u"Mission Reports", None))
        self.label20.setObjectName(QCoreApplication.translate("MainWindow", u"pageSub", None))
        self.label20.setText(QCoreApplication.translate("MainWindow", u"View, filter and export detection results.", None))
        self.generateReportBtn.setObjectName(QCoreApplication.translate("MainWindow", u"btnPrimary", None))
        self.generateReportBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Report", None))
        self.datasetHeader.setObjectName(QCoreApplication.translate("MainWindow", u"pageHeader", None))
        self.label21.setObjectName(QCoreApplication.translate("MainWindow", u"pageEyebrow", None))
        self.label21.setText(QCoreApplication.translate("MainWindow", u"\u25c9  Data Management", None))
        self.label22.setObjectName(QCoreApplication.translate("MainWindow", u"pageTitle", None))
        self.label22.setText(QCoreApplication.translate("MainWindow", u"Dataset", None))
        self.label23.setObjectName(QCoreApplication.translate("MainWindow", u"pageSub", None))
        self.label23.setText(QCoreApplication.translate("MainWindow", u"Manage sonar frames, annotations, and model training data.", None))
        self.importDatasetBtn.setObjectName(QCoreApplication.translate("MainWindow", u"btnPrimary", None))
        self.importDatasetBtn.setText(QCoreApplication.translate("MainWindow", u"Import Dataset", None))
        self.datasetPlaceholder.setText(QCoreApplication.translate("MainWindow", u"Sonar dataset and annotation management will appear here.", None))
        self.datasetPlaceholder.setStyleSheet(QCoreApplication.translate("MainWindow", u"color:#6070a0;font-size:14px;", None))
        self.configHeader.setObjectName(QCoreApplication.translate("MainWindow", u"pageHeader", None))
        self.label24.setObjectName(QCoreApplication.translate("MainWindow", u"pageEyebrow", None))
        self.label24.setText(QCoreApplication.translate("MainWindow", u"\u25c9  System Settings", None))
        self.label25.setObjectName(QCoreApplication.translate("MainWindow", u"pageTitle", None))
        self.label25.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.label26.setObjectName(QCoreApplication.translate("MainWindow", u"pageSub", None))
        self.label26.setText(QCoreApplication.translate("MainWindow", u"Configure model, confidence threshold, and mission settings.", None))
        self.configPlaceholder.setText(QCoreApplication.translate("MainWindow", u"Model and mission configuration options will appear here.", None))
        self.configPlaceholder.setStyleSheet(QCoreApplication.translate("MainWindow", u"color:#6070a0;font-size:14px;", None))
    # retranslateUi

