def bits_count(number):
    bin_cislo = bin(number)
    res = 0
    if bin_cislo[0] == "-":
        for i in bin_cislo[3:]:
            res += 1
    else:
        for i in bin_cislo[2:]:
            res += 1
    return res

print(bits_count(-4))