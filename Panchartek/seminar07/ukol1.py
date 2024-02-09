def mocnina(zaklad, exponent):
    vysledek = 1
    try:
        if not isinstance(exponent, int) or not isinstance(zaklad, int):
            raise TypeError("Exponent must be an integer!!!")
        elif zaklad == 0 and exponent <= 0:
            raise ZeroDivisionError("Cannot raise 0 to a non-positive power!!!")
        elif zaklad < 0 and exponent % 2 == 1:
            raise ValueError("Negative base with odd exponent results in a complex number!!!")
        for i in range(exponent):
            vysledek *= zaklad
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(e)
        vysledek = None
    except Exception as e:
        print(Exception.__class__, e)
        vysledek = None
    finally:
        return vysledek

# print('vysledek je', mocnina(2,'a'))
# print('vysledek je', mocnina('a',2))
# print('vysledek je', mocnina(-2,3))
print('vysledek je', mocnina(5,2))