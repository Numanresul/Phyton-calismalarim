#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import random

pencere = Tk()

pencere.geometry("300x50+600+460")

def kodlar():
    liste = []
    for i in range(6):
        while len(liste) != 6:
            a = random.randint(1,100)
            if a not in liste:
                liste.append(a)
    etiket["text"] = liste

etiket = Label(text="Sayı üretmek için düğmeye basın",
    fg="white",
    bg="#61380B",
    font="Helvetica 12 bold")

etiket.pack()

dugme = Button(text="Yeniden",command=kodlar)
dugme.pack()
mainloop()