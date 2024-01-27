# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enter_page_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 555)
        font = QtGui.QFont()
        font.setPointSize(3)
        Form.setFont(font)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.password_line = QtWidgets.QLineEdit(Form)
        self.password_line.setGeometry(QtCore.QRect(220, 270, 210, 41))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(11)
        self.password_line.setFont(font)
        self.password_line.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:10px;font-family:\"Object Sans Heavy\";border:3px solid #FFD60A;")
        self.password_line.setText("")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.login_line = QtWidgets.QLineEdit(Form)
        self.login_line.setGeometry(QtCore.QRect(220, 190, 210, 41))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(11)
        self.login_line.setFont(font)
        self.login_line.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:10px;font-family:\"Object Sans Heavy\";border:3px solid #FFD60A;")
        self.login_line.setObjectName("login_line")
        self.enter_label = QtWidgets.QLabel(Form)
        self.enter_label.setGeometry(QtCore.QRect(0, 80, 650, 31))
        self.enter_label.setMinimumSize(QtCore.QSize(650, 0))
        font = QtGui.QFont()
        font.setFamily("Donpoligrafbum")
        font.setPointSize(20)
        self.enter_label.setFont(font)
        self.enter_label.setStyleSheet("background: transparent; font-family:\"Donpoligrafbum\";color:#000814")
        self.enter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_label.setObjectName("enter_label")
        self.enter_btn = QtWidgets.QPushButton(Form)
        self.enter_btn.setGeometry(QtCore.QRect(240, 350, 170, 41))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(10)
        self.enter_btn.setFont(font)
        self.enter_btn.setStyleSheet("color:#FFFFFF;background:#001D3D;border-radius:15px;font-family:\"Object Sans Heavy\"")
        self.enter_btn.setObjectName("enter_btn")
        self.error_password = QtWidgets.QLabel(Form)
        self.error_password.setGeometry(QtCore.QRect(225, 315, 201, 25))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(7)
        self.error_password.setFont(font)
        self.error_password.setStyleSheet("color: #003566;font-family:\"Object Sans Heavy\";background:transparent\n"
"")
        self.error_password.setText("")
        self.error_password.setWordWrap(True)
        self.error_password.setIndent(-1)
        self.error_password.setObjectName("error_password")
        self.registration_btn = QtWidgets.QPushButton(Form)
        self.registration_btn.setGeometry(QtCore.QRect(259, 400, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.registration_btn.setFont(font)
        self.registration_btn.setStyleSheet("background: #FFD60A; color:#003566; font-family:\"Object Sans Heavy\";border-radius:10;text-decoration:none")
        self.registration_btn.setObjectName("registration_btn")
        self.error_login = QtWidgets.QLabel(Form)
        self.error_login.setGeometry(QtCore.QRect(225, 235, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(7)
        self.error_login.setFont(font)
        self.error_login.setStyleSheet("color: #003566;font-family:\"Object Sans Heavy\";background:transparent;")
        self.error_login.setText("")
        self.error_login.setWordWrap(True)
        self.error_login.setObjectName("error_login")
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
        self.change_password_btn = QtWidgets.QPushButton(Form)
        self.change_password_btn.setGeometry(QtCore.QRect(270, 440, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Object Sans Heavy")
        font.setPointSize(8)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.change_password_btn.setFont(font)
        self.change_password_btn.setStyleSheet("background: #FFD60A; color:#003566; font-family:\"Object Sans Heavy\";border-radius:10;text-decoration:none")
        self.change_password_btn.setObjectName("change_password_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.password_line.setPlaceholderText(_translate("Form", "Введите пароль"))
        self.login_line.setPlaceholderText(_translate("Form", "Введите логин"))
        self.enter_label.setText(_translate("Form", "ВХОД"))
        self.enter_btn.setText(_translate("Form", "ВОЙТИ"))
        self.registration_btn.setText(_translate("Form", "Регистрация"))
        self.home_btn.setText(_translate("Form", "← На главную"))
        self.change_password_btn.setText(_translate("Form", "Забыли пароль?"))