class Ausnahme2:
    def rechne(self):
        
        try:
            print("Eingabe Zahl 1")
            z1 = int(input())
            print("Eingabe Zahl 2")
            z2 = int(input())
            erg = z1 * z2
            print(erg)

        except ValueError:
            print("Bitte nur Zahlen eingeben")
        
