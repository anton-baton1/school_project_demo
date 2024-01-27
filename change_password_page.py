from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication

from change_password_page_ui import Ui_Form
from errors import NotFoundLoginError, WrongPasswordError, LenPasswordError, BigAlphaPasswordError, SymbolPasswordError, SmallAlphaPasswordError, \
    DigitPasswordError, AlphaPasswordError, SymbolLoginError, ExistLoginError
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class ChangePasswordForm(QWidget, Ui_Form):
    def __init__(self, data_base):
        super().__init__()
        self.setupUi(self)
        self.data_base = data_base
        self.back_btn.clicked.connect(self.back)
        self.show_password_btn.setStyleSheet(
            "background-color:transparent;background-image: url(hide.png)")
        self.show_password_btn.clicked.connect(self.show_password)
        self.change_password_btn.clicked.connect(self.change_password)

    def change_password(self):
        login, password = self.login_line.text(), self.password_line.text()
        alpha, digit, symbol = False, False, False
        try:
            if not self.data_base.cursor().execute("SELECT login FROM users WHERE login = ?", (login,)).fetchone():
                raise NotFoundLoginError
            for i in login:
                if not i.isalnum() and i not in "_-@":
                    raise SymbolLoginError
            if len(password) < 8:
                raise LenPasswordError
            for j in password:
                if j.isalpha():
                    alpha = True
                elif j.isdigit():
                    digit = True
                elif j not in "_-~@#%&(){}":
                    symbol = True
                if alpha and symbol and digit:
                    break
            if password.isupper():
                raise SmallAlphaPasswordError
            if password.islower():
                raise BigAlphaPasswordError
            if not digit:
                raise DigitPasswordError
            if symbol:
                raise SymbolPasswordError
            if not alpha:
                raise AlphaPasswordError
            self.data_base.cursor().execute("UPDATE users SET password = ? WHERE login = ?", (password, login,))
            self.data_base.connection().commit()
            self.parent().setCurrentIndex(1)
        except NotFoundLoginError:
            self.error_password.setText("")
            self.error_login.setText("Пользователя с таким логином не существует")

        except SymbolPasswordError:
            self.error_login.setText("")
            self.error_password.setText("Пароль может содержать только символы '_-~@#%&(){}'")
        except LenPasswordError:
            self.error_login.setText("")
            self.error_password.setText("Пароль должен содержать минимум 8 символов")
        except BigAlphaPasswordError:
            self.error_login.setText("")
            self.error_password.setText("Пароль должен содержать заглавные буквы")
        except SmallAlphaPasswordError:
            self.error_login.setText("")
            self.error_password.setText("Пароль должен содержать строчные буквы")
        except DigitPasswordError:
            self.error_login.setText("")
            self.error_password.setText("Пароль должен содержать цифры")
        except AlphaPasswordError:
            self.error_login.setText("")
            self.error_password.setText("Пароль должен содержать буквы")


    def back(self):
        self.parent().setCurrentIndex(1)


    def show_password(self):
        if self.password_line.echoMode() == 2:
            self.password_line.setEchoMode(0)
            self.show_password_btn.setStyleSheet(
                "background-color:transparent;background-image: url(show.png)")
        else:
            self.password_line.setEchoMode(2)
            self.show_password_btn.setStyleSheet(
                "background-color:transparent;background-image: url(hide.png)")
