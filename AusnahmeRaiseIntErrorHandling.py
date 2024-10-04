class AusnahmeRaiseIntErrorHandling:
    def __init__(self):
        self.i = 0  # Initialize i as an instance variable
    
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
                try:
                    raise BaseException("Maximale Anzahl an Versuchen überschritten")  # Raise with a message
                except BaseException as e:
                    print(e.args[0], type(e), sep="\t:\t")  # Handle the exception inside the class
                    return  # Exit the method after handling the exception
            
            if input("Ende mit q - weiter mit jeder anderen Taste: ") == "q":             
                break