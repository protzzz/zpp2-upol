HODNOTA = 0 
DALSI_PRVEK = 1 
seznam = []

def pridej_do_seznamu(seznam, x):
    while seznam:
        seznam = seznam[DALSI_PRVEK]
    seznam.extend([x, []])
   
pridej_do_seznamu(seznam, 1)
pridej_do_seznamu(seznam, 2)
pridej_do_seznamu(seznam, 3)
pridej_do_seznamu(seznam, 4)

print(seznam)

def odeber_ze_seznamu(seznam, x):
    if seznam[HODNOTA] == x:
        seznam[:] = seznam[DALSI_PRVEK]
        return
    while seznam[DALSI_PRVEK]:
        if seznam[DALSI_PRVEK][HODNOTA] == x:
            seznam[DALSI_PRVEK] = seznam[DALSI_PRVEK][DALSI_PRVEK]
            return 
        else:
            seznam = seznam[DALSI_PRVEK]

odeber_ze_seznamu(seznam, 3)
odeber_ze_seznamu(seznam, 1)
pridej_do_seznamu(seznam, 6)
print(seznam)
odeber_ze_seznamu(seznam, 4)
odeber_ze_seznamu(seznam, 2)
print(seznam)
