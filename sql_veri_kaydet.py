import sqlite3
baglanti = sqlite3.connect('veriler.db')
if(baglanti):
    print('Baglanti Basarili!')
else:
    print('Baglanti Basarisiz!')

#baglanti kurulan veriyi sec.
veritabani_sec = baglanti.cursor()

#secili veritabanina sql sorgu yolluyoruz.
veritabani_sec.execute('''
CREATE TABLE IF NOT EXISTS ogrenciler(
kayit_no INTEGER PRIMARY KEY,
ogrenci_no INTEGER NOT NULL ,
adi VARCHAR(50),
soyadi VARCHAR(50)
)
''')

#secili veritabanina veri ekliyoruz.
veritabani_sec.execute('''INSERT INTO ogrenciler (ogrenci_no,adi,soyadi) VALUES ('1234','Ali','Yaman')''')
veritabani_sec.execute('''INSERT INTO ogrenciler (ogrenci_no,adi,soyadi) VALUES ('3456','asdsadsa','asdasd')''')
baglanti.commit()
baglanti.close()