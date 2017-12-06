import sqlite3
baglanti = sqlite3.connect('veriler.db')
if(baglanti):
    print('Baglanti Basarili!')
else:
    print('Baglanti Basarisiz!')
#baglanti kurulan veriyi sec.
veritabani_sec = baglanti.cursor()
#secili olan veritabanin verileri okuyalim
oku = veritabani_sec.execute('SELECT * FROM ogrenciler')
print(oku.fetchall())

#yada
ku = veritabani_sec.execute('SELECT adi,soyadi,ogrenci_no from ogrenciler')
for verileri_cek in oku.fetchall():
    print('Ad Soyad : %s %s - Okul NO : %s'%verileri_cek)

baglanti.commit()
baglanti.close()