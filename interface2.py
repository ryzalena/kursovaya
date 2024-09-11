import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QWidget
from PyQt5.QtGui import QFont
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Автозаполнение грамот для ЦВО Творчество")
        self.setGeometry(200, 200, 800, 500)

        # Создаем центральный виджет
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Инициализируем элементы интерфейса
        self.initUI()

    def initUI(self):
        self.text = QLabel("Выберите, какой тип грамот надо создать", self)
        self.text.move(100, 100)
        self.text.adjustSize()

        self.btn = QPushButton("Пользовательские", self)
        self.btn.setFixedWidth(150)
        self.btn.move(100, 150)
        self.btn.clicked.connect(self.users)

    def users(self):
        self.text.hide()
        self.btn.hide()

        self.text2 = QLabel("Вам необходимо задать X и Y-координаты для расположения текста.", self)
        self.text2.move(100, 100)
        self.text2.adjustSize()

        self.text3 = QLabel("Вводить данные необходимо в пикселях.", self)
        self.text3.move(100, 130)
        self.text3.adjustSize()

        self.text4 = QLabel("Выберите вариант для X:", self)
        self.text4.move(100, 160)
        self.text4.adjustSize()

        self.btn2 = QPushButton("Одинаковый для всех строк", self)
        self.btn2.setFixedWidth(200)
        self.btn2.move(100, 200)
        self.btn2.clicked.connect(self.same)

        self.btn3 = QPushButton("Разный для каждой строки", self)
        self.btn3.setFixedWidth(200)
        self.btn3.move(450, 200)
        self.btn3.clicked.connect(self.hui2)

        self.text2.show()
        self.text3.show()
        self.text4.show()
        self.btn2.show()
        self.btn3.show()

    def same(self):
        self.text2.hide()
        self.text3.hide()
        self.text4.hide()
        self.btn2.hide()
        self.btn3.hide()

        self.text5 = QLabel("Вводить данные необходимо в пикселях.", self)
        self.text5.move(20, 20)

        self.text51 = QLabel("Ввод для Х:", self)
        self.text51.move(20, 60)

        self.num1_input = QLineEdit(self)
        self.num1_input.setFixedWidth(50)
        self.num1_input.move(120, 60)

        self.text52 = QLabel("Введите данные для Y", self)
        self.text52.move(20, 100)

        self.text53 = QLabel("Для ФИО ребенка:", self)
        self.text53.move(20, 140)

        self.num2_input = QLineEdit(self)
        self.num2_input.setFixedWidth(50)
        self.num2_input.move(120, 140)

        self.text54 = QLabel("Для места:", self)
        self.text54.move(20, 180)

        self.num3_input = QLineEdit(self)
        self.num3_input.setFixedWidth(50)
        self.num3_input.move(120, 180)

        self.text55 = QLabel("Для ФИО педагога:", self)
        self.text55.move(20, 220)

        self.num4_input = QLineEdit(self)
        self.num4_input.setFixedWidth(50)
        self.num4_input.move(120, 220)

        self.text56 = QLabel("Для названия ОУ:", self)
        self.text56.move(20, 260)

        self.num5_input = QLineEdit(self)
        self.num5_input.setFixedWidth(50)
        self.num5_input.move(120, 260)

        self.font_combo = QComboBox(self)
        self.fonts = self.list_fonts()
        self.font_combo.addItems([os.path.basename(f) for f in self.fonts])
        self.font_combo.move(20, 300)
        self.font_combo.resize(200, 30)

        self.btn4 = QPushButton("Сгенерировать", self)
        self.btn4.setFixedWidth(200)
        self.btn4.move(20, 340)
        self.btn4.clicked.connect(self.read_and_pass_data)

    def list_fonts(self):
        font_dirs = [
            "C:\\Windows\\Fonts",  # Windows
            "/usr/share/fonts",  # Linux
            "/usr/local/share/fonts",
            "~/.fonts",
            "/Library/Fonts",  # macOS
            "~/Library/Fonts"
        ]
        fonts = []
        for font_dir in font_dirs:
            expanded_dir = os.path.expanduser(font_dir)
            if os.path.exists(expanded_dir):
                for root, dirs, files in os.walk(expanded_dir):
                    for file in files:
                        if file.lower().endswith(".ttf"):
                            fonts.append(os.path.join(root, file))
        return fonts

    def read_and_pass_data(self):
        x = self.num1_input.text()
        kid = self.num2_input.text()
        place = self.num3_input.text()
        teacher = self.num4_input.text()
        school = self.num5_input.text()
        font_name = self.font_combo.currentText()

        self.preparation(x, kid, place, teacher, school, font_name)

    def preparation(self, x, kid, place, teacher, school, font_name):
        x = int(x)
        kid = int(kid)
        place = int(place)
        teacher = int(teacher)
        school = int(school)

        data = pd.read_excel('data.xlsx')
        image_path = 'osnova.png'

        font_path = os.path.join("C:\\Windows\\Fonts", font_name)
        try:
            font = ImageFont.truetype(font_path, 24)
        except IOError:
            print(f"Не удалось загрузить шрифт: {font_path}")
            return

        for index, row in data.iterrows():
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)

            surname = row['Фамилия']
            name = row['Имя']
            patronymic = row['Отчество']

            draw.text((x, kid), surname, anchor="ms", font=font, fill="black")
            draw.text((x, place), name, anchor="ms", font=font, fill="black")
            draw.text((x, teacher), patronymic, anchor="ms", font=font, fill="black")
            draw.text((x, school), patronymic, anchor="ms", font=font, fill="black")

            image.save(f"output_{index}.png")

    def hui2(self):
        pass

def application():
    app = QApplication(sys.argv)
    app.setStyleSheet('QLabel { font: bold }')

    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
