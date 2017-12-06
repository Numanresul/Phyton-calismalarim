from Tkinter import *

class Arayuz:
    def __init__(self):
        pencere = Tk()
        dugme = Button(text="tamam")
        dugme.pack()
        pencere.mainloop()

    def yaz(self):
        print "Gorusmek Uzere"

uygulama = Arayuz()