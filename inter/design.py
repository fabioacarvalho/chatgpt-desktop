# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QTabWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"../../../../Downloads/DALL-E.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #2D3250;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 581))
        self.tabWidget.setMinimumSize(QSize(801, 581))
        self.tabWidget.setMaximumSize(QSize(801, 581))
        self.tabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget.setStyleSheet(u"background-color: #2D3250;\n"
"border: none;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"border: none;")
        self.groupBox = QGroupBox(self.home)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 771, 541))
        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 60, 751, 371))
        self.scrollArea.setStyleSheet(u"border-radius: 8px;\n"
"color: #FFFFFF;\n"
"border: 1px solid #424769;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 749, 369))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.message = QTextEdit(self.groupBox)
        self.message.setObjectName(u"message")
        self.message.setGeometry(QRect(10, 440, 671, 91))
        self.message.setStyleSheet(u"border-radius: 8px;\n"
"background-color: #424769;\n"
"color: #FFFFFF;")
        self.btnSend = QPushButton(self.groupBox)
        self.btnSend.setObjectName(u"btnSend")
        self.btnSend.setGeometry(QRect(690, 442, 75, 91))
        self.btnSend.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSend.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 20, 111, 21))
        self.label_6.setStyleSheet(u"color: #FFF;\n"
"font-size: 18px;")
        self.tabWidget.addTab(self.home, "")
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.label = QLabel(self.settings)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 10, 81, 41))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 18px;")
        self.label_2 = QLabel(self.settings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 51, 31))
        self.label_2.setStyleSheet(u"color: #FFF;\n"
"font-size: 12px;")
        self.name = QLineEdit(self.settings)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(110, 80, 651, 31))
        self.name.setStyleSheet(u"color: #FFF;\n"
"border: 2px solid #424769;\n"
"border-radius: 8px;\n"
"padding-left: 10px;")
        self.apiKey = QLineEdit(self.settings)
        self.apiKey.setObjectName(u"apiKey")
        self.apiKey.setGeometry(QRect(110, 140, 651, 31))
        self.apiKey.setStyleSheet(u"color: #FFF;\n"
"border: 2px solid #424769;\n"
"border-radius: 8px;\n"
"padding-left: 10px;")
        self.label_3 = QLabel(self.settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 140, 51, 31))
        self.label_3.setStyleSheet(u"color: #FFF;\n"
"font-size: 12px;")
        self.mode = QLineEdit(self.settings)
        self.mode.setObjectName(u"mode")
        self.mode.setEnabled(False)
        self.mode.setGeometry(QRect(110, 200, 651, 31))
        self.mode.setStyleSheet(u"color: #FFF;\n"
"border: 2px solid #424769;\n"
"border-radius: 8px;\n"
"padding-left: 10px;")
        self.mode.setReadOnly(True)
        self.label_4 = QLabel(self.settings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 200, 51, 31))
        self.label_4.setStyleSheet(u"color: #FFF;\n"
"font-size: 12px;")
        self.url = QLineEdit(self.settings)
        self.url.setObjectName(u"url")
        self.url.setEnabled(False)
        self.url.setGeometry(QRect(110, 260, 651, 31))
        self.url.setStyleSheet(u"color: #FFF;\n"
"border: 2px solid #424769;\n"
"border-radius: 8px;\n"
"padding-left: 10px;")
        self.url.setReadOnly(True)
        self.label_5 = QLabel(self.settings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 260, 51, 31))
        self.label_5.setStyleSheet(u"color: #FFF;\n"
"font-size: 12px;")
        self.btnSave = QPushButton(self.settings)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setGeometry(QRect(674, 340, 81, 41))
        self.btnSave.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSave.setStyleSheet(u"background-color: #55AA7F;\n"
"border-radius: 8px;\n"
"color: #FFF;")
        self.label_7 = QLabel(self.settings)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 440, 161, 31))
        self.label_7.setStyleSheet(u"color: #FFF;\n"
"font-size: 12px;")
        self.label_8 = QLabel(self.settings)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 480, 161, 31))
        self.label_8.setStyleSheet(u"color: #FFF;\n"
"font-size: 12px;")
        self.label_9 = QLabel(self.settings)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 520, 161, 31))
        self.label_9.setStyleSheet(u"color: #FFF;\n"
"font-size: 12px;")
        self.btnLoad = QPushButton(self.settings)
        self.btnLoad.setObjectName(u"btnLoad")
        self.btnLoad.setGeometry(QRect(580, 340, 81, 41))
        self.btnLoad.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLoad.setStyleSheet(u"background-color: #676F9D;\n"
"border-radius: 8px;\n"
"color: #FFF;")
        self.tabWidget.addTab(self.settings, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ChatGPT", None))
        self.groupBox.setTitle("")
        self.message.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Message ChatGPT", None))
        self.btnSend.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ChatGPT 3.5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"API Key:", None))
        self.mode.setText(QCoreApplication.translate("MainWindow", u"gtp-3.5-turbo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"GPT Model:", None))
        self.url.setText(QCoreApplication.translate("MainWindow", u"https://api.openai.com/v1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Developed: F\u00e1bio Carvalho", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TikTok: @ofabioacarvalho", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9ditos: OpenAI", None))
        self.btnLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

