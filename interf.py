import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.geometry('450x350')
window.title("супермегагиперкласс")

labeldata = ttk.Label(window, text = "Введите дату(опционально):")
labeldata.grid(column=1, row=1)

txt = tk.Entry(window, width=10)
txt.insert(0, "YYYY-MM-DD")
txt.grid(column=1, row=2, sticky='ew')

labelTop = ttk.Label(window, text = "Выберите функцию:")
labelTop.grid(column=1, row=4)

combo = ttk.Combobox(window, values=["Поиск чарта по дате", "Место песни",
                                     "Кол-во песен мызыканта",
                                     "Кол-во песен мызыканта в период",
                                     "Пиковая позиция песни",
                                     "Кол-во недель песни в чарте",
                                     "Является ли песня новой на дату",
                                     "Есть ли песня со словом ___",
                                     "Сколько песен начинается с буквы ___",
                                     "Какая песня находится на ___ месте?"])
print(dict(combo))
combo.grid(column=1, row=5)
combo.current(1)
print(combo.current(), combo.get())

labeldata = ttk.Label(window, text = " ♡♡♡ ")
labeldata.grid(column=1, row=0)

labeldata = ttk.Label(window, text = " ♡♡♡♡♡ ")
labeldata.grid(column=1, row=3)

labeldata = ttk.Label(window, text = " ♡♡♡♡♡♡♡ ")
labeldata.grid(column=1, row=6)

labeldata = ttk.Label(window, text = " ♡                                ")
labeldata.grid(column=0, row=0)

btn = tk.Button(window, text='Поиск')
btn.grid(column=1, row=7)



window.mainloop()
