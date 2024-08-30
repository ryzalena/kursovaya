from tkinter import *
import for_our

def clicked_for_city ():
    lbl.configure(text="Я же просил...")

"""
def for_out_to(x, kid, place, teacher, school):
    for_our.preparation(x, kid, place, teacher, school)
"""

def click(x, kid, place, teacher, school):
    ix=int(x.get())
    kids=int(kid.get())
    places=int(place.get())
    teachers=int(teacher.get())
    schools=(school.get())

    for_our.preparation(ix, kids, places, teachers, schools)


def same ():
    for widget in frame.winfo_children():
        widget.destroy()
    lbl = Label(frame, text="Ввод X:", font=("Arial Bold", 18), wraplength=800)
    lbl.grid(row=0, column=0)
    x = Entry(frame, width=10)
    x.grid(row=0, column=1)

    lbl = Label(frame, text="\n Введите данные для Y:", font=("Arial Bold", 18), wraplength=800)
    lbl.grid(row=1, column=0)
    lbl = Label(frame, text="Для ФИО ребенка:", font=("Arial Bold", 18), wraplength=800)
    lbl.grid(row=2, column=0)
    kid = Entry(frame, width=10)
    kid.grid(row=2, column=1)

    lbl = Label(frame, text="Для места:", font=("Arial Bold", 18), wraplength=800)
    lbl.grid(row=3, column=0)
    place = Entry(frame, width=10)
    place.grid(row=3, column=1)

    lbl = Label(frame, text="Для ФИО педагога:", font=("Arial Bold", 18), wraplength=800)
    lbl.grid(row=4, column=0)
    teacher = Entry(frame, width=10)
    teacher.grid(row=4, column=1)

    lbl = Label(frame, text="Для названия ОУ:", font=("Arial Bold", 18), wraplength=800)
    lbl.grid(row=5, column=0)
    school = Entry(frame, width=10)
    school.grid(row=5, column=1)
    btn = Button(frame, text="Отправить данные", font=("Arial Bold", 18),
                  command=click(x, kid, place, teacher, school))

    #command=lambda: for_our.preparation((int(x.get()), int(kid.get()), int(place.get()), int(teacher.get()), int(school.get()))))
    btn.grid(row=6, column=0, columnspan=2)

"""
    btn = Button(frame, text="Сгененрировать", font=("Arial Bold", 18), wraplength=800, command=lambda: for_out_to(int(x.get()), kid.get(), place.get(), teacher.get(), school.get()))
    btn.grid(row=6, column=0, columnspan=2)
"""
def different ():
    for widget in frame.winfo_children():
        widget.destroy()


def clicked_for_our ():
    for widget in frame.winfo_children():
        widget.destroy()
    lbl = Label(frame, text="Вам необходимо задать X и Y-координаты для расположения текста. Вводить данные необходимо в пикселях.", font=("Arial Bold", 18), wraplength=800)
    lbl.grid(row=0, column=0, columnspan=2)
    lbl = Label(frame, text="Выберите вариант для X:", font=("Arial Bold", 18))
    lbl.grid(row=1, column=0, columnspan=2)
    btn = Button(frame, text="Одинаковый для всех строк", bg="black", fg="red", command=same)
    btn.grid(row=2, column=0)
    btn = Button(frame, text="Разный для каждой строки", command=different)
    btn.grid(row=2, column=1)



window = Tk()
window.title("Автозаполнение грамот для ЦВО Творчество")
frame = Frame(
   window,
   padx = 10,
   pady = 10
)
frame.pack(expand=True)

lbl = Label(frame, text="Выберите, какой тип грамот надо создать", font=("Arial Bold", 18))
lbl.grid(row=0, column=0, columnspan = 2)
window.geometry('900x400')
btn = Button(frame, text="Пользовательские", bg="black", fg="red", command=clicked_for_our)
btn.grid(row=1, column=0)
btn = Button(frame, text="Для города", command=clicked_for_city)
btn.grid(row=1, column=1)



window.mainloop()