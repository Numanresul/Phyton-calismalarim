# -*- coding: utf-8 -*-
import sqlite3,os
from Tkinter import *


dosya = 'vt.sqlite'
dosya_mevcut = os.path.exists(dosya)
vt = sqlite3.connect(dosya)
im = vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS faturalar
(fatura, miktar, ilk_odeme_tarihi, son_odeme_tarihi)""")

pencere = Tk()

liste = Listbox(bg="white")
liste.pack()

def listele():
    im.execute("""SELECT * FROM faturalar""")
    veriler = im.fetchall()
    for i in veriler:
        liste.insert(END, i)

def yeni():
    global giris
    pencere2 = Toplevel()
    giris = Entry(pencere2)
    giris.pack()
    btn2 = Button(pencere2, text="tamam",command=ekle)
    btn2.pack()

def ekle():
    if not giris.get():
        giris.insert(END, "Veri Yok!")
    if not "Veri Yok!" in giris.get():
        im.execute('''INSERT INTO faturalar (fatura, miktar, ilk_odeme_tarihi, son_odeme_tarihi) VALUES ('%s','Ali','Yaman','mert')''' %(giris.get()))
        vt.commit()
        liste.delete(0,END)
        listele()
        giris.delete(0, END)

def sil():
    c = liste.get(ACTIVE)
    a = c[0]
    im.execute("""DELETE from faturalar where fatura='%s'""" % (a))
    vt.commit()
    liste.delete(0, END)
    listele()

listele()
etiket = Label(text="#################", fg="magenta", bg="light green")
etiket.pack()

btn = Button(text="ekle", bg="orange", fg="navy", command=yeni)
btn.pack()
btn_sil = Button(text="sil", bg="orange", fg="navy",command=sil)
btn_sil.pack()

etiket2 = Label(text="#################", fg="magenta", bg="light green")
etiket2.pack()

mainloop()
vt.close()