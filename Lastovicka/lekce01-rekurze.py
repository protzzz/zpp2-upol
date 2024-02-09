# Uvažujeme jen celá nezáporná čísla.

def add(n, m):
    """Sečte zadaná čísla."""
    if m == 0:
        return n
    else:
        return add(n, m - 1) + 1

"""
>>> add(3, 4)
7
"""


def sub(n, m):
    """Spočítá rozdíl čísel."""
    if m == 0:
        return n
    else:
        return sub(n, m - 1) - 1

"""
>>> sub(5, 4)
1
"""


def mult(n, m):
    """Spočítá součin čísel."""
    if m == 0:
        return 0
    else:
        return add(mult(n, m - 1), n)

"""
mult(3, 4)
12
"""


def are_equal(n, m):
    """Rozhodne, zda se čísla rovnají."""
    if n == 0 and m == 0:
        return True
    elif n == 0 or m == 0:
        return False
    else:
        return are_equal(n - 1, m - 1)

"""
>>> are_equal(5, 3)
False
>>> are_equal(3, 3)
True
"""


def is_leq(n, m):
    """Rozhodne, zda je číslo `n` menší nebo rovno než `m`."""
    if n == 0:
        return True
    elif m == 0:
        return False
    else:
        return is_leq(n - 1, m - 1)

"""
>>> is_leq(3, 5)
True
>>> is_leq(5, 3)
False
>>> is_leq(3, 3)
True
"""

def are_equal2(n, m):
    """Rozhodne, zda se čísla rovnají."""
    return is_leq(n, m) and is_leq(m, n)

def is_less(n, m):
    """Rozhodne, zda je n menší než m."""
    return is_leq(n, m) and not is_leq(m, n)

"""
>>> is_less(3, 3)
False
>>> is_less(3, 4)
True
>>> is_less(4, 2)
False
"""

def div(n, m):
    """Spočítá celočíselný podíl zadaných čísel."""
    if is_less(n, m):
        return 0
    else:
        return div(sub(n, m), m) + 1

"""
>>> div(10, 3)
3
"""


def rem(n, m):
    """Spočítá zbytek po celočíselném podílu."""
    if is_less(n, m):
        return n
    else:
        return rem(sub(n, m), m)

"""
>>> rem(10, 3)
1
>>> rem(10, 5)
0
"""


def power(n, m):
    """Spočítá mocninu."""
    if m == 0:
        return 1
    else:
        return mult(power(n, m - 1), n)

"""
>>> power(2, 4)
16
>>> power(5, 2)
25
"""
    
def get_factorial(n):
    """Vrátí faktoriál zadaného čísla."""

# 0! = 1
# n! = n * (n - 1)!

"""
>>> factorial(5)
120
"""

def get_gcd(n, m):
    """Vrátí největšího společného dělitele zadaných čísel."""

"""
>>> get_gcd(12, 8)
4
"""

def sum_interval(a, b):
    """Vrátí součet celých čísel v intervalu."""


"""
>>> sum_interval(2, 4)
9
"""

# Celá část druhé odmocniny zadaného čísla.
# 16 -> 4
# 17 -> 4
#
# Rozhodněte, zda je číslo součtem dvou čtverců.
# 8 -> True
# 7 -> False




def get_fibonacci(n):
    """Vrátí n plus prvé Fibonacciho číslo."""


"""
>>> get_fibonacci(5)
5
"""


def get_fibonacci2_iter(n, a, b):
    """Pomocná funkce."""



def get_fibonacci2(n):
    """Vrátí n plus prvé Fibonacciho číslo."""

"""
>>> get_fibonacci(35)
9227465
>>> get_fibonacci2(35)
9227465
"""




def is_square_help(i, n):
    """Pomocná funkce."""

# Rozhodne, zda existuje číslo
# větší nebo rovno než i,
# jehož druhá mocnina je n.

"""
>>> is_square_help(0, 4)
True
>>> is_square_help(0, 5)
False
>>> is_square_help(0, 16)
True
"""


def is_square(n):
    """Rozhodne, zda je číslo čtvercové."""

"""
>>> is_square(9)
True
>>> is_square(10)
False
"""

