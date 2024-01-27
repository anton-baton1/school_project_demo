from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication

from go_to_test_page_ui import Ui_Form

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class GoToTestForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.go_to_test_btn.clicked.connect(self.go_to_test)
        self.back_btn.clicked.connect(self.back)

    def go_to_test(self):
        self.parent().parent().parent().test_form.first_test()
        self.parent().setCurrentIndex(5)

    def back(self):
        self.parent().setCurrentIndex(3)
