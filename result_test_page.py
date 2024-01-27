import csv
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox

from errors import NoTestsForDate, AuthorizationError
from result_test_page_ui import Ui_Form

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class ResultTestForm(QWidget, Ui_Form):
    def __init__(self, data_base):
        super().__init__()
        self.setupUi(self)
        self.user_ID = None
        self.data_base = data_base
        self.pixmap = QPixmap("csv_file.png")
        self.image.setPixmap(self.pixmap)
        self.pushButton.clicked.connect(self.show_test_result)
        self.test_btn.clicked.connect(self.test)
        self.analyzer_btn.clicked.connect(self.analyzer)
        self.home_btn.clicked.connect(self.home)

    def show_test_result(self):
        from test_page import user_ID
        self.user_ID = user_ID
        try:
            if not self.user_ID:
                raise AuthorizationError
            date = "-".join(self.date_line.text().split("-")[::-1])
            tests_list = self.data_base.cursor().execute("SELECT * FROM tests WHERE user_ID = ? AND date = ?",
                                                         (self.user_ID, date,)).fetchall()
            if not tests_list:
                raise NoTestsForDate
            data = []
            for i in tests_list:
                answer = "Правильный" if i[3] else "Неправильный"
                s = {"ID теста": i[0],
                     "Слово для теста": i[2],
                     "Ответ": answer,
                     "Дата": i[4],
                     "Время": i[5]}
                data.append(s)
            filename = QFileDialog.getSaveFileName(self, "Save File", "text_result", "Csv Files (*.csv)")[0]
            print(filename)
            with open(filename, 'w+', newline='', encoding="utf-8") as file:
                writer = csv.DictWriter(
                    file, fieldnames=list(data[0].keys()),
                    delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
                writer.writeheader()
                for d in data:
                    writer.writerow(d)
            download_file_ok_message = QMessageBox(self)
            answer = download_file_ok_message.question(self, '', "Файл успешно загружен", QMessageBox.Ok)
        except NoTestsForDate:
            self.error_label.setText(f"Пройденных тестов за {self.date_line.text()} не найденно")
        except AuthorizationError:
            no_user_message = QMessageBox(self)
            answer = no_user_message.question(self, '', "Посмотреть результаты теста могут только авторизованные "
                                                        "пользователи", QMessageBox.Ok)

    def test(self):
        self.parent().setCurrentIndex(5)

    def analyzer(self):
        self.parent().setCurrentIndex(3)

    def home(self):
        self.parent().setCurrentIndex(0)
