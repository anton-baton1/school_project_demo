# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 549)
        Form.setStyleSheet("")
        self.anonym_enter_btn = QtWidgets.QPushButton(Form)
        self.anonym_enter_btn.setGeometry(QtCore.QRect(250, 310, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(10)
        self.anonym_enter_btn.setFont(font)
        self.anonym_enter_btn.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:15px;font-family:\"Object Sans Heavy\";")
        self.anonym_enter_btn.setObjectName("anonym_enter_btn")
        self.main_enter_btn = QtWidgets.QPushButton(Form)
        self.main_enter_btn.setGeometry(QtCore.QRect(250, 250, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(10)
        self.main_enter_btn.setFont(font)
        self.main_enter_btn.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:15px;font-family:\"Object Sans Heavy\";")
        self.main_enter_btn.setObjectName("main_enter_btn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 50, 651, 91))
        font = QtGui.QFont()
        font.setFamily("Donpoligrafbum")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent; font-family:\"Donpoligrafbum\";color:#000814")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(300, 400, 50, 50))
        self.image.setText("")
        self.image.setObjectName("image")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.anonym_enter_btn.setText(_translate("Form", "ВОЙТИ АНОНИМНО"))
        self.main_enter_btn.setText(_translate("Form", "ВОЙТИ"))
        self.label.setText(_translate("Form", "Morphological\n"
"Maven"))
