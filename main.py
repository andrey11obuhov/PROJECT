import billboard
import datetime

def ch1(data: str, num: int):
    chart = billboard.ChartData('hot-100', data)
    res = []
    if num > 100:
        num = 100

    for i in range(num):
        res.append(str(chart[i].rank) + " " + chart[i].artist + " " + chart[i].title)
    return res


def ch2(data: str, art: str, song: str):
    chart = billboard.ChartData('hot-100', data)
    r = "Not found in this chart "
    for i in range(len(chart)):
        s = chart[i]
        if s.title == song and s.artist == art:
            r = s.rank
    return r


def ch3(data: str, art: str):
    chart = billboard.ChartData('hot-100', data)
    r = "Not found in this chart "
    res = []
    for i in range(len(chart)):
        s = chart[i]
        if s.artist == art:
            res.append(str(s.rank) + " " + s.artist + " " + s.title)
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
    s = 'Not found'
    for i in range(len(chart)):
        if chart[i].artist == art and chart[i].title == song:
            s = chart[i]
    return s


def ch10(date: str, num: int):
    if num>100:
        return "There is no "+ str(num)+"th place"
    chart = billboard.ChartData('hot-100', date)
    return chart[num - 1].artist + " " + chart[num - 1].title


def ch7(art: str, song: str, date: str):
    chart = billboard.ChartData('hot-100', date)
    s = findinfo(art, song, chart)
    return s.isNew


def ch6(art: str, song: str, date: str):
    chart = billboard.ChartData('hot-100', date)


    s = findinfo(art, song, chart)
    return s.weeks


def ch9(c: str, date: str):
    chart = billboard.ChartData('hot-100', date)
    count = 0
    if len(c) != 1: return 'symbol is incorrect'
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
print(ch10( "2022-05-19", 101))
