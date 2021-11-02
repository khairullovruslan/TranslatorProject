import sqlite3

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QMainWindow


class History_from(QMainWindow):
    def __init__(self, clear, names):
        super().__init__()
        uic.loadUi('designs/History.ui', self)  # TODO ПОДКЛЮЧЕНИЕ К ДИЗАЙНУ

        # TODO ПОДКЛЮЧЕНИЕ К БД. ПОЛУЧЕНИЕ ДАННЫХ
        con = sqlite3.connect('language.db')
        cur = con.cursor()
        self.name = names
        result = cur.execute(f"""SELECT language.image, language.History from
         language
                WHERE language.id = (SELECT id_languages.id FROM id_languages 
                WHERE Language = '{self.name}')""").fetchall()
        image = f'flags/{result[0][0]}'
        information = result[0][1]
        con.close()  # TODO ЗАКРЫТИЕ БД

        # TODO РАБОТА С QPixmap. ВСТАВКА ИЗОБРАЖЕНИЕ В ОКНО
        self.pixmap = QPixmap(image)
        self.image = QLabel(self)
        self.image.move(150, -50)
        self.image.resize(250, 250)
        self.image.setPixmap(self.pixmap)
        self.plainTextEdit.setStyleSheet('color: #AFEEEE;'  # TODO Styles
                                         "background-image:"
                                         " url(background-image/back_2.jpg);"
                                         "border-radius: 10px; font-size: 12pt")
        self.plainTextEdit.setPlainText(information
                                        )
