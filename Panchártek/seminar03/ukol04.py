def aplikuj(f, sekvence):
    result = sekvence[0]
    for i in sekvence[1:]:
        result = f(result, i)
    return result

print(aplikuj(lambda x,y: x+y,[1, 2, 3, 4, 5]))