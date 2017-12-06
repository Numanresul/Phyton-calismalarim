# -*- coding: utf-8 -*-
from Tkinter import *
def show_entry_fields():
    print ("Adınız: %s\nSoyadınız: %s" % (e1.get(),e2.get()))
    e1.delete(0,END)
    e2.delete(0,END)

master = Tk()
Label(master,text="Adınız").grid(row=0)
Label(master,text="Soyadınız").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)
e1.insert(10,"Mert")
e2.insert(10,"Mustafa")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Çıkış', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Göster', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )