# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration_page_widget.ui'
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
        Form.setMinimumSize(QtCore.QSize(650, 550))
        font = QtGui.QFont()
        font.setPointSize(6)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 120, 650, 31))
        font = QtGui.QFont()
        font.setFamily("Donpoligrafbum")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent; font-family:\"Donpoligrafbum\";color:#000814")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.login_line = QtWidgets.QLineEdit(Form)
        self.login_line.setGeometry(QtCore.QRect(220, 190, 210, 41))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(11)
        self.login_line.setFont(font)
        self.login_line.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:10px;font-family:\"Object Sans Heavy\";border:3px solid #FFD60A;")
        self.login_line.setObjectName("login_line")
        self.registration_btn = QtWidgets.QPushButton(Form)
        self.registration_btn.setGeometry(QtCore.QRect(240, 380, 170, 41))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(10)
        self.registration_btn.setFont(font)
        self.registration_btn.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:15px;font-family:\"Object Sans Heavy\";")
        self.registration_btn.setObjectName("registration_btn")
        self.password_line = QtWidgets.QLineEdit(Form)
        self.password_line.setGeometry(QtCore.QRect(220, 270, 210, 41))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(11)
        self.password_line.setFont(font)
        self.password_line.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:10px;font-family:\"Object Sans Heavy\";border:3px solid #FFD60A;")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.error_login = QtWidgets.QLabel(Form)
        self.error_login.setGeometry(QtCore.QRect(225, 235, 201, 25))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(7)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.error_login.setFont(font)
        self.error_login.setStyleSheet("color: #003566;font-family:\"Object Sans Heavy\";background:transparent;")
        self.error_login.setWordWrap(True)
        self.error_login.setObjectName("error_login")
        self.error_password = QtWidgets.QLabel(Form)
        self.error_password.setGeometry(QtCore.QRect(225, 315, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(7)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.error_password.setFont(font)
        self.error_password.setStyleSheet("color: #003566;font-family:\"Object Sans Heavy\";background:transparent;")
        self.error_password.setWordWrap(True)
        self.error_password.setObjectName("error_password")
        self.show_password_btn = QtWidgets.QPushButton(Form)
        self.show_password_btn.setGeometry(QtCore.QRect(385, 274, 33, 33))
        self.show_password_btn.setStyleSheet("")
        self.show_password_btn.setText("")
        self.show_password_btn.setObjectName("show_password_btn")
        self.home_btn = QtWidgets.QPushButton(Form)
        self.home_btn.setGeometry(QtCore.QRect(20, 520, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.home_btn.setFont(font)
        self.home_btn.setStyleSheet(" background: transparent;color:#001D3D;border:2px solid #003566;border-radius:5;text-decoration:none\n"
"\n"
"")
        self.home_btn.setObjectName("home_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "РЕГИСТРАЦИЯ"))
        self.login_line.setPlaceholderText(_translate("Form", "Придумайте логин"))
        self.registration_btn.setText(_translate("Form", "ЗАВЕРШИТЬ\n"
"РЕГИСТРАЦИЮ"))
        self.password_line.setPlaceholderText(_translate("Form", "Придумайте пароль"))
        self.error_login.setText(_translate("Form", "Логин может содержать цифры, буквы и символы \'_-@\'"))
        self.error_password.setText(_translate("Form", "Пароль должен содержать строчные и заглавные буквы, цифры, символы \'_-~@#%&(){}\'. Длина пароля должна быть не менее 8 символов"))
        self.home_btn.setText(_translate("Form", "← На главную"))