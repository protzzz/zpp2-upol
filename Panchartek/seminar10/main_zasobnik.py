import zasobnik

z1 = zasobnik.vytvor_zasobnik()
zasobnik.pridej_do_zasobniku(z1, "!")
zasobnik.pridej_do_zasobniku(z1, "world")
zasobnik.pridej_do_zasobniku(z1, "Hello")
z2 = zasobnik.vytvor_zasobnik()
zasobnik.pridej_do_zasobniku(z2, "fist")
zasobnik.pridej_do_zasobniku(z2, "second")
zasobnik.pridej_do_zasobniku(z2, "third")

print(zasobnik.odeber_ze_zasobniku(z1))
print(zasobnik.odeber_ze_zasobniku(z1))
print(zasobnik.odeber_ze_zasobniku(z1))
print(zasobnik.odeber_ze_zasobniku(z2))
print(zasobnik.odeber_ze_zasobniku(z2))
print(zasobnik.odeber_ze_zasobniku(z2))

print(zasobnik.odeber_ze_zasobniku(z1))
print(zasobnik.odeber_ze_zasobniku(z2))
zasobnik.pridej_do_zasobniku(z1, "ojdbcvk")
print(zasobnik.odeber_ze_zasobniku(z1))


z3 = zasobnik.vytvor_zasobnik()
zasobnik.pridej_do_zasobniku(z3, "apple")
zasobnik.pridej_do_zasobniku(z3, "samsung")
print(zasobnik.odeber_ze_zasobniku(z3))


# z1 = vytvor_zasobnik()
# pridej_do_zasobniku(z1, "!")
# pridej_do_zasobniku(z1, "world")
# pridej_do_zasobniku(z1, "Hello")
# z2 = vytvor_zasobnik()
# pridej_do_zasobniku(z2, "first")
# pridej_do_zasobniku(z2, "second")
# pridej_do_zasobniku(z2, "third")
# print(odeber_ze_zasobniku(z1))
# print(odeber_ze_zasobniku(z1))
# print(odeber_ze_zasobniku(z1))
# print(odeber_ze_zasobniku(z2))
# print(odeber_ze_zasobniku(z2))
# print(odeber_ze_zasobniku(z2))

# print(odeber_ze_zasobniku(z1))
# print(odeber_ze_zasobniku(z2))

# z3 = vytvor_zasobnik()
# pridej_do_zasobniku(z3, "apple")
# pridej_do_zasobniku(z3, "samsung")
# print(odeber_ze_zasobniku(z3))