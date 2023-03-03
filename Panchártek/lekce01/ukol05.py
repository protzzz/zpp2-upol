"""
Napište program, který vypíše číslo zadané v desítkové soustavě jako binární číslo.
"""

def desitkove(number):
    vysledek = ''

    while number > 0:
        vysledek = str(number%2) + vysledek
        number = number // 2

    return print(vysledek) 

desitkove(7)
    

