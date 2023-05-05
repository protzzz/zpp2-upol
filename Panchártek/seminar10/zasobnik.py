def vytvor_zasobnik():
    zasobnik = []
    return zasobnik

def pridej_do_zasobniku(zasobnik, hodnota):
    zasobnik.append(hodnota)
        
def odeber_ze_zasobniku(zasobnik):
    if not zasobnik:
        return None
    else:
        for i in zasobnik:
            return zasobnik.pop(-1)