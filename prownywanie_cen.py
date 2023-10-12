class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena


class Zamowienie:
    def __init__(self, produkty: list):
        self.produkty = produkty

    def koszt(self) -> float:
        """Liczy koszt zamówienie zastosowaniu po promocji dla 5 produktów,
        zależny od ilości kupowanych produktów w 1 zamówieniu"""
        if len(self.produkty) == 5:
            return (self.sumuj(self.produkty[0:4]) + 1) + 100
        if len(self.produkty) == 4:
            return (self.sumuj(self.produkty[0:3]) + (0.2 * self.produkty[3].cena)) + 100
        if len(self.produkty) == 3:
            return (self.sumuj(self.produkty[0:2]) + (0.45 * self.produkty[2].cena)) + 100
        if len(self.produkty) == 2:
            return (self.sumuj(self.produkty[0:1]) + (0.7 * self.produkty[1].cena)) + 100
        return self.sumuj(self.produkty) + 100

    @staticmethod
    def sumuj(produkty: list) -> int:
        """Sumuje ceny określonej listy produktów"""
        suma = 0
        for p in produkty:
            suma += p.cena
        return suma


def generuj_kombinacje(produkty: list) -> list:
    """Generuje wszystkie możliwe kombinacje zamówień"""
    for p1 in range(min(5, len(produkty)), 0, -1):
        z1 = Zamowienie(produkty[0:p1])

        pozostale = produkty[p1:]
        if len(pozostale) == 0:
            yield [z1]
        elif len(pozostale) == 1:
            yield [z1, Zamowienie(pozostale)]
        else:
            for lista_zamowien in generuj_kombinacje(pozostale):
                yield [z1] + lista_zamowien


produkty = [Produkt("lodowka", 5000),
            Produkt("zmywarka", 2800),
            Produkt("pralka", 2100),
            Produkt("piekarnik", 2000),
            Produkt("zlew", 1269),
            Produkt("plyta", 1100),
            Produkt("mokrofalowka", 1000),
            Produkt("okap", 700),
            ]

wyjsciowe_zamowienie = Zamowienie(produkty)
najtansza_kombinacja = [wyjsciowe_zamowienie]
najtaniej = wyjsciowe_zamowienie.koszt()
print(f"Bez promocji: {najtaniej}")

for kombinacja in generuj_kombinacje(produkty):
    koszt = 0
    for zamowienie in kombinacja:
        koszt += zamowienie.koszt()
    if koszt < najtaniej:
        najtaniej = koszt
        najtansza_kombinacja = kombinacja
print(f"Najtańsza opcja: {najtaniej}")
print(f"Obniżka: {wyjsciowe_zamowienie.koszt() - najtaniej} \n")

for zamowienie in najtansza_kombinacja:
    print(f'Zamowienie ({zamowienie.koszt()}): ', end="")
    for produkt in zamowienie.produkty:
        print(produkt.nazwa + ", ", end="")
    print("")
