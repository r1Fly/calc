# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

# MADE BY R1FLY

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(353, 515)
        MainWindow.setStyleSheet("QPushButton{\n"
" background-color:white;\n"
" width:75px; \n"
" height:75px;\n"
" font-size:16px;\n"
" font-weight:bold;\n"
" text-align:center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 50, 352, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_minus.setStyleSheet("background-color:rgb(255, 165, 0)")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.gridLayout.addWidget(self.pushButton_minus, 2, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_multiply = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_multiply.setStyleSheet("background-color:rgb(255, 165, 0)")
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.gridLayout.addWidget(self.pushButton_multiply, 0, 3, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 4, 0, 1, 2)
        self.pushButton_plusorminus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_plusorminus.setObjectName("pushButton_plusorminus")
        self.gridLayout.addWidget(self.pushButton_plusorminus, 0, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton_delit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_delit.setStyleSheet("background-color:rgb(255, 165, 0)")
        self.pushButton_delit.setObjectName("pushButton_delit")
        self.gridLayout.addWidget(self.pushButton_delit, 1, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_equal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_equal.setStyleSheet("background-color:rgb(255, 165, 0);\n"
"")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.gridLayout.addWidget(self.pushButton_equal, 4, 3, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.pushButton_tochka = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_tochka.setObjectName("pushButton_tochka")
        self.gridLayout.addWidget(self.pushButton_tochka, 4, 2, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_plus.setStyleSheet("background-color:rgb(255, 165, 0)")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout.addWidget(self.pushButton_plus, 3, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_procent = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_procent.setObjectName("pushButton_procent")
        self.gridLayout.addWidget(self.pushButton_procent, 0, 2, 1, 1)
        self.pushButton_1.raise_()
        self.pushButton_4.raise_()
        self.pushButton_8.raise_()
        self.pushButton_5.raise_()
        self.pushButton_2.raise_()
        self.pushButton_9.raise_()
        self.pushButton_6.raise_()
        self.pushButton_3.raise_()
        self.pushButton_minus.raise_()
        self.pushButton_delit.raise_()
        self.pushButton_plus.raise_()
        self.pushButton_0.raise_()
        self.pushButton_multiply.raise_()
        self.pushButton_procent.raise_()
        self.pushButton_plusorminus.raise_()
        self.pushButton_clear.raise_()
        self.pushButton_tochka.raise_()
        self.pushButton_equal.raise_()
        self.pushButton_7.raise_()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 51))
        self.label.setStyleSheet("color: rgb(136, 138,133);\n"
"font: 75 italic 11pt \"Ubuntu Mono\";\n"
"font-size:23px;\n"
"font-weight:bold;")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_multiply.setText(_translate("MainWindow", "*"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_plusorminus.setText(_translate("MainWindow", "+/-"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_delit.setText(_translate("MainWindow", "/"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        self.pushButton_clear.setText(_translate("MainWindow", "C"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_tochka.setText(_translate("MainWindow", "."))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_procent.setText(_translate("MainWindow", "%"))
