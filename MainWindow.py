# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 270)
        MainWindow.setMinimumSize(QtCore.QSize(600, 270))
        MainWindow.setMaximumSize(QtCore.QSize(600, 270))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Symbol = QtWidgets.QLineEdit(self.centralwidget)
        self.Symbol.setGeometry(QtCore.QRect(122, 18, 113, 25))
        self.Symbol.setObjectName("Symbol")
        self.lblSymbol = QtWidgets.QLabel(self.centralwidget)
        self.lblSymbol.setGeometry(QtCore.QRect(12, 20, 105, 19))
        self.lblSymbol.setObjectName("lblSymbol")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(326, 22, 261, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icon.png"))
        self.label_2.setObjectName("label_2")
        self.pushButtonStockdata = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStockdata.setGeometry(QtCore.QRect(12, 56, 221, 27))
        self.pushButtonStockdata.setObjectName("pushButtonStockdata")
        self.lblStockdata = QtWidgets.QLabel(self.centralwidget)
        self.lblStockdata.setGeometry(QtCore.QRect(16, 102, 277, 143))
        self.lblStockdata.setText("")
        self.lblStockdata.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblStockdata.setObjectName("lblStockdata")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock data"))
        self.Symbol.setText(_translate("MainWindow", "KO"))
        self.lblSymbol.setText(_translate("MainWindow", "Stock symbol"))
        self.pushButtonStockdata.setText(_translate("MainWindow", "Retrieve stock data"))

