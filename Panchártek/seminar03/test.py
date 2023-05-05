def test_all(f, sekvence):
    for i in sekvence:
        if not f(i):
            return False
    return True

sekvence = [1,2,3,4,5,6]
#sekvence = [1,-2,3,-4,5,-6]

test = lambda x : x > 0

print(sekvence)
print(test_all(test, sekvence))
 
print(3 % 4)