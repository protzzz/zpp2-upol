"""
Bonus:
>>> get_distance(cons(1, cons(2, cons(3, EMPTY))),
                 cons(1, cons(3, EMPTY)))
1
>>> get_distance(cons(1, cons(2, cons(3, EMPTY))),
                 cons(1, cons(4, cons(3, EMPTY))))
1
>>> get_distance(cons(1, cons(2, cons(3, EMPTY))),
                 cons(1, cons(4, EMPTY)))
2
"""
# (Spojové) seznamy - pokračování

# Prázdný seznam:
EMPTY = []

# Neprázdný seznam určuje první prvek a zbytek. Zbytek je opět seznam.
def cons(val, lst):
    """Vrátí seznam, kde první prvek bude val a zbytek lst."""
    return [val, lst]

"""
>>> cons(1, EMPTY)
[1, []]
>>> cons(1, cons(2, EMPTY))
[1, [2, []]]
"""

def get_first(lst):
    """Vrátí první prvek neprázdného seznamu."""
    return lst[0]

"""
>>> l = cons(1, cons(2, EMPTY))
>>> get_first(l)
1
"""

def get_rest(lst):
    """Vrátí zbytek neprázdného seznamu."""
    return lst[1]

"""
>>> l = cons(1, cons(2, EMPTY))
>>> get_rest(l)
[2, []]
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

def remove(val, lst):
    """Odebere ze seznamu všechny výskyty hodnoty."""
    if is_empty(lst):
        return EMPTY
    elif val == get_first(lst):
        return remove(val, get_rest(lst))
    else:
        return cons(get_first(lst), remove(val, get_rest(lst)))
    

"""
>>> remove(2, cons(2, cons(1, cons(2, cons(3, EMPTY)))))
[1, [3, []]]
"""

def remove_first(val, lst):
    """Odebere ze seznamu první výskyt hodnoty."""

"""
>>> remove_first(2, cons(2, cons(1, cons(2, cons(3, EMPTY)))))
[1, [2, [3, []]]]
"""


def square(num):
    """Vrátí druhou mocninu čísla."""
    return num **2

"""
>>> square(3)
9
"""

def square_map(lst):
    """Vrátí seznam druhých mocnin čísel."""
    if is_empty(lst):
        return EMPTY
    else:
        return cons(square(get_first(lst)),
                    square_map(get_rest(lst)))
        

"""
>>> square_map(cons(1, cons(2, cons(3, EMPTY))))
[1, [4, [9, []]]]
"""

def is_even(num):
    """Rozhodne, zda je číslo sudé."""
    return num % 2 == 0

"""
>>> is_even(2)
True
>>> is_even(3)
False
"""

def even_filter(lst):
    """Nechá v seznamu pouze sudá čísla."""

"""
>>> even_filter(cons(1, cons(2, cons(3, cons(4, EMPTY)))))
[2, [4, []]]
"""


def append(lst1, lst2):
    """Spojí seznamy."""
    if is_empty(lst1):
        return lst2
    else:
        return cons(get_first(lst1), append(get_rest(lst1), lst2))

"""
>>> append(cons(1, cons(2, EMPTY)), cons(3, cons(4, EMPTY)))
[1, [2, [3, [4, []]]]]
"""

def reverse_append(lst1, lst2):
    """Spojí seznamy tak, že otočí pořadí prvků v prvním seznamu."""
    if is_empty(lst1):
        return lst2
    else:
        return reverse_append(get_rest(lst1), cons(get_first(lst1), lst2))

"""
>>> reverse_append(cons(1, cons(2, EMPTY)), cons(3, cons(4, EMPTY)))
[2, [1, [3, [4, []]]]]
"""

def reverse(lst):
    """Otočí pořadí prvků v seznamu."""

"""
>>> reverse(cons(1, cons(2, cons(3, EMPTY))))
[3, [2, [1, []]]]
"""

def insert(val, lst):
    """Vloží hodnotu do setřízeného seznamu."""
    if is_empty(lst):
        return cons(val, EMPTY)
    elif val < get_first(lst):
        return cons(val, lst)
    else:
        return cons(get_first(lst), insert(val, get_rest(lst)))

"""
>>> insert(2, cons(1, cons(3, EMPTY)))
[1, [2, [3, []]]]
>>> insert(0, cons(1, cons(3, EMPTY)))
[0, [1, [3, []]]]
>>> insert(4, cons(1, cons(3, EMPTY)))
[1, [3, [4, []]]]
"""

def insertion_sort(lst):
    """Setřídí seznam vkládáním."""

"""
>>> insertion_sort(cons(3, cons(2, cons(1, cons(5, cons(4, EMPTY))))))
[1, [2, [3, [4, [5, []]]]]]
"""

def get_min(a, b):
    """Minimum dvou čísel."""
    if a <= b:
        return a
    else:
        return b
    
"""
>>> get_min(2, 5)
2
>>> get_min(5, 2)
2
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


def get_min_list(lst):
    """Vrátí minimum neprázdného seznamu."""

"""
>>> min_list(cons(5, cons(2, cons(7, EMPTY))))
2
"""


def selection_sort(lst):
    """Setřídí seznam výběrem."""

"""
>>> selection_sort(cons(3, cons(2, cons(1, cons(1, EMPTY)))))               
[1, [1, [2, [3, []]]]]
"""

def is_small(lst):
    """Rozhodne, zda je seznam nejvýše jednoprvkový."""
    return is_empty(lst) or is_empty(get_rest(lst))

"""
>>> is_small(EMPTY)
True
>>> is_small(cons(1, EMPTY))
True
>>> is_small(cons(1, cons(2, EMPTY)))
False
"""

def get_second(lst):
    """Vrátí druhý prvek seznamu."""
    return get_first(get_rest(lst))

"""
>>> get_second(cons(1, cons(2, cons(3, EMPTY))))
2
"""


def bubble_sort_step(lst):
    """Provede jeden průchod bublinkového třízení."""

"""
bubble_sort_step(cons(3, cons(2, cons(1, EMPTY))))
[2, [1, [3, []]]]
"""


def bubble_sort_help(lst, i):
    """Provede i průchodů bublikového třízení."""

"""
>>> bubble_sort_help(cons(3, cons(2, cons(1, EMPTY))), 2)
[1, [2, [3, []]]]
"""

def get_length(lst):
    """Vrátí délku seznamu."""
    if is_empty(lst):
        return 0
    else:
        return 1 + get_length(get_rest(lst))
    
"""
>>> l = cons(1, cons(2, cons(3, EMPTY)))
>>> get_length(l)
3
>>> get_length(EMPTY)
0
"""


def bubble_sort(lst):
    """Setřídí seznam bublikovým třízením."""

"""
>>> bubble_sort(cons(3, cons(2, cons(1, EMPTY))))
[1, [2, [3, []]]]
"""


def filter_less(lst, value):
    """Seznam čísel menších než zadané číslo."""

"""
>>> filter_less(cons(2, cons(1, cons(3, EMPTY))), 2)
[1, []]
"""


def filter_great(lst, value):
    """Seznam čísel větších než zadané číslo."""

"""
>>> filter_great(cons(2, cons(1, cons(3, EMPTY))), 2)
[3, []]
"""


def quicksort(lst):
    """Setřídí seznam rychlým tříděním."""
"""
>>> quicksort(cons(2, cons(1, cons(4, cons(3, cons(5, EMPTY))))))
[1, [2, [3, [4, [5, []]]]]]
"""


def merge(lst1, lst2):
    """Sleje dva uspořádané seznamy."""

"""
>>> merge(cons(1, cons(3, EMPTY)), cons(2, cons(4, cons(5, EMPTY))))
[1, [2, [3, [4, [5, []]]]]]
"""


def get_head(lst, n):
    """Vrátí prvních n prvků seznamu."""

"""
>>> get_head(cons(1, cons(2, cons(3, EMPTY))), 2)
[1, [2, []]]
"""


def get_tail(lst, n):
    """Vrátí seznam bez prvních n prvků."""

"""
>>> get_tail(cons(1, cons(2, cons(3, EMPTY))), 2)
[3, []]
"""


def merge_sort(lst):
    """Setřídí seznam slučováním."""

"""
>>> merge_sort(cons(2, cons(1, cons(4, cons(3, cons(5, EMPTY))))))
[1, [2, [3, [4, [5, []]]]]]
"""
