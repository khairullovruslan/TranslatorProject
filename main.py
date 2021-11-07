import sys
from PyQt5 import uic, QtCore, QtGui
import sqlite3
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow, QApplication
from translate import Translator
from SecondForm import SecondForm
from SelectLang_second import SecondForm_2
from Database import entering_data_into_a_table
import pyperclip as clipboard
import webbrowser
from PyQt5.QtCore import Qt


# TODO ИМПОРТ ТРЕБУЕМЫХ БИБЛИОТЕК И МОДУЛЕЙ

class Translate(QMainWindow):
    def __init__(self):
        super(Translate, self).__init__()
        # TODO ПОДКЛЮЧЕНИЕ К ДИЗАЙНУ
        uic.loadUi('designs/translate.ui', self)
        # TODO Styles
        self.languagebutton.setStyleSheet(
            "QPushButton {background-image: url(background-image/select_2.jpg);"
            " border-radius: 10px; color: rgb(255, 255, 255);}")
        self.languagebutton_second.setStyleSheet(
            "QPushButton {background-image: url(background-image/select_2.jpg);"
            " border-radius: 10px; color: rgb(255, 255, 255);}")
        self.text_reception.setStyleSheet('QPlainTextEdit {color: #AFEEEE;'
                                          "background-image:"
                                          " url(background-image/back_2.jpg);"
                                          "border-radius: 10px}"
                                          )
        self.text_output.setStyleSheet('color: #AFEEEE;'
                                       "background-image:"
                                       " url(background-image/back_2.jpg);"
                                       "border-radius: 10px"
                                       )
        self.footer.setStyleSheet("color: #ececec;")
        self.company_name.setStyleSheet("color: #ececec;")
        # TODO СОЗДАНИЕ ВСПЛЫВАЮЩИХ ОКОН
        self.copy_paste.setToolTip('Копировать')
        self.copy_paste_2.setToolTip('Копировать')
        self.contact_tg.setToolTip('Перейти')
        self.contact_vk.setToolTip('Перейти')
        self.contact_google.setToolTip('Перейти')
        self.translate_btn.setToolTip('Перевести')
        self.languagebutton_second.setToolTip('Выбрать язык')
        self.languagebutton.setToolTip('Выбрать язык')
        self.arrow_changes.setToolTip('Поменять местами')
        self.text_reception.setToolTip('Начните писать текст')

        # TODO ИЗМЕНЕИЕ КУРСОРА
        self.languagebutton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.languagebutton_second.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.arrow_changes.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.copy_paste.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.copy_paste_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.contact_tg.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.contact_vk.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.contact_google.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.translate_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        # TODO CONNECTING BUTTONS
        self.languagebutton.clicked.connect(self.open_second_form)
        self.languagebutton_second.clicked.connect(self.open_second_form1)
        self.copy_paste.clicked.connect(self.copy_paste_fun)
        self.translate_btn.clicked.connect(self.start)
        self.copy_paste_2.clicked.connect(self.copy_paste_fun_2)
        self.arrow_changes.clicked.connect(self.change)

        # TODO ОТКРЫТИЕ САЙТА ПРИ НАЖАТИИ НА КНОПКУ
        self.contact_vk.clicked.connect(
            lambda: webbrowser.open(
                'https://vk.com/im?peers=363207223_592456333'
                '_458503653_-97568278&sel=262014370'))
        self.contact_tg.clicked.connect(
            lambda: webbrowser.open('https://t.me/I_am_a_busy_person'))
        self.contact_google.clicked.connect(
            lambda: webbrowser.open('mailto: khairullov.ruslan@gmail.com'))
        # TODO ПЕРЕМЕННЫЕ
        self.from_what = 'Русский'  # TODO НА КАКОМ ЯЗЫКЕ ТЕКСТ
        self.in_what = 'Английский'  # TODO НА КАКОМ ХОТИМ ПОЛУЧИТЬ РЕЗУЛЬТАТ
        self.change_flag = False  # TODO FLAG ДЛЯ ПРОВЕРКИ СМЕНЫ ЯЗЫКОВ МЕЖДУ СОБОЙ
        # TODO СОЗДАНИЕ БД, ЕСЛИ ДАННЫЕ УЖЕ ЕСТЬ, ТО СОЗДАНИЕ ПРЕКРАЩАЕТСЯ
        try:
            entering_data_into_a_table()
        except sqlite3.IntegrityError:
            print('База данных уже создана')
        # TODO ДОБАВЛЕНИЕ ТЕКСТА ДЛЯ КНОПОК
        self.languagebutton.setText(self.from_what)
        self.languagebutton_second.setText(self.in_what)
        self.select_flag = False  # TODO FLAG ДЛЯ ПРОВЕРКИ ВЫБОРА ЯЗЫКА

    def start(self):  # TODO ВЫПОЛНЕНИЕ ПЕРЕВОДА # ОСНОВНАЯ ФУНКЦИЯ
        try:  # TODO ПРОВЕРКА НА ОТКРЫТИЕ ВТОРОГО ОКНА
            if self.second_form.select_lan():
                self.from_what = self.second_form.select_lan()

            if self.second_form1.select_lan():
                self.in_what = self.second_form1.select_lan()
        except AttributeError:  # TODO ЕСЛИ ОДНО ИЗ ОКОН НЕ БЫЛО ОТКРЫТО, ТО ЛОВИМ ИСКЛЮЧЕНИЕ
            try:
                if self.second_form1.select_lan():
                    self.in_what = self.second_form1.select_lan()
            except AttributeError:  # TODO И ТАК ДО КОНЦА
                try:
                    if self.second_form.select_lan():
                        self.in_what = self.second_form1.select_lan()
                        self.languagebutton.setText(self.from_what)
                        self.languagebutton_second.setText(self.in_what)

                except AttributeError:
                    pass
        if self.change_flag:  # TODO ПРОВЕРКА НА НАЖАТИЕ КНОПКИ CHANGE LANGUAGES
            self.change_flag = False
            first = self.from_what
            second = self.in_what
            self.from_what = second  # TODO СМЕНА ЯЗЫКОВ МЕЖДУ СОБОЙ
            self.in_what = first
            self.languagebutton.setText(self.from_what)  # TODO ВСТАВКА НАЗВАНИЙ
            # TODO ЯЗЫКОВ ПОСЛЕ ИЗМЕНЕНИЯ
            self.languagebutton_second.setText(self.in_what)
        else:
            self.languagebutton.setText(self.from_what)
            self.languagebutton_second.setText(self.in_what)
        text = self.text_reception.toPlainText()  # TODO ПОЛУЧЕНИЕ ТЕКСТА
        input_ = self.get_translate(
            self.from_what)  # TODO С КАКОГО ЯЗЫКА ПРОИСХОДИТ ПЕРЕВОД
        output_ = self.get_translate(
            self.in_what)  # TODO НА КАКОЙ ЯЗЫК ТРЕБУЕТСЯ ПЕРЕВЕСТИ
        translator = Translator(from_lang=input_,
                                to_lang=output_)  # TODO ПРОЦЕСС ПЕРЕВОДА
        w = translator.translate(text)
        self.text_output.setPlainText(w)  # TODO ВСТАВКА ТЕКСТА

    def open_second_form(self):  # TODO ОТКРЫТИЕ ВТОРОГО ОКНА
        self.second_form = SecondForm()
        self.second_form.setWindowIcon(QtGui.QIcon('icons/logo.png'))
        self.second_form.setFixedSize(800, 600)
        self.second_form.show()

    def open_second_form1(self):  # TODO ОТКРЫТИЕ ВТОРОГО ОКНА
        self.second_form1 = SecondForm_2()
        self.second_form1.setWindowIcon(QtGui.QIcon('icons/logo.png'))
        self.second_form1.setFixedSize(800, 600)
        self.second_form1.show()

    def get_translate(self, name):  # TODO ПОЛУЧЕНИЕ ТРЕБУЕМОГО ПОЛЬЗОВАТЕЛЕМ ЯЗЫКА

        con = sqlite3.connect('language.db')  # TODO ПОДКЛЮЧЕНИЕ К БД
        cur = con.cursor()
        result = cur.execute(f"""SELECT language.Translate from language
        WHERE language.id = (SELECT id_languages.id FROM id_languages 
        WHERE Language = '{name}')""").fetchall()
        lang = []
        for i in result:
            lang.append(i)
        con.close()
        return lang[0][0]  # TODO ПЕРЕДАЧА НАЗВАНИЯ

    def change(self):  # TODO ПРОЦЕСС ИЗМЕНЕНИЕ ЯЗЫКОМ МЕСТАМИ
        first = self.languagebutton.text()
        second = self.languagebutton_second.text()
        self.languagebutton.setText(second)
        self.languagebutton_second.setText(first)
        self.change_flag = True
        first_text = self.text_reception.toPlainText()  # TODO СМЕНА ТЕКСТОВ
        second_text = self.text_output.toPlainText()
        self.text_reception.setPlainText(second_text)
        self.text_output.setPlainText(first_text)

    def copy_paste_fun(
            self):  # TODO КОПИРОВАНИЕ В БУФЕР ОБМЕНА ПРИ ПОМОЩИ КНОПКИ
        clipboard.copy(self.text_reception.toPlainText())

    def copy_paste_fun_2(self):
        clipboard.copy(self.text_output.toPlainText())

    def keyPressEvent(self, event):  # TODO ПЕРЕВОД ТЕКСТА ПРИ НАЖАТИИ НА SHIFT
        if event.key() == Qt.Key_Shift:
            self.start()


def except_hook(cls, exception, traceback):  # TODO ПОИСК ОШИБОК
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':  # TODO ОТКРЫТИЕ ПРОГРАММЫ БЕЗ .EXE
    app = QApplication(sys.argv)

    wnd = Translate()
    wnd.setFixedSize(1275, 820)
    wnd.setWindowIcon(QtGui.QIcon('icons/logo.png'))
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
