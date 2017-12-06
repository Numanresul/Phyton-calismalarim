# -*- coding: utf-8 -*-
import sqlite3,os

dosya = 'vt.sqlite'
dosya_mevcut = os.path.exists(dosya)
vt = sqlite3.connect(dosya)
im = vt.cursor()
a=15

im.execute("""CREATE TABLE IF NOT EXISTS faturalar
(fatura, miktar, ilk_odeme_tarihi, son_odeme_tarihi)""")

if not dosya_mevcut:
    im.execute("""INSERT INTO faturalar VALUES
    ("Elektrik", "asdfg", "23 Ocak 2010", "30 Ocak 2010")""")
    vt.commit()

im.execute("""SELECT * FROM faturalar""")
veriler = im.fetchall()
print(veriler)


vt.close()