from tkinter import *


window = Tk()
window.title("Супермегагипер Chart")
window.geometry('350x450')
lbl = Label(window, text="Главная страница")
lbl.pack(anchor = 'center')

data = "Поиск чарта по дате:"
labeldata = Label(text=data, justify=LEFT)
labeldata.place(x=45, y=45)

data1 = "временной \n отрезок:"
labeldata1 = Label(text=data1, justify=LEFT)
labeldata1.place(x=180, y=40)

song = "Место песни:"
labelsong = Label(text=song, justify=LEFT)
labelsong.place(x=45, y=165)

song1 = "в чарте за временной \n период:"
labelsong1 = Label(text=song1, justify=LEFT)
labelsong1.place(x=180, y=160)

artiste = "Кол-во песен \n мызыканта:"
labelartiste = Label(text=artiste, justify=LEFT)
labelartiste.place(x=45, y=285)

artiste1 = "в чарте за временной \n период:"
labelartiste1 = Label(text=artiste1, justify=LEFT)
labelartiste1.place(x=180, y=285)





window.mainloop()
