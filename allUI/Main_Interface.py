# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 467)
        MainWindow.setMinimumSize(QtCore.QSize(670, 467))
        MainWindow.setMaximumSize(QtCore.QSize(670, 467))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(670, 422))
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(130, 20, 51, 381))
        self.line.setTabletTracking(False)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(180, 22, 107, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_time.setFont(font)
        self.label_time.setScaledContents(True)
        self.label_time.setObjectName("label_time")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(180, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_date.setFont(font)
        self.label_date.setScaledContents(True)
        self.label_date.setObjectName("label_date")
        self.label_day_wea = QtWidgets.QLabel(self.centralwidget)
        self.label_day_wea.setGeometry(QtCore.QRect(390, 10, 101, 18))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        self.label_day_wea.setFont(font)
        self.label_day_wea.setAlignment(QtCore.Qt.AlignCenter)
        self.label_day_wea.setObjectName("label_day_wea")
        self.label_day_wea_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_day_wea_pic.setGeometry(QtCore.QRect(390, 30, 101, 101))
        self.label_day_wea_pic.setText("")
        self.label_day_wea_pic.setScaledContents(True)
        self.label_day_wea_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_day_wea_pic.setObjectName("label_day_wea_pic")
        self.label_day_tem = QtWidgets.QLabel(self.centralwidget)
        self.label_day_tem.setGeometry(QtCore.QRect(390, 140, 101, 16))
        self.label_day_tem.setText("")
        self.label_day_tem.setAlignment(QtCore.Qt.AlignCenter)
        self.label_day_tem.setObjectName("label_day_tem")
        self.label_night_wea = QtWidgets.QLabel(self.centralwidget)
        self.label_night_wea.setGeometry(QtCore.QRect(530, 10, 101, 18))
        self.label_night_wea.setText("")
        self.label_night_wea.setAlignment(QtCore.Qt.AlignCenter)
        self.label_night_wea.setObjectName("label_night_wea")
        self.label_night_wea_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_night_wea_pic.setGeometry(QtCore.QRect(530, 30, 101, 101))
        self.label_night_wea_pic.setText("")
        self.label_night_wea_pic.setScaledContents(True)
        self.label_night_wea_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_night_wea_pic.setObjectName("label_night_wea_pic")
        self.label_night_tem = QtWidgets.QLabel(self.centralwidget)
        self.label_night_tem.setGeometry(QtCore.QRect(530, 140, 101, 16))
        self.label_night_tem.setText("")
        self.label_night_tem.setAlignment(QtCore.Qt.AlignCenter)
        self.label_night_tem.setObjectName("label_night_tem")
        self.City_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.City_comboBox.setGeometry(QtCore.QRect(290, 10, 104, 26))
        self.City_comboBox.setCurrentText("")
        self.City_comboBox.setObjectName("City_comboBox")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 122, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout_2.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 180, 481, 221))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.layoutWidget.raise_()
        self.line.raise_()
        self.label_time.raise_()
        self.label_date.raise_()
        self.label_day_wea.raise_()
        self.label_day_wea_pic.raise_()
        self.label_day_tem.raise_()
        self.label_night_wea.raise_()
        self.label_night_wea_pic.raise_()
        self.label_night_tem.raise_()
        self.City_comboBox.raise_()
        self.plainTextEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "momofish"))
        self.label_time.setText(_translate("MainWindow", "00:00:00"))
        self.label_date.setText(_translate("MainWindow", "0000-00-00"))
        self.label_day_wea.setText(_translate("MainWindow", "请选择城市"))
        self.label.setText(_translate("MainWindow", "主界面"))
        self.pushButton_1.setText(_translate("MainWindow", "翻译工具"))
        self.pushButton_2.setText(_translate("MainWindow", "计算器"))
        self.pushButton_3.setText(_translate("MainWindow", "OCR文字识别"))
        self.pushButton_4.setText(_translate("MainWindow", "工具3号"))
        self.pushButton_5.setText(_translate("MainWindow", "工具4号"))
        self.pushButton_6.setText(_translate("MainWindow", "工具5号"))
        self.pushButton_7.setText(_translate("MainWindow", "工具6号"))
        self.pushButton_8.setText(_translate("MainWindow", "工具7号"))
        self.pushButton_9.setText(_translate("MainWindow", "工具8号"))
        self.pushButton_10.setText(_translate("MainWindow", "定制化"))