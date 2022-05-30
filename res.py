import billboard
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def ch1(data: str, num: int):
    chart = billboard.ChartData('hot-100', data)
    res = []
    if num > 15:
        num = 15

    for i in range(num):
        res.append( chart[i].artist + " - " + chart[i].title)
    return res


def ch2(data: str, art: str, song: str):
    chart = billboard.ChartData('hot-100', data)
    r = "Не нашлось в этом чарте "
    for i in range(len(chart)):
        s = chart[i]
        if s.title == song and s.artist == art:
            r = "На выбранную дату " + str(art) + " - " + str(song) + " заняла " + str(s.rank) + " место"
    return r


def ch3(data: str, art: str):
    chart = billboard.ChartData('hot-100', data)
    r = "Не нашлось в этом чарте "
    res = []
    for i in range(len(chart)):
        s = chart[i]
        if s.artist == art:
            res.append(str(s.rank) + " : " + s.artist + " - " + s.title)
    if res != []:
        return res
    else:
        return r


def ch4(datafrom: str, datato: str, art: str):
    dd=datafrom
    count = 0
    songs = []
    while strTodate(dd) < strTodate(datato):
        chart = billboard.ChartData('hot-100', dd)
        for i in range(len(chart)):
            if chart[i].artist == art and not chart[i].title in songs:
                count += 1
                songs.append(chart[i].title)
        dd= move(dd)
    count = str(count)
    count = "На выбранный период артист " + art + " " + count + " раз(а) вошёл в чарт"
    return count


def ch5(datafrom: str, datato: str, art: str, song: str):
    dd = datafrom
    count = 0
    while strTodate(dd) < strTodate(datato):
        chart = billboard.ChartData('hot-100', dd)
        for i in range(len(chart)):
            if chart[i].artist == art and chart[i].title == song:
                if count < chart[i].peakPos:
                    count = chart[i].peakPos
        dd = move(dd)
    count = str(count)
    count = "На выбранный период максимальная позиция артиста " + art + " - " + count
    return count


def strTodate(date: str):
    date = date.split('-')
    return datetime.date(int(date[0]), int(date[1]), int(date[2]))


def dateTostr(date: datetime):
    month=date.month
    day=date.day
    if len(str(date.month))==1:
        month="0"+str(date.month)
    if len(str(date.day))==1:
        day="0"+str(date.day)
    return str(str(date.year) + "-" +str(month) + "-" + str(day))


def move(date: str):
    date = strTodate(date)
    date = date + datetime.timedelta(days=7)
    return dateTostr(date)


def findinfo(art: str, song: str, chart: billboard.ChartData):
    s = 'Не найдено'
    for i in range(len(chart)):
        if chart[i].artist == art and chart[i].title == song:
            s = chart[i]
    return s


def ch10(date: str, num: int):
    if num>100:
        chart = "Чарт не состоит из "+ str(num)+" мест(а)"
    else:
        chart = billboard.ChartData('hot-100', date)
        chart = chart[num - 1].artist + " - " + chart[num - 1].title

    return chart


def ch7(art: str, song: str, date: str):
    chart = billboard.ChartData('hot-100', date)
    s = findinfo(art, song, chart)
    if s == True:
        s = " является новой"
    else:
        s = " не является новой"
    s = "На выбранную дату песня " +art + " - " + song + s
    return s


def ch6(art: str, song: str, date: str):
    chart = billboard.ChartData('hot-100', date)
    s = findinfo(art, song, chart)
    s = str(s.weeks)
    s = "На выбранную дату " + art + " - " + song + " встречается " + s + " раз в чарте"
    return s


def ch9(c: str, date: str):
    chart = billboard.ChartData('hot-100', date)
    count = 0
    if len(c) != 1: return 'неверный символ'
    for i in range(len(chart)):
        if chart[i].title[0]==c:
            count += 1
    return count


def ch8(word: str, date: str):
    chart = billboard.ChartData('hot-100', date)
    count = 0
    song=""
    for i in range(len(chart)):
        song=chart[i].title
        if song.find(word) != -1:
            count += 1
    return count

'''

'''

def call1():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('450x350')
    newWindow.title("Поиск чарта по дате")
    newWindow.configure(bg='#addbcb')

    label1 = tk.Label(newWindow, text="Введите дату:", background='#addbcb')
    label1.place(x=100, y=10,
                width=125, height=20)

    label2 = tk.Label(newWindow, text="Введите кол-во песен:", background='#addbcb')
    label2.place(x=100, y=40,
                width=125, height=20)

    labelt1 = tk.Label(newWindow, text=" ", background='#addbcb')
    labelt1.place(x=0, y=100,
                 width=450, height=250)


    txt1 = tk.Entry(newWindow)
    txt1.insert(0, " ")
    txt1.place(x=225, y=10,
            width=125, height=20)

    txt2 = tk.Entry(newWindow)
    txt2.insert(0, "")
    txt2.place(x=225, y=40,
            width=125, height=20)

    def test1():
        txt = ch1(txt1.get(), int(txt2.get()))
        I = 0
        CH = ""
        for item in txt:
            I += 1
            CH += str(I) + " : " + str(item) + " " + "\n"

        labelt1.config(text=CH)

    button = tk.Button(newWindow, text="Ввод!", command=test1)
    button.place(x=100, y=70,
                width=250, height=20)

    MainButton.pack()


def call2():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('450x350')
    newWindow.title("Место песни")
    newWindow.configure(bg='#addbcb')

    label1 = tk.Label(newWindow, text="Введите дату:", background='#addbcb')
    label1.place(x=100, y=10,
                 width=125, height=20)

    label2 = tk.Label(newWindow, text="Введите артиста:", background='#addbcb')
    label2.place(x=100, y=40,
                 width=125, height=20)

    label3 = tk.Label(newWindow, text="Введите песню:", background='#addbcb')
    label3.place(x=100, y=70,
                 width=125, height=20)

    txt1 = tk.Entry(newWindow)
    txt1.insert(0, " ")
    txt1.place(x=225, y=10,
               width=125, height=20)

    txt2 = tk.Entry(newWindow)
    txt2.insert(0, " ")
    txt2.place(x=225, y=40,
               width=125, height=20)

    txt3 = tk.Entry(newWindow)
    txt3.insert(0, " ")
    txt3.place(x=225, y=70,
               width=125, height=20)

    labelt1 = tk.Label(newWindow, text=" ", background='#addbcb')
    labelt1.place(x=0, y=130,
                 width=450, height=20)

    def test2():
        txt = ch2(txt1.get(), txt2.get(), txt3.get())

        labelt1.config(text=txt)

    button = tk.Button(newWindow, text="Ввод!", command=test2)
    button.place(x=100, y=100,
                 width=250, height=20)

    MainButton.pack()


def call3():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('450x350')
    newWindow.title("Кол-во песен мызыканта")
    newWindow.configure(bg='#addbcb')

    label1 = tk.Label(newWindow, text="Введите дату:", background='#addbcb')
    label1.place(x=100, y=10,
                 width=125, height=20)

    label2 = tk.Label(newWindow, text="Введите артиста:", background='#addbcb')
    label2.place(x=100, y=40,
                 width=125, height=20)

    labelt1 = tk.Label(newWindow, text=" ", background='#addbcb')
    labelt1.place(x=0, y=100,
                 width=450, height=100)

    txt1 = tk.Entry(newWindow)
    txt1.insert(0, " ")
    txt1.place(x=225, y=10,
               width=125, height=20)

    txt2 = tk.Entry(newWindow)
    txt2.insert(0, " ")
    txt2.place(x=225, y=40,
               width=125, height=20)

    def test3():
        txt = ch3(txt1.get(), txt2.get())
        CH = ""
        for item in txt:
            CH +=str(item) + " " + "\n"

        labelt1.config(text=CH)

    button = tk.Button(newWindow, text="Ввод!", command=test3)
    button.place(x=100, y=70,
                 width=250, height=20)


    MainButton.pack()


def call4():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('450x350')
    newWindow.title("Кол-во песен мызыканта в период")
    newWindow.configure(bg='#addbcb')

    label1 = tk.Label(newWindow, text="Введите дату от:", background='#addbcb')
    label1.place(x=100, y=10,
                 width=125, height=20)

    label2 = tk.Label(newWindow, text="Введите дату до:", background='#addbcb')
    label2.place(x=100, y=40,
                 width=125, height=20)

    label3 = tk.Label(newWindow, text="Введите артиста:", background='#addbcb')
    label3.place(x=100, y=70,
                 width=125, height=20)

    labelt1 = tk.Label(newWindow, text=" ", background='#addbcb')
    labelt1.place(x=0, y=100,
                 width=450, height=100)

    txt1 = tk.Entry(newWindow)
    txt1.insert(0, " ")
    txt1.place(x=225, y=10,
               width=125, height=20)

    txt2 = tk.Entry(newWindow)
    txt2.insert(0, " ")
    txt2.place(x=225, y=40,
               width=125, height=20)

    txt3 = tk.Entry(newWindow)
    txt3.insert(0, " ")
    txt3.place(x=225, y=70,
               width=125, height=20)

    def test4():
        txt = ch4(txt1.get(), txt2.get(), txt3.get())

        labelt1.config(text=txt)

    button = tk.Button(newWindow, text="Ввод!", command=test4)
    button.place(x=100, y=100,
                 width=250, height=20)

    MainButton.pack()


def call5():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('450x350')
    newWindow.title("Пиковая позиция песни")
    newWindow.configure(bg='#addbcb')

    label1 = tk.Label(newWindow, text="Введите дату от:", background='#addbcb')
    label1.place(x=100, y=10,
                 width=125, height=20)

    label2 = tk.Label(newWindow, text="Введите дату до:", background='#addbcb')
    label2.place(x=100, y=40,
                 width=125, height=20)

    label3 = tk.Label(newWindow, text="Введите артиста:", background='#addbcb')
    label3.place(x=100, y=70,
                 width=125, height=20)

    label4 = tk.Label(newWindow, text="Введите песню:", background='#addbcb')
    label4.place(x=100, y=100,
                 width=125, height=20)

    txt1 = tk.Entry(newWindow)
    txt1.insert(0, " ")
    txt1.place(x=225, y=10,
               width=125, height=20)

    txt2 = tk.Entry(newWindow)
    txt2.insert(0, " ")
    txt2.place(x=225, y=40,
               width=125, height=20)

    txt3 = tk.Entry(newWindow)
    txt3.insert(0, " ")
    txt3.place(x=225, y=70,
               width=125, height=20)

    txt4 = tk.Entry(newWindow)
    txt4.insert(0, " ")
    txt4.place(x=225, y=100,
               width=125, height=20)

    labelt1 = tk.Label(newWindow, text=" ", background='#addbcb')
    labelt1.place(x=0, y=130,
                 width=450, height=100)

    def test5():
        txt = ch5(txt1.get(), txt2.get(), txt3.get(), txt4.get())

        labelt1.config(text=txt)


    button = tk.Button(newWindow, text="Ввод!", command=test5)
    button.place(x=100, y=130,
                 width=250, height=20)

    MainButton.pack()


def call6():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('450x350')
    newWindow.title("Кол-во недель песни в чарте")
    newWindow.configure(bg='#addbcb')

    label1 = tk.Label(newWindow, text="Введите артиста:", background='#addbcb')
    label1.place(x=100, y=10,
                 width=125, height=20)

    label2 = tk.Label(newWindow, text="Введите песню:", background='#addbcb')
    label2.place(x=100, y=40,
                 width=125, height=20)

    label3 = tk.Label(newWindow, text="На дату:", background='#addbcb')
    label3.place(x=100, y=70,
                 width=125, height=20)

    labelt1 = tk.Label(newWindow, text=" ", background='#addbcb')
    labelt1.place(x=0, y=100,
                  width=450, height=100)

    txt1 = tk.Entry(newWindow)
    txt1.insert(0, " ")
    txt1.place(x=225, y=10,
               width=125, height=20)

    txt2 = tk.Entry(newWindow)
    txt2.insert(0, " ")
    txt2.place(x=225, y=40,
               width=125, height=20)

    txt3 = tk.Entry(newWindow)
    txt3.insert(0, " ")
    txt3.place(x=225, y=70,
               width=125, height=20)

    def test6():
        txt = ch6(txt1.get(), txt2.get(), txt3.get())
        labelt1.config(text=txt)

    button = tk.Button(newWindow, text="Ввод!", command=test6)
    button.place(x=100, y=100,
                 width=250, height=20)

    MainButton.pack()


def call7():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('450x350')
    newWindow.title("Является ли песня новой на дату")
    newWindow.configure(bg='#addbcb')

    label1 = tk.Label(newWindow, text="Введите артиста:", background='#addbcb')
    label1.place(x=100, y=10,
                 width=125, height=20)

    label2 = tk.Label(newWindow, text="Введите песню:", background='#addbcb')
    label2.place(x=100, y=40,
                 width=125, height=20)

    label3 = tk.Label(newWindow, text="Введите дату:", background='#addbcb')
    label3.place(x=100, y=70,
                 width=125, height=20)

    labelt1 = tk.Label(newWindow, text=" ", background='#addbcb')
    labelt1.place(x=0, y=100,
                  width=450, height=100)

    txt1 = tk.Entry(newWindow)
    txt1.insert(0, " ")
    txt1.place(x=225, y=10,
               width=125, height=20)

    txt2 = tk.Entry(newWindow)
    txt2.insert(0, " ")
    txt2.place(x=225, y=40,
               width=125, height=20)

    txt3 = tk.Entry(newWindow)
    txt3.insert(0, " ")
    txt3.place(x=225, y=70,
               width=125, height=20)

    def test7():
        txt = ch7(txt1.get(), txt2.get(), txt3.get())
        labelt1.config(text=txt)

    button = tk.Button(newWindow, text="Ввод!", command=test7)
    button.place(x=100, y=100,
                 width=250, height=20)

    MainButton.pack()


def call8():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('450x350')
    newWindow.title("Есть ли песня со словом ___")
    newWindow.configure(bg='#addbcb')

    label1 = tk.Label(newWindow, text="Введите слово:", background='#addbcb')
    label1.place(x=100, y=10,
                 width=125, height=20)

    label2 = tk.Label(newWindow, text="Введите дату:", background='#addbcb')
    label2.place(x=100, y=40,
                 width=125, height=20)

    labelt1 = tk.Label(newWindow, text=" ", background='#addbcb')
    labelt1.place(x=0, y=70,
                  width=450, height=100)

    txt1 = tk.Entry(newWindow)
    txt1.insert(0, " ")
    txt1.place(x=225, y=10,
               width=125, height=20)

    txt2 = tk.Entry(newWindow)
    txt2.insert(0, " ")
    txt2.place(x=225, y=40,
               width=125, height=20)

    def test8():
        txt = ch8(txt1.get(), txt2.get())
        txt= str(txt)
        txt = "С выбранным словом " + txt + " песен(я/и)"
        labelt1.config(text=txt)

    button = tk.Button(newWindow, text="Ввод!", command=test8)
    button.place(x=100, y=70,
                 width=250, height=20)

    MainButton.pack()


def call9():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('450x350')
    newWindow.title("Сколько песен начинается с буквы ___")
    newWindow.configure(bg='#addbcb')

    label1 = tk.Label(newWindow, text="Введите букву:", background='#addbcb')
    label1.place(x=100, y=10,
                 width=125, height=20)

    label2 = tk.Label(newWindow, text="Введите дату:", background='#addbcb')
    label2.place(x=100, y=40,
                 width=125, height=20)

    labelt1 = tk.Label(newWindow, text=" ", background='#addbcb')
    labelt1.place(x=0, y=70,
                  width=450, height=100)

    txt1 = tk.Entry(newWindow)
    txt1.insert(0, " ")
    txt1.place(x=225, y=10,
               width=125, height=20)

    txt2 = tk.Entry(newWindow)
    txt2.insert(0, " ")
    txt2.place(x=225, y=40,
               width=125, height=20)

    def test9():
        txt = ch9(txt1.get(), txt2.get())
        txt = str(txt)
        txt = "С выбранной буквы начинается " + txt + " песен(я/и)"
        labelt1.config(text=txt)

    button = tk.Button(newWindow, text="Ввод!", command=test9)
    button.place(x=100, y=70,
                 width=250, height=20)

    MainButton.pack()


def call10():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('450x350')
    newWindow.title("Какая песня находится на ___ месте?")
    newWindow.configure(bg='#addbcb')

    label1 = tk.Label(newWindow, text="Введите дату:", background='#addbcb')
    label1.place(x=100, y=10,
                 width=125, height=20)

    label2 = tk.Label(newWindow, text="Введите место:", background='#addbcb')
    label2.place(x=100, y=40,
                 width=125, height=20)

    labelt1 = tk.Label(newWindow, text=" ", background='#addbcb')
    labelt1.place(x=0, y=70,
                  width=450, height=100)

    txt1 = tk.Entry(newWindow)
    txt1.insert(0, " ")
    txt1.place(x=225, y=10,
               width=125, height=20)

    txt2 = tk.Entry(newWindow)
    txt2.insert(0, " ")
    txt2.place(x=225, y=40,
               width=125, height=20)

    def test10():
        txt = ch10(txt1.get(), int(txt2.get()))
        txt = str(txt)
        txt = "На выбранном месте - " + txt
        labelt1.config(text=txt)

    button = tk.Button(newWindow, text="Ввод!", command=test10)
    button.place(x=100, y=70,
                 width=250, height=20)

    MainButton.pack()



def  createNewWindow():

    if combo.get() == "Поиск чарта по дате":
        call1()
    elif combo.get() == "Место песни":
        call2()
    elif combo.get() ==  "Кол-во песен мызыканта":
        call3()
    elif combo.get() ==  "Кол-во песен мызыканта в период":
        call4()
    elif combo.get() == "Пиковая позиция песни":
        call5()
    elif combo.get() == "Кол-во недель песни в чарте":
        call6()
    elif combo.get() ==  "Является ли песня новой на дату":
        call7()
    elif combo.get() == "Есть ли песня со словом ___":
        call8()
    elif combo.get() ==  "Сколько песен начинается с буквы ___":
        call9()
    elif combo.get() == "Какая песня находится на ___ месте?":
        call10()



window = tk.Tk()
window.geometry('450x350')
window.title("Анализ billboard hot 100")
window.configure(bg='#addbcb')

label = ttk.Label(window, text = " Анализ billboard hot 100 ", background='#addbcb', font="Courier 14 bold")
label.place(x=80, y=10,
                 width=350, height=20)

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
combo.place(x=100, y=50,
                 width=250, height=20)
combo.current(0)

MainButton = tk.Button(window,
              text="Поиск!",
              command=createNewWindow)
MainButton.pack(padx=10, pady=100)

window.mainloop()
