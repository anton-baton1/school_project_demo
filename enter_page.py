from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication

from errors import NotFoundLoginError, WrongPasswordError
from enter_page_ui import Ui_Form

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

user_ID_1 = None


class EnterForm(QWidget, Ui_Form):
    def __init__(self, data_base):
        super().__init__()
        self.setupUi(self)
        self.data_base = data_base
        self.enter_btn.clicked.connect(self.enter_user)
        self.registration_btn.clicked.connect(self.open_registration_page)
        self.show_password_btn.setStyleSheet(
            "background-color:transparent;background-image: url(hide.png)")
        self.show_password_btn.clicked.connect(self.show_password)
        self.home_btn.clicked.connect(self.home)
        self.change_password_btn.clicked.connect(self.change_password)


    def enter_user(self):
        global user_ID_1
        login, password = self.login_line.text(), self.password_line.text()
        try:
            if not self.data_base.cursor().execute("SELECT login FROM users WHERE login = ?", (login,)).fetchone():
                raise NotFoundLoginError
            if password != \
                    self.data_base.cursor().execute("SELECT password FROM users WHERE login = ?", (login,)).fetchone()[
                        0]:
                raise WrongPasswordError
            self.parent().setCurrentIndex(3)
            self.login_line.setText("")
            self.password_line.setText("")
            user_ID_1 = \
                self.data_base.cursor().execute("SELECT user_ID FROM users WHERE login = ?", (login,)).fetchone()[0]
        except NotFoundLoginError:
            self.error_password.setText("")
            self.error_login.setText("Пользователя с таким логином не существует")
        except WrongPasswordError:
            self.error_login.setText("")
            self.error_password.setText("Неверный пароль")

    def open_registration_page(self):
        self.parent().setCurrentIndex(2)

    def show_password(self):
        if self.password_line.echoMode() == 2:
            self.password_line.setEchoMode(0)
            self.show_password_btn.setStyleSheet(
                "background-color:transparent;background-image: url(show.png)")
        else:
            self.password_line.setEchoMode(2)
            self.show_password_btn.setStyleSheet(
                "background-color:transparent;background-image: url(hide.png)")

    def home(self):
        self.parent().setCurrentIndex(0)

    def change_password(self):
        self.parent().setCurrentIndex(7)
