# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result_test_page_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 550)
        self.result_label = QtWidgets.QLabel(Form)
        self.result_label.setGeometry(QtCore.QRect(0, 50, 651, 41))
        font = QtGui.QFont()
        font.setFamily("Donpoligrafbum")
        font.setPointSize(20)
        self.result_label.setFont(font)
        self.result_label.setStyleSheet("background: transparent; font-family:\"Donpoligrafbum\";color:#000814")
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName("result_label")
        self.date_line = QtWidgets.QLineEdit(Form)
        self.date_line.setGeometry(QtCore.QRect(230, 210, 191, 41))
        self.date_line.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:10px;font-family:\"Object Sans Heavy\";border:3px solid #FFD60A;")
        self.date_line.setReadOnly(False)
        self.date_line.setObjectName("date_line")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 410, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:15px;font-family:\"Object Sans Heavy\";")
        self.pushButton.setObjectName("pushButton")
        self.date_label = QtWidgets.QLabel(Form)
        self.date_label.setGeometry(QtCore.QRect(235, 180, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(9)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("color: #003566;font-family:\"Object Sans Heavy\";background:transparent;")
        self.date_label.setObjectName("date_label")
        self.error_label = QtWidgets.QLabel(Form)
        self.error_label.setGeometry(QtCore.QRect(235, 260, 181, 41))
        self.error_label.setStyleSheet("color: #003566;font-family:\"Object Sans Heavy\";background:transparent;")
        self.error_label.setText("")
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName("error_label")
        self.analyzer_btn = QtWidgets.QPushButton(Form)
        self.analyzer_btn.setGeometry(QtCore.QRect(270, 520, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.analyzer_btn.setFont(font)
        self.analyzer_btn.setStyleSheet(" background: transparent;color:#001D3D;border:2px solid #003566;border-radius:5;text-decoration:none\n"
"\n"
"")
        self.analyzer_btn.setObjectName("analyzer_btn")
        self.home_btn = QtWidgets.QPushButton(Form)
        self.home_btn.setGeometry(QtCore.QRect(530, 520, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.home_btn.setFont(font)
        self.home_btn.setStyleSheet(" background: transparent;color:#001D3D;border:2px solid #003566;border-radius:5;text-decoration:none\n"
"\n"
"")
        self.home_btn.setObjectName("home_btn")
        self.test_btn = QtWidgets.QPushButton(Form)
        self.test_btn.setGeometry(QtCore.QRect(20, 520, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.test_btn.setFont(font)
        self.test_btn.setStyleSheet(" background: transparent;color:#001D3D;border:2px solid #003566;border-radius:5;text-decoration:none\n"
"\n"
"")
        self.test_btn.setObjectName("test_btn")
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(275, 280, 100, 100))
        self.image.setText("")
        self.image.setObjectName("image")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.result_label.setText(_translate("Form", "РЕЗУЛЬТАТЫ"))
        self.date_line.setInputMask(_translate("Form", "99-99-9999;_"))
        self.date_line.setText(_translate("Form", "--"))
        self.date_line.setPlaceholderText(_translate("Form", "ДД-ММ-ГГГГ"))
        self.pushButton.setText(_translate("Form", "СКАЧАТЬ\n"
"РЕЗУЛЬТАТЫ"))
        self.date_label.setText(_translate("Form", "Укажите дату"))
        self.analyzer_btn.setText(_translate("Form", "← Разбор слов"))
        self.home_btn.setText(_translate("Form", "← На главную"))
        self.test_btn.setText(_translate("Form", "← Тест"))
