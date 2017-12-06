# -*- coding: utf-8 -*-

def asalsayi(sayi,sayi1):
        for i in range(sayi,sayi1):
            bolundu = False
            for j in range(2,i):
                if i%j==0:
                    bolundu = True
                    break
            if bolundu == False:
                print(i)
                print("Asal sayıdır")
            elif bolundu==True:
                print(i)
                print("Asal sayı değildir")
            elif bolundu==True:
                print(i)
                print("Asal sayı değildir")

sayi = int(raw_input("Birinci sayı giriniz"))
sayi1 = int(raw_input(("İkinci sayıyı giriniz:")))
asalsayi(sayi,sayi1)

