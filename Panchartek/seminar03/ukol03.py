def mapovani(f, sekvence):
    seznam = []
    for i in sekvence:
        seznam.append(f(i))
    return seznam

print(mapovani(lambda x: x * x,[1,2,3,4,5]))