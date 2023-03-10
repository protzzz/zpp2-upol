def factorial_konc(n, result=1):
    if n == 0:
        return result
    else:
        return factorial_konc(n-1, result*n)

print(factorial_konc(3))