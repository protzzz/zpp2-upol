def test_all(f, sequence):
    try:
        for i in sequence:
            if not f(i):
                return False
    except Exception as e:
        print("An error is:", e)
        return False
    return True

sequence = [1, 2, 3, 4, 5, 6]

test = lambda x: x > 0

print("Sequence:", sequence)
try:
    print("Result:", test_all(test, sequence))
except Exception as e:
    print("Problem while running the test_all function:", e)
