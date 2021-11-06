import sqlite3

from PyQt5 import uic, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow


class Update_form(QMainWindow):
    def __init__(self, clear, names):
        super().__init__()
        uic.loadUi('designs/Update.ui', self)  # TODO ПОДКЛЮЧЕНИЕ К ДИЗАЙНУ
        self.update_inf.clicked.connect(self.update_info)
        self.name = names

        # TODO Styles
        self.info_plain.setStyleSheet('color: #AFEEEE;'
                                      "background-image:"
                                      " url(background-image/back_2.jpg);"
                                      "border-radius: 10px"
                                      )
        self.update_inf.setStyleSheet(
            "QPushButton {background-image: url(background-image/select_2.jpg);"
            " border-radius: 10px; color: rgb(255, 255, 255);}")
        self.update_inf.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def update_info(self):  # TODO ОБНОВЛЕНИЕ ИНФОРМАЦИИИ ПРО ЯЗЫК
        con = sqlite3.connect('language.db')
        cur = con.cursor()

        # TODO ПОЛУЧЕНИЕ ИНФОРМАЦИИ ИЗ БД
        result = cur.execute(f"""SELECT language.History 
                 from language
                        WHERE language.id =
                         (SELECT id_languages.id FROM id_languages 
                        WHERE Language = '{self.name}')""").fetchall()
        information = result[0][0]
        dop_information = self.info_plain.toPlainText()
        # TODO ИНФОРМАЦИЯ ПРО ЯЗЫК, КОТОРЫЙ ВВЕЛ ПОЛЬЗОВАТЕЛЬ ДЛЯ ДОПОЛНЕНИЯ
        info = information + " " + dop_information
        cur.execute(f"""UPDATE language
        SET History = '{info}'
        WHERE id = (SELECT id FROM id_languages 
            WHERE Language = '{self.name}')
        """)
        con.commit()
        con.close()  # TODO ЗАКРЫТИЕ БД
