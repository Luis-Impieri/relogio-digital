from time import *
from tkinter import *
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


def segundos():
    passagem = strftime("%H: %M: %S")
    tempo.config(text=passagem)
    tempo.after(1000, segundos)

def dias():
    decorrer = strftime("%A")
    dia.config(text=decorrer)
    dia.after(1000, dias)
    meses = strftime("%d de %B de %Y")
    data.config(text=meses)
    data.after(1000, dias)

window = Tk()

tempo = Label(window,
                  bg="#000000",
                  fg="#FF0000",
                  font=("Constantia", 60),
                  width=15,
                  height=2
                  )
tempo.pack()

dia = Label(window,
                  bg="#000000",
                  fg="#FF0000",
                  font=("Constantia", 60),
                  width=15,
                  height=2)
dia.pack()

data = Label(window,
                  bg="#000000",
                  fg="#FF0000",
                  font=("Constantia", 60),
                  width=15,
                  height=2)
data.pack()

segundos()

dias()

window.mainloop()