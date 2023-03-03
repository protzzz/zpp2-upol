"""
Napište program, který oveří zda dva zadané seznamy obsahují stejné hodnoty.
Jednotlivé prvky mohou být v jiném pořadí. Pozor na případy, kdy se hodnoty opakují.
"""

import random

seznam1 = [random.randint(0,10) for i in range(10)]
seznam2 = [random.randint(0,10) for i in range(10)]
seznam3 = []

print(seznam1)
print(seznam2)

for i in seznam1:
    if i in seznam3:
        continue
    for j in seznam2:
        if i == j:
            seznam3.append(i)
            break
    
print(seznam3)