def factorial(výpočet):
    if výpočet == 0:
        return 1
    else:
        return výpočet*(factorial(výpočet-1))

print(factorial(3))