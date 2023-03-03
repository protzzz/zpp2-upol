"""
Naprogramujte funkci mocnina(zaklad, exponent) vracející hodnotu 
zaklad^exponent. Při implementaci funkce nepoužívejte operátor **.
"""
def mocnina(zaklad, exponent):
    vysledek = 1
    for i in range(exponent):
        vysledek *= zaklad
    return vysledek

print(mocnina(3,3))