def vytvor_matici(m, n):
    return [m, n, None, None]

def vloz_prvek(matice, hodnota, radek, sloupec):
    if hodnota == 0:
        return
    
    def najdi_nebo_udelej(lst, index):
        pred, aktualni = None, lst
        while aktualni and aktualni[0] != index:
            pred, aktualni = aktualni, aktualni[1]

        if not aktualni:
            aktualni = [index, None, None]
            if pred:
                pred[1] = aktualni
            else:
                lst = aktualni
        return lst, aktualni

    matice[2], radek_element = najdi_nebo_udelej(matice[2], radek)
    matice[3], sloupec_element = najdi_nebo_udelej(matice[3], sloupec)

    radek_element[2] = pridat_element(radek_element[2], [sloupec, hodnota, None])
    sloupec_element[2] = pridat_element(sloupec_element[2], [radek, hodnota, None])

def pridat_element(seznam, element):
    if not seznam:
        return element

    aktualni = seznam
    while aktualni[2]:
        aktualni = aktualni[2]

    aktualni[2] = element
    return seznam

def print_matrix(matice):
    m, n, rakdy, cols = matice
    for r in range(m):
        radek = []
        for c in range(n):
            hodnota = find_value(rakdy, r, c)
            radek.append(hodnota)
        print(" ".join("{:3}".format(h) for h in radek))

def find_value(rakdy, radek, sloupec):
    aktualni_radek = rakdy
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
vloz_prvek(matice, 16, 3, 1)
print_matrix(matice)
print(matice)
