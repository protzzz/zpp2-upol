def pascal(radek, sloupec):
    if sloupec == 0 or sloupec == radek:
        return 1
    else:
        return pascal(radek - 1, sloupec - 1) + pascal(radek - 1, sloupec)
print(pascal(0,0))
print(pascal(3,3))
print(pascal(6,2))
print(pascal(7,2))