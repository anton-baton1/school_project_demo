import pymorphy3
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication

from analyzer_page_ui import Ui_Form

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class AnalyzerForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tag_dict = {'NOUN': 'существительное',
                         'ADJF': 'полное прилагательное',
                         'ADJS': 'краткое прилагательное',
                         'COMP': 'компаратив',
                         'VERB': 'глагол',
                         'INFN': 'глагол',
                         'PRTF': 'полное причастие',
                         'PRTS': 'краткое причастие',
                         'GRND': 'деепричастие',
                         'NUMR': 'числительное',
                         'ADVB': 'наречие',
                         'NPRO': 'местоимение',
                         'PRED': 'предикатив',
                         'PREP': 'предлог',
                         'CONJ': 'союз',
                         'PRCL': 'частица',
                         'INTJ': 'междометие',
                         'anim': 'одушевлённое',
                         'inan': 'неодушевлённое',
                         'masc': 'мужской род',
                         'femn': 'женский род',
                         'neut': 'средний род',
                         'ms-f': 'общий род',
                         'sing': 'единственное число',
                         'plur': 'множественное число',
                         'Sgtm': 'единственное число',
                         'Pltm': 'множественное число',
                         'Fixd': 'неизменяемое',
                         'nomn': 'именительный падеж',
                         'gent': 'родительный падеж',
                         'datv': 'дательный падеж',
                         'accs': 'винительный падеж',
                         'ablt': 'творительный падеж',
                         'loct': 'предложный падеж',
                         'Supr': 'превосходная степень',
                         'Qual': 'качественное',
                         'Anum': 'порядковое',
                         'Poss': 'притяжательное',
                         'perf': 'совершенный вид',
                         'impf': 'несовершенный вид',
                         'tran': 'переходный',
                         'intr': 'непереходный',
                         'Impe': 'безличный',
                         'Refl': 'возвратный',
                         '1per': '1-ое лицо',
                         '2per': '2-ое лицо',
                         '3per': '3-е лицо',
                         'pres': 'настоящее время',
                         'past': 'прошедшее время',
                         'futr': 'будущее время',
                         'indc': 'изъявительное наклонение',
                         'impr': 'повелительное наклонение',
                         'actv': 'действительный залог',
                         'pssv': 'страдательный залог',
                         'Coll': 'собирательное',
                         'Erro': 'опечатка'
                         }
        self.output.setReadOnly(True)
        self.analyze_btn.clicked.connect(self.analyze)
        self.clear_btn.clicked.connect(self.clear)
        self.test_btn.clicked.connect(self.test)
        self.home_btn.clicked.connect(self.home)

    def analyze(self):
        word = self.word_edit.text().strip()
        morph = pymorphy3.MorphAnalyzer().parse(word)
        flag = False

        if word.isalpha():
            self.output.setPlainText(f"{word.capitalize()}:\n")
            parsers = [i for i in morph if all(
                [True if j not in ["Surn", "Name", "Patr" "UNKN"] else False for j in
                 str(i.tag).replace(" ", ",").split(",")])]
            for q, k in enumerate(parsers):
                if str(k.methods_stack[0][0]) == "DictionaryAnalyzer()":
                    parser = str(k.tag).replace(" ", ",").split(",")
                    s = [self.tag_dict[j] for j in parser if j in self.tag_dict]
                    s.insert(1, f"н.ф - {k.normal_form}")
                    self.output.setPlainText(f'{self.output.toPlainText()}{q + 1}) {", ".join(s)}\n\n')
                    flag = True
            print(*parsers, sep="\n")
        if not word.isalpha() or not flag:
            self.output.setPlainText("Некорректный ввод")

    def clear(self):
        self.output.setPlainText("")

    def test(self):
        self.parent().setCurrentIndex(4)

    def home(self):
        self.parent().setCurrentIndex(0)
