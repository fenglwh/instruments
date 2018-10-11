# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\fengl\Documents\GitHub\instruments\Source_Code\Python\ConductedTest\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1133, 982)
        self.list_case = QtWidgets.QListWidget(Dialog)
        self.list_case.setGeometry(QtCore.QRect(20, 80, 311, 691))
        self.list_case.setObjectName("list_case")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 360, 150, 46))
        self.pushButton.setObjectName("pushButton")
        self.list_to_run = QtWidgets.QListWidget(Dialog)
        self.list_to_run.setGeometry(QtCore.QRect(520, 80, 371, 691))
        self.list_to_run.setObjectName("list_to_run")
        self.button_run = QtWidgets.QPushButton(Dialog)
        self.button_run.setGeometry(QtCore.QRect(930, 150, 150, 46))
        self.button_run.setObjectName("button_run")
        self.button_clear = QtWidgets.QPushButton(Dialog)
        self.button_clear.setGeometry(QtCore.QRect(930, 220, 150, 46))
        self.button_clear.setObjectName("button_clear")
        self.button_delete = QtWidgets.QPushButton(Dialog)
        self.button_delete.setGeometry(QtCore.QRect(930, 300, 150, 46))
        self.button_delete.setObjectName("button_delete")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 108, 24))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(520, 30, 151, 31))
        self.label_2.setObjectName("label_2")
        self.line_path = QtWidgets.QLineEdit(Dialog)
        self.line_path.setGeometry(QtCore.QRect(30, 820, 871, 41))
        self.line_path.setObjectName("line_path")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 780, 108, 24))
        self.label_3.setObjectName("label_3")
        self.button_browse = QtWidgets.QPushButton(Dialog)
        self.button_browse.setGeometry(QtCore.QRect(930, 820, 150, 46))
        self.button_browse.setObjectName("button_browse")
        self.label_status = QtWidgets.QLabel(Dialog)
        self.label_status.setGeometry(QtCore.QRect(30, 930, 1061, 24))
        self.label_status.setObjectName("label_status")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(700, 20, 211, 41))
        self.comboBox.setObjectName("comboBox")
        self.button_save = QtWidgets.QPushButton(Dialog)
        self.button_save.setGeometry(QtCore.QRect(930, 20, 150, 46))
        self.button_save.setObjectName("button_save")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", ">"))
        self.button_run.setText(_translate("Dialog", "Run"))
        self.button_clear.setText(_translate("Dialog", "Clear Case"))
        self.button_delete.setText(_translate("Dialog", "Delete"))
        self.label.setText(_translate("Dialog", "Case"))
        self.label_2.setText(_translate("Dialog", "Case to run"))
        self.label_3.setText(_translate("Dialog", "Path"))
        self.button_browse.setText(_translate("Dialog", "Browse"))
        self.label_status.setText(_translate("Dialog", "Status"))
        self.button_save.setText(_translate("Dialog", "Save Case"))

