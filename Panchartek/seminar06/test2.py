def vytvor_matici(m, n):
    return [m, n, 0, 0]

def vloz_prvek(matice, hodnota, radek, sloupec):
    if hodnota == 0:
        return

    def najdi_nebo_vytvor(seznam, index):
        predchozi, aktualni = None, seznam
        while aktualni and aktualni[0] != index:
            predchozi, aktualni = aktualni, aktualni[1]

        if not aktualni:
            aktualni = [index, None, None]
            if predchozi:
                predchozi[1] = aktualni
            else:
                seznam = aktualni
        return seznam, aktualni

    matice[2], radek_element = najdi_nebo_vytvor(matice[2], radek)
    matice[3], sloupec_element = najdi_nebo_vytvor(matice[3], sloupec)

    radek_element[2] = [sloupec, hodnota, radek_element[2]]
    sloupec_element[2] = [radek, hodnota, sloupec_element[2]]

def pridat_element(seznam, element):
    if not seznam:
        return element

    aktualni = seznam
    while aktualni[1]:
        aktualni = aktualni[1]

    aktualni[1] = element
    return seznam

def vypis_matici(matice):
    m, n, radky, sloupce = matice
    for r in range(m):
        radek = []
        for s in range(n):
            hodnota = najdi_hodnotu(radky, r, s)
            radek.append(hodnota)
        print(" ".join("{:3}".format(h) for h in radek))

def najdi_hodnotu(radky, radek, sloupec):
    aktualni_radek = radky
    while aktualni_radek and aktualni_radek[0] != radek:
        aktualni_radek = aktualni_radek[1]

    if not aktualni_radek:
        return 0

    hodnoty = aktualni_radek[2]
    while hodnoty and hodnoty[0] != sloupec:
        hodnoty = hodnoty[2]

    if not hodnoty:
        return 0

    return hodnoty[1]

matice = vytvor_matici(4, 4)
vloz_prvek(matice, 2, 1, 2)
vloz_prvek(matice, 18, 1, 1)
vloz_prvek(matice, 18, 0, 2)
vloz_prvek(matice, 80, 3, 2)
vloz_prvek(matice, 90, 3, 2)
vloz_prvek(matice, 16, 3, 1)
vypis_matici(matice)
print(matice)
