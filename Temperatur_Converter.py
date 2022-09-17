def ctox(auswahl):  #1/2
    Grad = input("Gebe die zu konvertierende Temperatur ein: ")
    # Celsius nach Kelvin
    if auswahl == "1":
        rechnung = float(Grad) + 273.15
        print(f"{Grad} Grad Celsius sind {rechnung} Grad Kelvin.")
    # Celsius nach Fahrenheit
    elif auswahl == "2":
        rechnung = (int(Grad) * 9/5) + 32
        print(f'{Grad} Celsius sind {rechnung} Grad Fahrenheit')


def ktox(auswahl):  #3/4
    grad = input('Gebe die konvertierung ein: ')
    # Kelvin nach Celsius
    if auswahl == "3":
        rechnung = grad - 273.15
        print(f'{grad} Kelvin sind {rechnung} Grad Celsius.')
    # Kelvin nach Fahrenheit
    elif auswahl == "4":
        rechnung = (float(grad)-273.15)*9/5+32
        print(f'{grad} Kelvin sind {rechnung} Grad Fahrenheit.')


def ftox(auwahl):  #5/6
    grad = input('Gebe die konvertierung ein: ')
    # Fahrenheit nach Celsius
    if auwahl == "5":
        rechnung = (int(grad)-32)*5/9
        print(f'{grad} Fahrenheit sind {rechnung} Grad Celsius.')
    # Fahrenheit nach Kelvin
    elif auswahl == "6":
        rechnung = (int(grad)-32)*5/9+273.15
        print(f'{grad} Fahrenheit sind {rechnung} Kelvin.')

def main():
    while True:
        print("Wähle eine der folgenden Möglichkeiten:"
              "\n(1) Umrechnung von Celsius nach Kelvin"
              "\n(2) Umrechnung von Celsius nach Fahrenheit"
              "\n(3) Umrechnung von Kelvin nach Celsius"
              "\n(4) Umrechnung von Kelvin nach Fahrenheit"
              "\n(5) Umrechnung von Fahrenheit nach Celsius"
              "\n(6) Umrechnung von Fahrenheit nach Kelvin")
        UserSel = input("Was möchtest du tun: ")
        if UserSel == "1" or UserSel == "2":
            ctox(UserSel)
        elif UserSel == "3" or UserSel == "4":
            ktox(UserSel)
        elif UserSel == "5" or UserSel == "6":
            ftox(UserSel)
        elif UserSel == 'q':
            break
        else:
            print("Nicht Möglich.")
main()
