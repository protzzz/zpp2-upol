def vytvor_zasobnik(bajt):
    zasobnik = [[bajt]]
    return zasobnik


def pridej_do_zasobniku(zasobnik, cislo):
    if zasobnik:
        max_cislo = 1
        for i in range(zasobnik[0][0]):
            max_cislo *= 0xff + 1
        if 0 <= cislo and cislo < max_cislo:
            zasobnik.append(cislo)
        else:
            print(f"hodnota {cislo} je mimo povolený rozsah.")
    elif not zasobnik:
        print(f"zasobnik {zasobnik} doesn't exist! create one.")
    return zasobnik


def odeber_ze_zasobniku(zasobnik):
    if len(zasobnik) == 1:
        return None
    else:
        last = zasobnik[-1]
        # zasobnik = zasobnik[:-1]
        zasobnik.remove(last)
    return last


def zapis_do_souboru(file, zasobnik):
    def int_to_bytes(num):
        byte_list = []
        if num == 0:
            byte_list.append(0)
        else:
            while num:
                byte_list.append(num & 0xff)
                num >>= 8
        return byte_list[::-1]

    byte_data = [int_to_bytes(num) for num in zasobnik[1:]]

    with open(file, "wb") as file:
        file.write(bytes(zasobnik[0]))
        file.write(b"\n")
        for byte_list in byte_data:
            file.write(bytes(byte_list))
            file.write(b"\n")
            
def nacti_ze_souboru(file):
    def bytes_to_int(byte_list):
        cislo = 0
        for byte in byte_list:
            cislo = (cislo << 8) + byte
        return cislo

    with open(file, "rb") as file:
        lines = file.read().split(b'\n')

    zasobnik = [[lines[0][0]]]
    for i in lines[1:]:
        if i:
            zasobnik.append(bytes_to_int(i))

    return zasobnik

hello = vytvor_zasobnik(2)
pridej_do_zasobniku(hello, 16)
pridej_do_zasobniku(hello, 65535)
pridej_do_zasobniku(hello, 16)
pridej_do_zasobniku(hello, 3)
print(hello)
zapis_do_souboru("zasobnik.bin", hello)
bye = nacti_ze_souboru("zasobnik.bin")
print(odeber_ze_zasobniku(bye))
print(odeber_ze_zasobniku(bye))
print(odeber_ze_zasobniku(bye))
print(odeber_ze_zasobniku(bye))
print(odeber_ze_zasobniku(bye))
print(bye)
