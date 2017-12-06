#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *

pencere = Tk()

etiket = Label(text = "Hata: Bellek Read Olamadı!")
etiket.pack()

def olustur():
    dosya = open("deneme.txt", "w")

dugme = Button(text = "oluştur", command=olustur)
dugme.pack(side=LEFT)
dugme2 = Button(text = "çıkış", command=pencere.quit)
dugme2.pack(side=RIGHT)

cerceve = Frame()
cerceve.pack(pady=10)

def sil():
    giris.delete(0, END)

giris = Entry()
giris.pack()

dugme1 = Button(text = "KAPAT", command = pencere.quit)
dugme1.pack(side = LEFT)

dugme2 = Button(text = "SİL", command = sil)
dugme2.pack(side = RIGHT)


liste = Listbox(bg="white")
liste.pack()

gnulinux_dagitimlari = ["Pardus", "Debian", "Ubuntu", "PclinuxOS",
"TruvaLinux", "Gelecek Linux"]

for i in gnulinux_dagitimlari:
    liste.insert(END, i)

etiket = Label(text="#####################",
    fg="magenta", bg="light green")
etiket.pack()

btn = Button(text="ekle", bg="orange", fg="navy")
btn.pack()

etiket2 = Label(text="#####################",
    fg="magenta", bg="light green")
etiket2.pack()


mainloop()