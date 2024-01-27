# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyzer_page_widget.ui'
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
        self.output = QtWidgets.QPlainTextEdit(Form)
        self.output.setGeometry(QtCore.QRect(20, 70, 611, 361))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(12)
        self.output.setFont(font)
        self.output.setStyleSheet("color:#FFFFFF;background:#000814;border-radius:10px;font-family:\"Object Sans Heavy\";border:3px solid #FFC300;")
        self.output.setPlainText("")
        self.output.setObjectName("output")
        self.word_edit = QtWidgets.QLineEdit(Form)
        self.word_edit.setGeometry(QtCore.QRect(20, 20, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(11)
        self.word_edit.setFont(font)
        self.word_edit.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:10px;font-family:\"Object Sans Heavy\";border:3px solid #FFC300;")
        self.word_edit.setObjectName("word_edit")
        self.analyze_btn = QtWidgets.QPushButton(Form)
        self.analyze_btn.setGeometry(QtCore.QRect(420, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(10)
        self.analyze_btn.setFont(font)
        self.analyze_btn.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:15px;font-family:\"Object Sans Heavy\"")
        self.analyze_btn.setObjectName("analyze_btn")
        self.clear_btn = QtWidgets.QPushButton(Form)
        self.clear_btn.setGeometry(QtCore.QRect(20, 460, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(10)
        self.clear_btn.setFont(font)
        self.clear_btn.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:15px;font-family:\"Object Sans Heavy\"")
        self.clear_btn.setObjectName("clear_btn")
        self.home_btn = QtWidgets.QPushButton(Form)
        self.home_btn.setGeometry(QtCore.QRect(20, 520, 95, 21))
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
        self.test_btn.setGeometry(QtCore.QRect(535, 520, 95, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.test_btn.setFont(font)
        self.test_btn.setStyleSheet(" background: transparent;color:#001D3D;border:2px solid #003566;border-radius:5;text-decoration:none\n"
"\n"
"")
        self.test_btn.setObjectName("test_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.word_edit.setPlaceholderText(_translate("Form", "Введите слово для морфологического разбора"))
        self.analyze_btn.setText(_translate("Form", "АНАЛИЗИРОВАТЬ"))
        self.clear_btn.setText(_translate("Form", "ОЧИСТИТЬ"))
        self.home_btn.setText(_translate("Form", "← На главную"))
        self.test_btn.setText(_translate("Form", "Пройти тест →"))