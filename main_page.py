from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap

from main_page_ui import Ui_Form

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MainForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.pixmap = QPixmap("Morphological_Maven.png")
        # self.label.setPixmap(self.pixmap)
        self.main_enter_btn.clicked.connect(self.open_enter_page)
        self.anonym_enter_btn.clicked.connect(self.open_analyze_page)
        self.pixmap = QPixmap("genius.png")
        self.image.setPixmap(self.pixmap)

    def open_enter_page(self):
        self.parent().setCurrentIndex(1)

    def open_analyze_page(self):
        self.parent().setCurrentIndex(3)
