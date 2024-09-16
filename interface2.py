import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QWidget, QFileDialog
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

        self.btn2 = QPushButton("Городские", self)
        self.btn2.setFixedWidth(150)
        self.btn2.move(400, 150)
        self.btn2.clicked.connect(self.city)

    def users(self):


        self.text.hide()
        self.btn.hide()
        self.btn2.hide()

        self.base_image_path, _ = QFileDialog.getOpenFileName(self, 'Выберите изображение для основы грамоты', '', '*.png')
        if not self.base_image_path:
            print("No image selected. Exiting.")
            sys.exit()


        self.data_path, _ = QFileDialog.getOpenFileName(self, 'Выберите файл Excel для сбора данных', '', '*.xlsx')
        if not self.data_path:
            print("No Excel file selected. Exiting.")
            sys.exit()

        self.text11 = QLabel("Вам необходимо задать X и Y-координаты для расположения текста.", self)
        self.text11.move(100, 70)
        self.text11.adjustSize()
        self.text11.show()

        self.text12 = QLabel("Вводить данные необходимо в пикселях.", self)
        self.text12.move(100, 100)
        self.text12.adjustSize()
        self.text12.show()

        self.text13 = QLabel("Ввод для Х:", self)
        self.text13.move(100, 135)
        self.text13.adjustSize()
        self.text13.show()

        self.num1_input = QLineEdit(self)
        self.num1_input.setFixedWidth(50)
        self.num1_input.move(250, 130)
        self.num1_input.show()

        self.text14 = QLabel("Введите данные для Y:", self)
        self.text14.move(100, 200)
        self.text14.adjustSize()
        self.text14.show()

        self.text15 = QLabel("Выберите шрифт:", self)
        self.text15.move(350, 200)
        self.text15.adjustSize()
        self.text15.show()

        self.text110 = QLabel("Введите размер шрифта:", self)
        self.text110.move(600, 200)
        self.text110.adjustSize()
        self.text110.show()



        self.text16 = QLabel("Для ФИО ребенка:", self)
        self.text16.move(100, 235)
        self.text16.adjustSize()
        self.text16.show()


        self.num2_input = QLineEdit(self)
        self.num2_input.setFixedWidth(50)
        self.num2_input.move(250, 230)
        self.num2_input.show()

        self.font_combo = QComboBox(self)
        self.fonts = self.list_fonts()
        self.font_combo.addItems([os.path.basename(f) for f in self.fonts])
        self.font_combo.move(350, 230)
        self.font_combo.resize(200, 30)
        self.font_combo.show()

        self.size_combo = QComboBox(self)
        self.size_combo.addItems(["6", "8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30", "32", "34", "36", "40", "50", "52", "54", "56", "58", "60"])
        self.size_combo.move(600, 230)
        self.size_combo.resize(100, 30)
        self.size_combo.show()

        self.text17 = QLabel("Для места:", self)
        self.text17.move(100, 270)
        self.text17.adjustSize()
        self.text17.show()

        self.num3_input = QLineEdit(self)
        self.num3_input.setFixedWidth(50)
        self.num3_input.move(250, 265)
        self.num3_input.show()

        self.font_combo2 = QComboBox(self)
        self.fonts2 = self.list_fonts()
        self.font_combo2.addItems([os.path.basename(f) for f in self.fonts])
        self.font_combo2.move(350, 265)
        self.font_combo2.resize(200, 30)
        self.font_combo2.show()

        self.size_combo2 = QComboBox(self)
        self.size_combo2.addItems(["6", "8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30", "32", "34", "36", "40", "50", "52", "54", "56", "58", "60"])
        self.size_combo2.move(600, 265)
        self.size_combo2.resize(100, 30)
        self.size_combo2.show()

        self.text18 = QLabel("Для ФИО педагога:", self)
        self.text18.move(100, 305)
        self.text18.adjustSize()
        self.text18.show()

        self.num4_input = QLineEdit(self)
        self.num4_input.setFixedWidth(50)
        self.num4_input.move(250, 300)
        self.num4_input.show()

        self.font_combo3 = QComboBox(self)
        self.fonts3 = self.list_fonts()
        self.font_combo3.addItems([os.path.basename(f) for f in self.fonts])
        self.font_combo3.move(350, 300)
        self.font_combo3.resize(200, 30)
        self.font_combo3.show()



        self.size_combo3 = QComboBox(self)
        self.size_combo3.addItems(["6", "8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30", "32", "34", "36", "40", "50", "52", "54", "56", "58", "60"])
        self.size_combo3.move(600, 300)
        self.size_combo3.resize(100, 30)
        self.size_combo3.show()

        self.text19 = QLabel("Для названия ОУ:", self)
        self.text19.move(100, 340)
        self.text19.adjustSize()
        self.text19.show()

        self.num5_input = QLineEdit(self)
        self.num5_input.setFixedWidth(50)
        self.num5_input.move(250, 335)
        self.num5_input.show()

        self.font_combo4 = QComboBox(self)
        self.fonts4 = self.list_fonts()
        self.font_combo4.addItems([os.path.basename(f) for f in self.fonts])
        self.font_combo4.move(350, 335)
        self.font_combo4.resize(200, 30)
        self.font_combo4.show()

        self.size_combo4 = QComboBox(self)
        self.size_combo4.addItems(["6", "8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30", "32", "34", "36", "40", "50", "52", "54", "56", "58", "60"])
        self.size_combo4.move(600, 335)
        self.size_combo4.resize(100, 30)
        self.size_combo4.show()




        self.btn4 = QPushButton("Сгенерировать", self)
        self.btn4.setFixedWidth(200)
        self.btn4.move(100, 375)
        self.btn4.clicked.connect(self.read_and_pass_data)
        self.btn4.show()

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
        font_name2 = self.font_combo2.currentText()
        font_name3 = self.font_combo3.currentText()
        font_name4 = self.font_combo4.currentText()
        size1 = self.size_combo.currentText()
        size2 = self.size_combo2.currentText()
        size3 = self.size_combo3.currentText()
        size4 = self.size_combo4.currentText()



        self.preparation(x, kid, place, teacher, school, font_name, font_name2, font_name3, font_name4, size1, size2, size3, size4)

    def preparation(self, x, kid, place, teacher, school, font_name, font_name2, font_name3, font_name4, size1, size2, size3, size4):
        x = int(x)
        kid = int(kid)
        place = int(place)
        teacher = int(teacher)
        school = int(school)


        image_path = self.base_image_path
        data = pd.read_excel(self.data_path)

        font_path = os.path.join("C:\\Windows\\Fonts", font_name)
        try:
            font = ImageFont.truetype(font_path, size=int(size1))
        except IOError:
            print(f"Не удалось загрузить шрифт: {font_path}")
            return

        font_path2 = os.path.join("C:\\Windows\\Fonts", font_name2)
        try:
            font2 = ImageFont.truetype(font_path2, size=int(size2))
        except IOError:
            print(f"Не удалось загрузить шрифт: {font_path2}")
            return

        font_path3 = os.path.join("C:\\Windows\\Fonts", font_name3)
        try:
            font3 = ImageFont.truetype(font_path3, size=int(size3))
        except IOError:
            print(f"Не удалось загрузить шрифт: {font_path3}")
            return

        font_path4 = os.path.join("C:\\Windows\\Fonts", font_name4)
        try:
            font4 = ImageFont.truetype(font_path4, size=int(size4))
        except IOError:
            print(f"Не удалось загрузить шрифт: {font_path4}")
            return


        for index, row in data.iterrows():
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)

            author_name = row['Фамилия, имя автора конкурсной работы']
            place_name = row['Место']
            teacher_name = row['Ф.И.О. педагога (руководителя)']
            school_name = row['Полное наименование образовательного учреждения']

            draw.text((x, kid), author_name, anchor="ms", font=font, fill="black")
            draw.text((x, place), place_name, anchor="ms", font=font2, fill="black")
            draw.text((x, teacher), teacher_name, anchor="ms", font=font3, fill="black")
            draw.text((x, school), school_name, anchor="ms", font=font4, fill="black")
            image.save(f"output_{index}.png")

        self.text6 = QLabel("Грамоты созданы", self)
        self.text6.move(100, 430)
        self.text6.adjustSize()
        self.text6.show()

    def city(self):
        pass

"""
    def city(self):
        self.text.hide()
        self.btn.hide()

        self.base_image_path, _ = QFileDialog.getOpenFileName(self, 'Выберите изображение для основы грамоты', '',
                                                              '*.png')
        if not self.base_image_path:
            print("No image selected. Exiting.")
            sys.exit()

        self.data_path, _ = QFileDialog.getOpenFileName(self, 'Выберите файл Excel для сбора данных', '', '*.xlsx')
        if not self.data_path:
            print("No Excel file selected. Exiting.")
            sys.exit()
"""
def application():
    app = QApplication(sys.argv)
    app.setStyleSheet('QLabel { font: bold }')

    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
