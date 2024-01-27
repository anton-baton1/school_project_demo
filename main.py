import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QHBoxLayout, QWidget

from analyzer_page import AnalyzerForm
from data_base import DataBase
from enter_page import EnterForm
from main_page import MainForm
from registration_page import RegistrationForm
from go_to_test_page import GoToTestForm
from test_page import TestForm
from result_test_page import ResultTestForm
from change_password_page import ChangePasswordForm

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morphological Maven")
        self.resize(650, 550)
        self.main_layout = QHBoxLayout(self)
        self.setLayout(self.main_layout)
        self.stack = QStackedWidget(self)

        self.main_layout.addWidget(self.stack)
        self.data_base = DataBase()

        self.main_form = MainForm()
        self.enter_form = EnterForm(self.data_base)
        self.registration_form = RegistrationForm(self.data_base)
        self.analyzer_form = AnalyzerForm()
        self.go_to_test_form = GoToTestForm()
        self.test_form = TestForm(self.data_base)
        self.result_test_form = ResultTestForm(self.data_base)
        self.change_password_from = ChangePasswordForm(self.data_base)

        self.stack.addWidget(self.main_form)
        self.stack.addWidget(self.enter_form)
        self.stack.addWidget(self.registration_form)
        self.stack.addWidget(self.analyzer_form)
        self.stack.addWidget(self.go_to_test_form)
        self.stack.addWidget(self.test_form)
        self.stack.addWidget(self.result_test_form)
        self.stack.addWidget(self.change_password_from)

        self.stack.setCurrentWidget(self.main_form)
        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
