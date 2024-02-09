def vytvor_zasobnik(bajt):
    zasobnik = [[bajt]]
    return zasobnik


def pridej_do_zasobniku(zasobnik, cislo):
    if zasobnik:
        pocet_bajtu = zasobnik[0][0]
        rozsah = 2 ** (pocet_bajtu * 8)
        if 0 <= cislo < rozsah:
            zasobnik.append(cislo)
        else:
            print(f"Hodnota {cislo} je mimo povolený rozsah.")
    elif not zasobnik:
        print(f"Tento zásobník {zasobnik} neexistuje. Vytvořte nový!!!")
    return zasobnik


def odeber_ze_zasobniku(zasobnik):
    if len(zasobnik) > 1:
        last = zasobnik[-1]
        del zasobnik[-1]
        # zasobnik.remove(last)
        return last
    return None

def zapis_do_souboru(file, zasobnik):
    def int_to_bytes(num, byte_count):
        byte_list = []
        for i in range(byte_count):
            byte = num & 0xff
            byte_list.append(byte)
            num >>= 8
        return byte_list[::-1]

    byte_count = zasobnik[0][0]
    byte_data = [int_to_bytes(num, byte_count) for num in zasobnik[1:]]

    with open(file, "wb") as file:
        file.write(bytes([byte_count]))
        for byte_list in byte_data:
            for byte in byte_list:
                file.write(bytes([byte]))


def nacti_ze_souboru(file):
    def bytes_to_int(byte_list):
        result = 0
        for byte in byte_list:
            result = (result << 8) + byte
        return result

    with open(file, "rb") as file:
        byte_count = file.read(1)[0]
        file_content = file.read()
        numbers = []
        for i in range(0, len(file_content), byte_count):
            number = file_content[i:i+byte_count]
            # print(number)
            numbers.append(number)

    zasobnik = [[byte_count]]
    for number in numbers:
        zasobnik.append(bytes_to_int(number))
    return zasobnik

hello = vytvor_zasobnik(2)
pridej_do_zasobniku(hello, 10)
pridej_do_zasobniku(hello, 65535)
pridej_do_zasobniku(hello, 900)
print(hello)
zapis_do_souboru("zasobnik.bin", hello)
bye = nacti_ze_souboru("zasobnik.bin")
print(odeber_ze_zasobniku(bye))
print(odeber_ze_zasobniku(bye))
print(odeber_ze_zasobniku(bye))
print(bye)