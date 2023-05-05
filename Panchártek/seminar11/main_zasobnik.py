import zasobnik

z1 = zasobnik.vytvor_zasobnik(2)
zasobnik.pridej_do_zasobniku(z1, 16)
zasobnik.pridej_do_zasobniku(z1, 65536)
zasobnik.pridej_do_zasobniku(z1, 65535)
zasobnik.pridej_do_zasobniku(z1, 3)
zasobnik.pridej_do_zasobniku(z1, -3)


zasobnik.zapis_do_souboru("zasobnik.bin", z1)
z2 = zasobnik.nacti_ze_souboru("zasobnik.bin")
print(zasobnik.odeber_ze_zasobniku(z2))
print(zasobnik.odeber_ze_zasobniku(z2))
print(zasobnik.odeber_ze_zasobniku(z2))

# Vypíše:
#   hodnota 65536 je mimo povolený rozsah.
#   hodnota -3 je mimo povolený rozsah.
#   16
#   65535
#   2