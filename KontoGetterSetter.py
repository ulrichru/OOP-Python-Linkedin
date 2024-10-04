class KontoGetterSetter:
    def __init__(self,kontostand, kontotyp):
        self.__kontostand = kontostand
        self.__kontotyp = kontotyp
        
    def einzahlen(self, betrag):
        self.__kontostand = self.__kontostand + betrag
    def auszahlen(self, betrag):
        self.__kontostand = self.__kontostand + betrag
    def getKontostand(self):
        return self.__kontostand
    
