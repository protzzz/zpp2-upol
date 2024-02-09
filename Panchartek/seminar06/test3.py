class Prvek:
    def __init__(self, hodnota, radek, sloupec):
        self.hodnota = hodnota
        self.radek = radek
        self.sloupec = sloupec
        self.dalsi_radek = None
        self.dalsi_sloupec = None


def vytvor_matici(pocet_radku, pocet_sloupcu):
    prvni_radek = Prvek(None, 0, 0)
    posledni_radek = prvni_radek
    prvni_sloupec = Prvek(None, 0, 0)
    posledni_sloupec = prvni_sloupec

    for i in range(pocet_radku):
        radek = Prvek(None, i, 0)
        posledni_radek.dalsi_radek = radek
        posledni_radek = radek
        for j in range(1, pocet_sloupcu):
            prvek = Prvek(None, i, j)
            posledni_radek.dalsi_sloupec = prvek
            posledni_radek = prvek

    for j in range(pocet_sloupcu):
        sloupec = Prvek(None, 0, j)
        posledni_sloupec.dalsi_sloupec = sloupec
        posledni_sloupec = sloupec
        for i in range(1, pocet_radku):
            prvek = Prvek(None, i, j)
            posledni_sloupec.dalsi_radek = prvek
            posledni_sloupec = prvek

    return prvni_radek, prvni_sloupec


def vloz_prvek(prvni_prvek, hodnota, radek, sloupec):
    aktualni_prvek = prvni_prvek
    while aktualni_prvek is not None:
        if aktualni_prvek.radek == radek and aktualni_prvek.sloupec == sloupec:
            aktualni_prvek.hodnota = hodnota
            return
        if aktualni_prvek.dalsi_radek is None or aktualni_prvek.dalsi_radek.radek > radek:
            novy_prvek = Prvek(hodnota, radek, sloupec)
            novy_prvek.dalsi_radek = aktualni_prvek.dalsi_radek
            aktualni_prvek.dalsi_radek = novy_prvek
            return
        aktualni_prvek = aktualni_prvek.dalsi_radek


def zobraz_matici(prvni_radek, prvni_sloupec):
    aktualni_radek = prvni_radek
    for i in range(prvni_sloupec.sloupec):
        print('{:4d}'.format(i), end='')
    print()
    while aktualni_radek is not None:
        aktualni_sloupec = aktualni_radek
        print('{:4d}'.format(aktualni_radek.radek), end='')
        while aktualni_sloupec is not None:
            if aktualni_sloupec.hodnota is None:
                print('    ', end='')
            else:
                print('{:4d}'.format(aktualni_sloupec.hodnota), end='')
            aktualni_sloupec = aktualni_sloupec.dalsi_sloupec
        print()
        aktualni_radek = aktualni_radek.dalsi_radek



               
prvni_radek, prvni_sloupec = vytvor_matici(4, 4)

vloz_prvek(prvni_radek, 1, 0, 1)
vloz_prvek(prvni_radek, 18, 0, 2)
vloz_prvek(prvni_radek, 3, 2, 2)

zobraz_matici(prvni_radek, prvni_sloupec)
