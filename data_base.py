import sqlite3

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect("Morphological_Maven.sqlite3")
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_ID  INTEGER PRIMARY KEY AUTOINCREMENT
                     NOT NULL
                     UNIQUE
                     REFERENCES tests (user_ID),
    login    TEXT    UNIQUE
                     NOT NULL,
    password TEXT    NOT NULL
);
""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS tests (
    test_ID     INTEGER PRIMARY KEY AUTOINCREMENT
                        UNIQUE
                        NOT NULL,
    user_ID     INTEGER NOT NULL,
    test_word   TEXT    NOT NULL,
    test_result INTEGER NOT NULL,
    date        TEXT    NOT NULL,
    time        TEXT    NOT NULL
);
""")
        self.con.commit()

    def cursor(self):
        return self.cur

    def connection(self):
        return self.con
