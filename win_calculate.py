# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculate.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(661, 386)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(370, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 230, 121, 71))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_outputrezult = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_outputrezult.setGeometry(QtCore.QRect(380, 60, 251, 301))
        self.textBrowser_outputrezult.setObjectName("textBrowser_outputrezult")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(30, 100, 240, 24))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.spinBox_AI = QtWidgets.QSpinBox(self.splitter)
        self.spinBox_AI.setObjectName("spinBox_AI")
        self.spinBox_BI = QtWidgets.QSpinBox(self.splitter)
        self.spinBox_BI.setObjectName("spinBox_BI")
        self.spinBox_AO = QtWidgets.QSpinBox(self.splitter)
        self.spinBox_AO.setObjectName("spinBox_AO")
        self.spinBox_BO = QtWidgets.QSpinBox(self.splitter)
        self.spinBox_BO.setObjectName("spinBox_BO")
        self.spinBox_UI = QtWidgets.QSpinBox(self.splitter)
        self.spinBox_UI.setObjectName("spinBox_UI")
        self.spinBox_CO = QtWidgets.QSpinBox(self.splitter)
        self.spinBox_CO.setObjectName("spinBox_CO")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Кол-во сигналов"))
        self.label_2.setText(_translate("Dialog", "Перечень оборудования"))
        self.pushButton.setText(_translate("Dialog", "Рассчитать"))
        self.label_3.setText(_translate("Dialog", "AI  BI  AO  BO  UI  CO"))
