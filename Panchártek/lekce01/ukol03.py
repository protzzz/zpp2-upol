"""
Napište program, který pro zadanou hodnotu n vytvoří matici obsahující 
převrácenou diagonálu.

Výstup pro n = 8
    [[0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0]]
"""
n = 5

#seznam = [[0 for i in range(n)] for j in range(n)]
seznam = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    seznam.append(row)

for i in range(n):
    seznam[i][n-1-i] = 1

for vysledek in seznam:
    print(vysledek)