# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Translate_custom.ui'
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
        self.centralwidget.setObjectName("centralwidget")
        self.main_Button = QtWidgets.QPushButton(self.centralwidget)
        self.main_Button.setGeometry(QtCore.QRect(21, 11, 81, 32))
        self.main_Button.setObjectName("main_Button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 15, 208, 18))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(21, 53, 646, 400))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_1 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_1.setObjectName("textEdit_1")
        self.horizontalLayout_2.addWidget(self.textEdit_1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Lang_comboBox = QtWidgets.QComboBox(self.widget)
        self.Lang_comboBox.setObjectName("Lang_comboBox")
        self.verticalLayout_2.addWidget(self.Lang_comboBox)
        self.translate_Button_2 = QtWidgets.QPushButton(self.widget)
        self.translate_Button_2.setObjectName("translate_Button_2")
        self.verticalLayout_2.addWidget(self.translate_Button_2)
        self.clear_Button_2 = QtWidgets.QPushButton(self.widget)
        self.clear_Button_2.setObjectName("clear_Button_2")
        self.verticalLayout_2.addWidget(self.clear_Button_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_4.setReadOnly(True)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.horizontalLayout_2.addWidget(self.plainTextEdit_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout.addWidget(self.textEdit_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.translate_Button = QtWidgets.QPushButton(self.widget)
        self.translate_Button.setObjectName("translate_Button")
        self.verticalLayout.addWidget(self.translate_Button)
        self.clear_Button = QtWidgets.QPushButton(self.widget)
        self.clear_Button.setObjectName("clear_Button")
        self.verticalLayout.addWidget(self.clear_Button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.horizontalLayout.addWidget(self.plainTextEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "momofish-Translate"))
        self.main_Button.setText(_translate("MainWindow", "?????????"))
        self.label.setText(_translate("MainWindow", "????????????????????????????????????????????????"))
        self.translate_Button_2.setText(_translate("MainWindow", "Translate"))
        self.clear_Button_2.setText(_translate("MainWindow", "Clear"))
        self.translate_Button.setText(_translate("MainWindow", "Translate"))
        self.clear_Button.setText(_translate("MainWindow", "Clear"))
