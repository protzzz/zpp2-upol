def vytvor_zasobnik():
    zasobnik = []
    return zasobnik

def pridej_do_zasobniku(zasobnik, hodnota):
    zasobnik.append(hodnota)
    # try:
    #     if zasobnik:
    #         zasobnik.append(hodnota)
    #     # else:
    #     #     raise ValueError("Zasobnik neexistuje.")
    #     #     # raise NameError("wrong name, take an existing zasobnik")
    # except NameError as e:
    #     print(e)
    # except Exception as e:
    #     print(e.__class__, ": ", e)
        
def odeber_ze_zasobniku(zasobnik):
    if not zasobnik:
        return None
    else:
        for i in zasobnik:
            return zasobnik.pop(-1)
            

z1 = vytvor_zasobnik()
pridej_do_zasobniku(z1, "!")
pridej_do_zasobniku(z1, "world")
pridej_do_zasobniku(z1, "Hello")
z2 = vytvor_zasobnik()
pridej_do_zasobniku(z2, "first")
pridej_do_zasobniku(z2, "second")
pridej_do_zasobniku(z2, "third")
print(odeber_ze_zasobniku(z1))
print(odeber_ze_zasobniku(z1))
print(odeber_ze_zasobniku(z1))
print(odeber_ze_zasobniku(z2))
print(odeber_ze_zasobniku(z2))
print(odeber_ze_zasobniku(z2))

print(odeber_ze_zasobniku(z1))
print(odeber_ze_zasobniku(z2))

z3 = vytvor_zasobnik()
pridej_do_zasobniku(z3, "apple")
pridej_do_zasobniku(z3, "samsung")
print(odeber_ze_zasobniku(z3))
