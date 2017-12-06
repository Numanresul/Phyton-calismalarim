import sqlite3
baglanti = sqlite3.connect('veriler.db')
baglanti.row_factory = sqlite3.Row
veritabani_sec = baglanti.cursor()
a=raw_input("Gir: ")
veritabani_sec.execute("update ogrenciler set adi='Mert' where adi='%d'"%(a))


oku = veritabani_sec.execute('Select * from %d'%(a))
for verileri_cek in oku.fetchall():
    print(verileri_cek['adi'],verileri_cek['soyadi'],verileri_cek['ogrenci_no'])
#baglanti kapatma ve kaydetme.
baglanti.commit()
baglanti.close()