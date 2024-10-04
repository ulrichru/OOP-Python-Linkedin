class AusnahmeRaise:
    i = 0
    
    def verifiziere(self):
        while True:    
            try:
                geheimzahl = int(input("Bitte Geheimzahl eingeben:\n"))
                if (geheimzahl % 7 != 0):
                    self.i += 1
                else:
                    print("Zugang gestattet")
                    return
            except ValueError:
                print("Nur Zahlen eingeben")
                self.i += 1
            
            # Check if the number of attempts exceeds 2
            if self.i > 2:
                raise BaseException("Maximale Anzahl an Versuchen überschritten")  # Raise with a message
            
            if input("Ende mit q - weiter mit jeder anderen Taste: ") == "q":             
                break

# Example of how to use the class
