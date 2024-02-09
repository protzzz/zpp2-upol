PREDCHOZI_PRVEK = 0
HODNOTA = 1
DALSI_PRVEK = 2
seznam = []

def pridej_do_obousmerneho_seznamu(seznam, x):
    predchozi_prvek = []
    while seznam:
        predchozi_prvek = seznam
        seznam = seznam[DALSI_PRVEK]
    seznam.extend([predchozi_prvek, x, []])

pridej_do_obousmerneho_seznamu(seznam,1)
pridej_do_obousmerneho_seznamu(seznam,2)
pridej_do_obousmerneho_seznamu(seznam,3)
pridej_do_obousmerneho_seznamu(seznam,4)
print(seznam)

def odeber_z_obousmerneho_seznamu(seznam, x):
    if seznam[HODNOTA] == x:
        seznam[HODNOTA] = seznam[DALSI_PRVEK]
        return
    while seznam[DALSI_PRVEK]:
        if seznam[DALSI_PRVEK][HODNOTA] == x and seznam[DALSI_PRVEK][DALSI_PRVEK]:
            seznam[DALSI_PRVEK] = seznam[DALSI_PRVEK][DALSI_PRVEK]
            seznam = seznam[DALSI_PRVEK]
            seznam[PREDCHOZI_PRVEK] = seznam[PREDCHOZI_PRVEK][PREDCHOZI_PRVEK]
            return
        elif seznam[DALSI_PRVEK][HODNOTA] == x and not seznam[DALSI_PRVEK][DALSI_PRVEK]:
            seznam[DALSI_PRVEK] = seznam[DALSI_PRVEK][DALSI_PRVEK]
            return
        else:
            seznam = seznam[DALSI_PRVEK]


odeber_z_obousmerneho_seznamu(seznam,2) 
odeber_z_obousmerneho_seznamu(seznam,3)


print(seznam)