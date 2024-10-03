class Konto:
    #kontostand = 0
    #kontotyp = ""
    #Problem: obenstehende Eigenschaften sind Klasseneingenschaften -> Variablen stehen allen Instanzen zur Verfügung. Würden Sie sich ändern gilt es global. Deswegen:

#magic method:
    def __init__(self, kontostand, kontotyp):
        self.kontostand = kontostand
        self.kontotyp = kontotyp
    
    def einzahlen (self, betrag):
        #pass
        #Eine Änderung:
        self.kontostand += betrag
    def auszahlen (self, betrag):
        pass