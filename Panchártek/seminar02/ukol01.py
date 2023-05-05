def recursive(zaklad, exponent):
    if exponent == 0:
        return 1
    else:
        return zaklad * recursive(zaklad, exponent - 1)
    
print(recursive(2,5))

def konc_recursive(zaklad, exponent, x = 1):
    if exponent == 0:
        return x
    else:
        return konc_recursive(zaklad, exponent - 1, x * zaklad)

print(konc_recursive(2,4))