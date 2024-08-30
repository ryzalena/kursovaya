from PIL import Image, ImageDraw, ImageFont
import pandas as pd

def add_text_to_image(image_path, data, our_x, y_kid, y_place, y_teacher, y_school):

    for index, row in data.iterrows():
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 12)

        surname = row['Фамилия']
        name = row['Имя']
        patronymic = row['Отчество']

        draw.text((our_x, y_kid), surname, anchor="ms", font=font, fill="black")
        draw.text((our_x, y_place), name, anchor="ms", font=font, fill="black")
        draw.text((our_x, y_teacher), patronymic, anchor="ms", font=font, fill="black")
        draw.text((our_x, y_school), patronymic, anchor="ms", font=font, fill="black")
        image.save(f"output_{index}.png")

def preparation(x, kid, place, teacher, school):
    data = pd.read_excel('data.xlsx')
    image_path = 'osnova.png'
    add_text_to_image(image_path, data, x, kid, place, teacher, school)
""" 
    our_x = x
    y_kid = kid
    y_place = place
    y_teacher = teacher
    y_school = school"""

"""
    y_surname_text = input ("Введите высоту 1: ")
    y_surname = int(y_surname_text)
"""
#add_text_to_image(image_path, data, y_surname)  # Вы можете указать любую высоту, например 50

#название грамоты должно быть оу_педагог_ребенок