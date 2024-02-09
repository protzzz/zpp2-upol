import random

def delka(seznam):
    return delka1(seznam,0)

def delka1(seznam,a):
    if seznam == []:
        return a
    else:
        return delka1(seznam[1:],a+1)
    
# seznam = [random.randint(0,10) for i in range(random.randint(0,10))]
# print(seznam)
print(delka(seznam=[]))
