def vytvor_zasobnik(bytes):
    return [[bytes]]


def pridej_do_zasobniku(zasobnik, pocet_bitu):
    mypocet_bitu = pocet_bitu
    j = 0   
    temp = pocet_bitu
    try:
        if pocet_bitu < 0:
            print(f"hodnota {pocet_bitu} je mimo povolený rozsah.")
            return zasobnik
    except TypeError:
        print(f"hodnota {pocet_bitu} musi byt jenom kladné čislo.")
        return zasobnik
    while mypocet_bitu:
        mypocet_bitu = mypocet_bitu >> 8
        j += 1  
    if zasobnik[0][0] < j:
        print(f"hodnota {pocet_bitu} je mimo povolený rozsah.")
        return zasobnik
    else:
        zasobnik.append(temp)

    return zasobnik

def zapis_do_souboru(file, zasobnik):
    bytes_array = []
    for i in zasobnik[1:]:
        temp = []
        if i:
            while i:
                byte = i & 0xff
                temp.append(byte)
                i = i >> 8
        else:
            temp.append(0)
        bytes_array.append(temp[::-1])

    with open(file,"wb") as f:
        f.write(bytes(zasobnik[0]))
        f.write(b"\n")
        for j in bytes_array:
            f.write(bytes(j))
            f.write(b"\n")

def nacti_ze_souboru(file):
    seznam = []
    temp = []
    soubor = open(file, "rb")
    while True:
        line = soubor.readline()
        for i in line:
            if i == 10:
                seznam.append(temp)
                temp = []
                break
            temp.append(i)
        if not line:
            break
    pocet_bytes = seznam[0][0]
    zasobnik = vytvor_zasobnik(pocet_bytes)
    number = 0
    for byte in seznam[1:]:
        for j in byte: 
            number = number << 8
            number = number | j
        pridej_do_zasobniku(zasobnik, number)
        number = 0
    return zasobnik

def odeber_ze_zasobniku(zasobnik):
    if len(zasobnik) == 1:
        return None
    else:
        temp = zasobnik[-1]
        zasobnik.remove(temp)
    return temp


