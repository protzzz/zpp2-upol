def soucet_prvku(od,do):
    if od > do:
        return 0 
    else:
        return od + soucet_prvku(od + 1, do)

print(soucet_prvku(0,10))