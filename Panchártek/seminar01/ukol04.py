"""
Napište program, který oveří zda dva zadané seznamy obsahují stejné hodnoty.
Jednotlivé prvky mohou být v jiném pořadí. Pozor na případy, kdy se hodnoty opakují.
"""
import random
seznam1 = [1,2,3,4,5]
seznam2 = [5,3,2,4,1,1]
seznam3 = []
for i in seznam1:
    if i in seznam3:
        continue
    for j in seznam2:
        if i == j:
            seznam3.append(i)
            break

# seznam1 = [1,2,3,1]
# seznam2 = [1,3,2,4]
# print(seznam1)
# print(seznam2)

# def porovnany(seznam1, seznam2):  
#     if set(seznam1) == set(seznam2):
#         return True
#     else:
#         return False

# print(porovnany(seznam1, seznam2))