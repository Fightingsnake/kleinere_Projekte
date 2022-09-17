import Grundfunktionen
from time import sleep
import random
import string

class Passwort:
    def __init__(self, laenge=6, zahlen=True, sonderzeichen=False):
        self.laenge = laenge
        self.passwort = ''  # ergebnis
        self.zahlen = zahlen
        self.sonderzeichen = sonderzeichen
        self.buchstabe = string.ascii_letters
        self.ziffer = string.digits
        self.zeichen = ['.', ',', '!', '?', '-', '_']


    @property
    def laenge(self):
        return self.__laenge

    @laenge.setter
    def laenge(self, laenge):
        self.__laenge = laenge


    def generieren(self):
        zahl = Grundfunktionen.abfrageJaNein('Sollen Zahlen enthalten sein?')
        if zahl is True:
            self.zahlen = True
        else:
            self.zahlen = False
        sonder = Grundfunktionen.abfrageJaNein('Sollen Sonderzeichen enthalten sein?')
        if sonder is True:
            self.sonderzeichen = True
        else:
            self.sonderzeichen = False
        while True:
            lang = input('Wie lang soll das Passwort werden? (min 4 / max 20) ')
            try:
                lang = int(lang)
                if lang <= 3:
                    print('Die angegebene Zahl ist zu kurz.')
                elif 4 <= lang <= 20:
                    self.laenge = lang
                    break
                elif lang >= 21:
                    print('Die angegebene Zahl ist zu lang.')
            except ValueError:
                print("Die Eingabe war nicht in Ordnung.")
        verzA = [self.buchstabe, self.ziffer, self.zeichen]
        verzB = [self.buchstabe, self.ziffer]
        verzC = [self.buchstabe, self.zeichen]
        verzD = [self.buchstabe]
        i = 0
        if self.zahlen is True and self.sonderzeichen is True:
            while i < self.laenge:
                a = random.choice(verzA)
                b = len(a)-1
                self.passwort += a[random.randint(0, b)]
                i+=1
        elif self.zahlen is True and self.sonderzeichen is False:
            while i < self.laenge:
                a = random.choice(verzB)
                b = len(a)-1
                self.passwort += a[random.randint(0, b)]
                i+=1
        elif self.zahlen is False and self.sonderzeichen is True:
            while i < self.laenge:
                a = random.choice(verzC)
                b = len(a)-1
                self.passwort += a[random.randint(0, b)]
                i+=1
        elif self.zahlen is False and self.sonderzeichen is False:
            while i < self.laenge:
                a = random.choice(verzD)
                b = len(a)-1
                self.passwort += a[random.randint(0, b)]
                i+=1
        print(f"Das Passwort lautet: {self.passwort}")



x = Passwort()
x.generieren()
