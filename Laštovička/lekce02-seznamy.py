# Seznamy v Pythonu nazýváme pole.
#
# Seznam v Pythonu opravdu polem je.
# Platí například, že přístup k prvku na indexu je v konstantním čase.

# Zavedeme si (spojové) seznamy.

# Prázdný seznam:
EMPTY = []

# Neprázdný seznam určuje první prvek a zbytek. Zbytek je opět seznam.
def cons(val, lst):
    """Vrátí seznam, kde první prvek bude val a zbytek lst."""
    return [val, lst]

"""
>>> cons(1, EMPTY)
[1, []]
>>> cons(2, cons(1, EMPTY))
[2, [1, []]]
"""

def get_first(lst):
    """Vrátí první prvek neprázdného seznamu."""
    return lst[0]

"""
>>> l = cons(2, cons(1, EMPTY))
>>> get_first(l)
2
"""

def get_rest(lst):
    """Vrátí zbytek neprázdného seznamu."""
    return lst[1]

"""
>>> l = cons(2, cons(1, EMPTY))
>>> get_rest(l)
[1, []]
"""


def is_empty(lst):
    """Rozhodne, zda je seznam prázdný."""
    return lst == EMPTY 

"""
>>> l = cons(1, EMPTY)
>>> is_empty(l)
False
>>> is_empty(get_rest(l))
True
"""


def get_second(lst):
    """Vrátí druhý prvek seznamu."""
    return get_first(get_rest(lst))

"""
>>> l = cons(1, cons(2, cons(3, EMPTY)))
>>> get_second(l)
2
"""


def get_third(lst):
    """Vrátí třetí prvek seznamu."""

"""
>>> l = cons(1, cons(2, cons(3, EMPTY)))
>>> get_third(l)
3
"""


def get_nth(lst, n):
    """Vrátí prvek na indexu."""
    if n == 0:
        return get_first(lst)
    else:
        return get_nth(get_rest(lst), n - 1)
    
"""
>>> l = cons(1, cons(2, cons(3, EMPTY)))
>>> get_nth(l, 0)
1
>>> get_nth(l, 2)
3
"""

def is_singleton(lst):
    """Rozhodne, zda má seznam jediný prvek."""
    return not is_empty(lst) and is_empty(get_rest(lst))

"""
>>> is_singleton(EMPTY)
False
>>> is_singleton(cons(1, EMPTY))
True
>>> is_singleton(cons(1, cons(2, EMPTY)))
False
"""

def get_last(lst):
    """Vrátí poslední prvek neprázdného seznamu."""
    
"""
get_last(cons(1, cons(2, cons(3, EMPTY))))
3
"""


def get_length(lst):
    """Vrátí délku seznamu."""
    if is_empty(lst):
        return 0
    else:
        return get_length(get_rest(lst)) + 1
"""
>>> l = cons(1, cons(2, cons(3, EMPTY)))
>>> get_length(l)
3
>>> get_length(EMPTY)
0
"""

def list_sum(lst):
    """Vrátí součet prvků seznamu."""
"""
>>> l = cons(1, cons(2, cons(3, EMPTY)))
>>> list_sum(l)
6
"""

def list_product(lst):
    """Vrátí součin prvků seznamu."""
"""
>>> l = cons(2, cons(3, EMPTY))
>>> list_product(l)
6
"""

def is_member(value, lst):
    """Rozhodne, zda je hodnota prvkem seznamu."""
    return not is_empty(lst) and (get_first(lst) == value or is_member(value, get_rest(lst)))

"""
>>> l = cons(1, cons(2, cons(3, EMPTY)))
>>> is_member(2, l)
True
>>> is_member(4, l)
False
"""


def is_subset(lst1, lst2):
    """Rozhodne, zda seznam `lst2` obsahuje každý prvek seznamu `lst1`."""

"""
>>> l1 = cons(1, cons(3, EMPTY))
>>> l2 = cons(3, cons(2, cons(1, EMPTY)))
>>> is_subset(l1, l2)
True
>>> is_subset(l2, l1)
False
"""


def are_sets_equal(lst1, lst2):
    """"Rozhodne, zda seznamy obsahují stejné prvky."""

"""
>>> l1 = cons(1, cons(3, cons(2, EMPTY)))
>>> l2 = cons(3, cons(2, cons(1, EMPTY)))
>>> are_sets_equal(l1, l2)
True
"""



def are_lists_equal(lst1, lst2):
    """Rozhodne, zda jsou seznamy stejné."""


def is_sublist(lst1, lst2):
    """Rozhodne, zda je seznam jedna podseznamem seznamu dva."""

"""
>>> is_sublist(cons(1, cons(3, EMPTY)), cons(1, cons(2, cons(3, EMPTY))))
True
"""
