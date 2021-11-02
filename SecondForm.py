import webbrowser
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow
from History_form import History_from


class SecondForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designs/SecondForm.ui', self)  # TODO ПОДКЛЮЧЕНИЕ К ДИЗАЙНУ
        self.history_lang.clicked.connect(self.open_second_form)

        # TODO Styles
        self.list_of_languages.setStyleSheet(
            "QComboBox {background-image: url(background-image/select_2.jpg);"
            " padding:25px 50px 30px 155px;"
            "border-radius: 10px; color: rgb(255, 255, 255);}"
            "QComboBox::drop-down{border-radius: 10px; background-image:"
            " url(background-image/select_2.jpg);"
            "color: black;font-weight:bold; padding: 0px;}"
            "QComboBox::down-arrow{color: white;padding-right: 5px;}")
        self.history_lang.setStyleSheet(
            "QPushButton {background-image: url(background-image/select_2.jpg);"
            " border-radius: 10px; color: rgb(255, 255, 255);}")
        self.footer.setStyleSheet("color: #ececec;")
        self.company_name.setStyleSheet("color: #ececec;")

        # TODO CONNECTING
        self.contact_vk.clicked.connect(
            lambda: webbrowser.open('https://vk.com/im?peers=363207223_59245633'
                                    '3_458503653_-97568278&sel=262014370'))
        self.contact_tg.clicked.connect(
            lambda: webbrowser.open('https://t.me/I_am_a_busy_person'))
        self.contact_google.clicked.connect(
            lambda: webbrowser.open('mailto: khairullov.ruslan@gmail.com'))
        self.selected.clicked.connect(self.select_lan)

        # TODO ПОДДЕРЖИВАЕМЫЕ ЯЗЫКИ
        languages_dict = {'Русский': 'Russian', 'Английский': 'English',
                          'Испанский': 'Spanish', 'Французский': 'French',
                          'Бенгальский': 'Bengali', 'Португальский':
                              'Portuguese', 'Индонезийский': 'Indonesian',
                          'Японский': 'Japanese', 'Турецкий': 'Turkish',
                          'Украинский': 'Ukrainian', 'Корейский': 'Korean',
                          'Немецкий': 'German', 'Итальянский': 'Italian',
                          'Польский': 'Polish', 'Норвежский': 'Norwegian'}
        self.lang = 'Русский'  # TODO ТЕКУЩИЙ ЯЗЫК

        # TODO ДОБАВЛНИЕ ЭЛЕМЕНТОВ В ДОБАВЛЕНИЕ В QComboBox
        for i in sorted(languages_dict):
            self.list_of_languages.addItem(i)

        # TODO ИЗМЕНЕНИЕ КУРСОРА
        self.list_of_languages.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.history_lang.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.selected.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.contact_tg.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.contact_vk.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.contact_google.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        # TODO СОЗДАНИЕ ВСПЛЫВАЮЩИХ ОКОН
        self.contact_tg.setToolTip('Перейти')
        self.contact_vk.setToolTip('Перейти')
        self.contact_google.setToolTip('Перейти')
        self.list_of_languages.setToolTip('Список поддерживаемых языков')
        self.history_lang.setToolTip('Информация о выбранном языке')
        self.selected.setToolTip('Выбрать')

    def select_lan(self):  # TODO ПОЛУЧЕНИЕ ЯЗЫКА ИЗ QComboBox
        self.lang = self.list_of_languages.currentText()
        return self.list_of_languages.currentText()

    def open_second_form(self):  # TODO ОТКРЫТИЕ ВТОРОГО ОКНА
        name = self.lang
        self.history_form = History_from(self, name)
        self.history_form.setWindowIcon(QtGui.QIcon('icons/logo.png'))
        self.history_form.setFixedSize(455, 589)
        self.history_form.show()
