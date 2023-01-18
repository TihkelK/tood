from tkinter import *
from tkinter import ttk

def kuu_nimi(o):
    kuud = ["", "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[o]
    
def kuupaev(p,l,a):
    vastus.config(text=f"{p}. {l} {a}. a")


#teiseldus
def teiselda():
    sisget = sisestus.get()
    p,k,a = sisget.split(".")
    kuupaev(p,kuu_nimi(int(k)),a)


#akna seaded
aken = Tk()
aken.resizable(0, 0)
aken.title("Kuupäev")
aken.geometry("300x300")

#sisestus
sisestus = Entry(aken)
sisestus.grid(row=2, column=0, padx=10, pady=5)

tekst = Label(aken,
              text="Sisesta kuupäev kujul DD.MM.YYYY: ",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=1, column=0)

#nupp
nupp1 = Button(aken, text="=", width=10, command=teiselda)
nupp1.grid(row=3, column=0)

#joon
joon = Label(aken, text="__________________________________", font="Tahoma 12",  padx=0, pady=5)
joon.grid(row=4, column=0)

#vastus
vastus = Label(aken,
              text="()",
              font="Tahoma 12",
              padx=2,
              pady=2)

vastus.grid(row=5, column=0)

aken.mainloop()