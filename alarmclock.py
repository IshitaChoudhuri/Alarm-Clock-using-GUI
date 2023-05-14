from lib2to3.pgen2.token import LBRACE
from tkinter import font
from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image
from pygame import mixer
from threading import Thread

from datetime import datetime
from time import sleep

# colors
bg_color = "#ffffff"
col = "#566FC6"
col2 = '#000000'

# window
window = Tk()
window.title("Alarm Clock using GUI")
window.geometry("450x150")
window.configure(bg=bg_color)

frame_line = Frame(window, width=500, height=5, bg=col)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=500, height=290, bg=bg_color)
frame_body.grid(row=1, column=0)

img = Image.open('icon.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height=100, image=img, bg=bg_color)
app_image.place(x=10, y=10)

name = Label(frame_body, text="Alarm", height=1,
             font=('Ivy 19 bold'), bg=bg_color)
name.place(x=125, y=10)

# hours
hour = Label(frame_body, text="hour", height=1,
             font=('Ivy 14 bold'), bg=bg_color, fg=col)
hour.place(x=127, y=40)
c_hour = Combobox(frame_body, width=2, font=('arial 11'))
c_hour['values'] = ("00", "01", "02", "03", "04", "05",
                    "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24")
c_hour.current(0)
c_hour.place(x=130, y=70)

# minutes
min = Label(frame_body, text="min", height=1,
            font=('Ivy 14 bold'), bg=bg_color, fg=col)
min.place(x=177, y=40)
c_min = Combobox(frame_body, width=2, font=('arial 11'))
c_min['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28",
                   "29", '30', "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_min.current(0)
c_min.place(x=180, y=70)


# seconds
sec = Label(frame_body, text="sec", height=1,
            font=('Ivy 14 bold'), bg=bg_color, fg=col)
sec.place(x=227, y=40)
c_sec = Combobox(frame_body, width=2, font=('arial 11'))
c_sec['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28",
                   "29", '30', "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_sec.current(0)
c_sec.place(x=230, y=70)


def activate_alarm():
    t = Thread(target=alarm)
    t.start()


def deactivate_alarm():
    print("Deactivate", selected.get())
    mixer.music.stop()


selected = IntVar()

rad1 = Radiobutton(frame_body, font=('arial 9 bold'), value=1,
                   text="Start", bg=bg_color, command=activate_alarm, variable=selected)
rad1.place(x=130, y=105)


def sound_alarm():
    mixer.music.load('alarm.mp3')
    mixer.music.play()
    selected.set(0)


rad2 = Radiobutton(frame_body, font=('arial 9 bold'), value=2, text="Stop",
                   bg=bg_color, command=deactivate_alarm, variable=selected)
rad2.place(x=190, y=105)


def sound_alarm():
    mixer.music.load('alarm.mp3')
    mixer.music.play()


def alarm():
    while True:
        control = selected.get()
        print(control)

        alarm_hour = c_hour.get()
        alarm_minute = c_min.get()
        alarm_sec = c_sec.get()

        now = datetime.now()

        hour = now.strftime("%H")
        min = now.strftime("%M")
        sec = now.strftime("%S")

        if control == 1:
            if alarm_hour == hour:
                if alarm_minute == min:
                    if alarm_sec == sec:
                        print("Break Time")
                        sound_alarm()
        sleep(1)


mixer.init()
window.mainloop()
