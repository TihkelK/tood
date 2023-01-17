from tkinter import *
from  tkinter import ttk

#funktsioonid
#def arvuta:
#    hind = sisestus.get()
#    kmaks = var
#    print(hind)


#akna seaded
aken = Tk()
aken.title('Kalkulaator')
aken.option_add('*font', ('tahoma', 12))
aken.geometry("200x200")

#tekst
tekst = Label(aken, text="Siia kunagi vastus!", pady=10, padx=8)
tekst.grid(row=0, columnspan=5, sticky=E+W)

#nupud
nupp0 = Button(aken, text="0", width=4, padx=2, pady=2)
nupp0.grid(row=4, column=1)

nuppkom = Button(aken, text=",", width=4, padx=2, pady=2)
nuppkom.grid(row=4, column=2)

nuppvor = Button(aken, text="=", width=4, padx=2, pady=2)
nuppvor.grid(row=4, column=3)

nuppliit = Button(aken, text="+", width=4, padx=2, pady=2)
nuppliit.grid(row=4, column=4)

nupp1 = Button(aken, text="1", width=4, padx=2, pady=2)
nupp1.grid(row=3, column=1)

nupp2 = Button(aken, text="2", width=4, padx=2, pady=2)
nupp2.grid(row=3, column=2)

nupp3 = Button(aken, text="3", width=4, padx=2, pady=2)
nupp3.grid(row=3, column=3)

nupplah = Button(aken, text="-", width=4, padx=2, pady=2)
nupplah.grid(row=3, column=4)

nupp4 = Button(aken, text="4", width=4, padx=2, pady=2)
nupp4.grid(row=2, column=1)

nupp5 = Button(aken, text="5", width=4, padx=2, pady=2)
nupp5.grid(row=2, column=2)

nupp6 = Button(aken, text="6", width=4, padx=2, pady=2)
nupp6.grid(row=2, column=3)

nuppkor = Button(aken, text="*", width=4, padx=2, pady=2)
nuppkor.grid(row=2, column=4)

nupp7 = Button(aken, text="7", width=4, padx=2, pady=2)
nupp7.grid(row=1, column=1)

nupp8 = Button(aken, text="8", width=4, padx=2, pady=2)
nupp8.grid(row=1, column=2)

nupp9 = Button(aken, text="9", width=4, padx=2, pady=2)
nupp9.grid(row=1, column=3)

nuppjag = Button(aken, text="/", width=4, padx=2, pady=2)
nuppjag.grid(row=1, column=4)

aken.mainloop()
