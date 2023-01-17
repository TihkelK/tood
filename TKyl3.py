from tkinter import *
from  tkinter import ttk

#akna seaded
aken = Tk()
aken.title('Tervitus"')
aken.resizable(0, 0)
aken.configure(background='black')

tekst1 = Label(aken, text="Nimi: Mihkel Kuusemäe", justify=CENTER, font="Tahoma 16 bold italic", foreground="red", background="black", pady=10, padx=30).pack()
tekst2 = Label(aken, text="Rühm: IT-22", justify=CENTER, font="Tahoma 16 bold italic", foreground="red", background="black").pack()
tekst3 = Label(aken, text="2023", justify=CENTER, font="Tahoma 16 bold italic", foreground="red", background="black", pady=10).pack()



aken.mainloop()