# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 331)
        font = QtGui.QFont()
        font.setPointSize(9)
        Dialog.setFont(font)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 110, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("\n"
"   border-style:solid;\n"
"    border-width:0pz 0px 2px 0px;\n"
"    border-color:rgb(0, 205, 205);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 160, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 160, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("\n"
"   border-style:solid;\n"
"    border-width:0pz 0px 2px 0px;\n"
"    border-color:rgb(0, 205, 205);\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"   border-style:solid;\n"
"    border-width:0pz 0px 5px 0px;\n"
"    border-color:rgb(0, 205, 205);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   border-style:solid;\n"
"    border-width:0px 0px 2px 0px;\n"
"    border-color:rgb(0, 205, 205);\n"
"}\n"
"    \n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 240, 91, 31))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"   border-style:solid;\n"
"    border-width:0pz 0px 5px 0px;\n"
"    border-color:rgb(0, 205, 205);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   border-style:solid;\n"
"    border-width:0px 0px 2px 0px;\n"
"    border-color:rgb(0, 205, 205);\n"
"}\n"
"    \n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButton, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.lineEdit)
        Dialog.setTabOrder(self.lineEdit, self.pushButton_2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "USER:"))
        self.label_2.setText(_translate("Dialog", "BANJ-SOUCE LOGIN"))
        self.label_3.setText(_translate("Dialog", "PASSWORD:"))
        self.pushButton.setText(_translate("Dialog", "LOGIN"))
        self.pushButton_2.setText(_translate("Dialog", "CANCEL"))
