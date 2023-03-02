#Naprogramujte rekurzivní i koncově rekurzivní mocnina
#(zaklad, exponent) vracející hodnotu zakladexponent. 
#Při implementaci funkce nepoužívejte operátor **.

def power(n,m):
    if m == 1:
        return n
    elif m != 1:
        return (m * power(n,m-1))

#Napište „hloupou“ funkci na výpočet součtu 
#prvků intervalu celých čísel.

def add(n):
    if n == 0:
        return 0
    elif n != 0:
        return n + add(n-1)


#Napište rekurzivní funkci pro výpočet faktoriálu zadaného čísla n.

#Napište koncově rekurzivní funkci pro
#výpočet faktoriálu zadaného čísla n.

#Napište rekurzivní funkci pro výpočet délky seznamu.

#Napiště rekurzivní funkci pascal která vypočítá daný 
#prvek pascalova trojúhelníka.
