def recursive(zaklad, exponent):
    try:
        if exponent > 997:
            raise AssertionError("The exponent cant have value more than 997")
        elif exponent == 0:
            return 1
        else:
            return zaklad * recursive(zaklad, exponent - 1)
    except AssertionError as e:
        print(e)
    except Exception as e:
        return print("Problem: ", e)

print(recursive(2, 999))