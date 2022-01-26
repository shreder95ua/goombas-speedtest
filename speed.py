import speedtest
from time import sleep as wait
from time import asctime
from os.path import isfile
threads = None
style = '''<style>
body {font-family:'Comic Sans MS',cursive}</style>'''
if not isfile("internet_diagnosis.htm"):
    file = open("internet_diagnosis.htm", "w")
    file.write(f'{style}<title>Діагностика інтернету</title><link rel="icon" type="image/x-icon" href="http://www.rw-designer.com/icon-image/14196-256x256x32.png">')
    file.close()
file = open("internet_diagnosis.htm", "a")
print("---- Включення за", asctime(), "----")
file.write("<h1>Включення за " + asctime() + "</h1>")
file.close()
file = open("internet_diagnosis.htm", "a")
while True:
    try:
        s = speedtest.Speedtest()
        download = s.download(threads=threads) / 1000000
        print("Завантаження:", download)
    except speedtest.ConfigRetrievalError:
        download = 0.0
        print("Немає підключення до інтернету! (але програма досі працює)\n")
    time = asctime()
    if int(download) == 0:
        color = "red"
    elif int(download) < 6:
        color = "orange"
    elif int(download) < 11:
        color = "yellow"
    elif int(download) < 16:
        color = "yellowgreen"
    else:
        color = "green"
    file.write(f'<h3 style="color:darkblue">{time}:</h3><p style="color:{color}">Завантаження: {str(download)}</p>')
    file.close()
    file = open("internet_diagnosis.htm", "a")
    wait(60)