def test_any(f, sekvence):
    for i in sekvence:
        if f(i):
            return True
    return False

#sekvence = [-1,-2,-3,-4,-5,-6]
sekvence = [-1,-2,-3,-4,-5,-6]

test = lambda x : x > 0
print(test_any(test, sekvence))