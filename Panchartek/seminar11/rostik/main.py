import zasobnik

z1 = zasobnik.vytvor_zasobnik(2)
zasobnik.pridej_do_zasobniku(z1, "5999")
zasobnik.pridej_do_zasobniku(z1, 65535)
zasobnik.pridej_do_zasobniku(z1, 65536)
zasobnik.pridej_do_zasobniku(z1, 111)
zasobnik.pridej_do_zasobniku(z1,-11)

zasobnik.zapis_do_souboru("soubor.bin", z1)
z2 = zasobnik.nacti_ze_souboru("soubor.bin")
print(z2)
print(zasobnik.odeber_ze_zasobniku(z2))
print(zasobnik.odeber_ze_zasobniku(z2))
print(zasobnik.odeber_ze_zasobniku(z2))
print(zasobnik.odeber_ze_zasobniku(z2))
print(zasobnik.odeber_ze_zasobniku(z2))
z3 = zasobnik.nacti_ze_souboru("soubor.bin")
zasobnik.pridej_do_zasobniku(z3, 131)
zasobnik.pridej_do_zasobniku(z3, 999)
zasobnik.pridej_do_zasobniku(z3, -3)
zasobnik.pridej_do_zasobniku(z3, 6555)
zasobnik.zapis_do_souboru("soubor.bin", z3)
z4 = zasobnik.nacti_ze_souboru("soubor.bin")
print(z4)





