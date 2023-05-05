"""
Napište program, který vypíše číslo zadané v desítkové soustavě jako binární číslo.
"""

number = 10
# number = "10"
# number = 0
# number = ""


def desitkove(number):
    vysledek = ''
    try:
        if number <= 0:
            raise ValueError("Number must be more than 0!!!")
        while number > 0:
            vysledek = str(number%2) + vysledek
            number = number // 2
    except (TypeError, Exception, ValueError) as e:
        print(e.__class__, '\n' , e)
    finally:
        return vysledek 

if number == "":
    print("Full the number field")
else:
    try:
        if number.__class__ == str:
            raise TypeError("It must contains integer only!")
        else:
            print(desitkove(number))
    except TypeError as e:
        print(e)
    except Exception as e:
        print("The problem is", e)