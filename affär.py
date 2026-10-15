class Produkt:
    def __init__(self, namn, pris, mängd):
        self.namn = namn
        self.__mängd = mängd
        self.pris = pris

    def Lägg_till_produkt(self):
        self.__mängd += 1

    def Ta_bort_produkt(self):
        if self.__mängd > 0:
            self.__mängd -= 1

class Webbshop:
    def __init__(self, produkt):
        self.produkt = produkt

    def Lägg_till_produkter(self):
        for mängd in range(int(input("Mängd: "))):
            self.produkt.Lägg_till_produkt()

    def Ta_bort_produkter(self):
        for mängd in range(int(input("Mängd"))):
            self.produkt.Ta_bort_produkt()