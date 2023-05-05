# Binární strom (nazýváme pouze strom)
#
# Strom je buď prázdný, nebo neprázdný.
#
# Prázdný strom je pouze hodnota EMPTY.
EMPTY = []

# Neprázdný strom určuje hodnotu v kořeni, levý a pravý podstrom.

def make_tree(value, left, right):
    """Vytvoří neprázdný strom."""
    return [value, left, right]

# První testovací strom:
t1 = make_tree(1, EMPTY, EMPTY)

"""
>>> t1
[1, [], []]
"""

# Druhý testovací strom:
t2 = make_tree(2, t1, make_tree(3, EMPTY, EMPTY))

"""
>>> t2
[2, [1, [], []], [3, [], []]]
"""

def get_value(tree):
    """Vrátí hodnotu v kořeni neprázdného stromu."""
    return tree[0]

"""
>>> get_value(t2)
2
"""

def get_left(tree):
    """Vrátí levý podstrom neprázdného stromu."""
    return tree[1]

"""
>>> get_left(t2)
[1, [], []]
"""

def get_right(tree):
    """Vrátí pravý podstrom neprázdného stromu."""
    return tree[2]

"""
>>> get_right(t2)
[3, [], []]
"""


def is_empty(tree):
    """Rozhodne, zda je strom prázdný."""
    return tree == EMPTY

"""
>>> is_empty(get_left(t1))
True
>>> is_empty(t1)
False
"""

# List je neprázdný strom, který má prázdný levý i pravý podstrom.

def is_leaf(tree):
    """Rozhodne, zda je strom list."""
    return (not is_empty(tree)
            and is_empty(get_left(tree))
            and is_empty(get_right(tree)))

"""
>>> is_leaf(t1)
True
>>> is_leaf(EMPTY)
False
>>> is_leaf(t2)
False
"""


def make_leaf(value):
    """Vytvoří list."""
    return make_tree(value, EMPTY, EMPTY)

"""
>>> make_leaf(1)
[1, [], []]
"""

# Třetí testovací strom:
t3 = make_tree(
    1,
    make_tree(
        2,
        make_leaf(3),
        make_leaf(4)),
    make_tree(
        5,
        make_leaf(6),
        make_leaf(7)))

"""
>>> t3
[1, [2, [3, [], []], [4, [], []]], [5, [6, [], []], [7, [], []]]]
"""


def is_member(value, tree):
    """Rozhodne, zda se hodnota nalézá ve stromu."""
    return (not is_empty(tree)
            and (get_value(tree) == value
                 or is_member(value, get_left(tree))
                 or is_member(value, get_right(tree))))

"""
>>> is_member(5, t3)
True
>>> is_member(10, t3)
False
"""


def get_value_count(tree):
    """Vrátí počet hodnot ve stromu."""

"""
>>> get_value_count(t3)
7
"""

def remove_leaf(value, tree):
    """Odstraní všechny listy s hodnotou ze stromu."""
    if is_empty(tree):
        return EMPTY
    elif is_leaf(tree) and get_value(tree) == value:
        return EMPTY
    else:
        return make_tree(get_value(tree),
                         remove_leaf(value, get_left(tree)),
                         remove_leaf(value, get_right(tree)))

"""
>>> remove_leaf(7, t3)
[1, [2, [3, [], []], [4, [], []]], [5, [6, [], []], []]]
>>> remove_leaf(6, t3)
[1, [2, [3, [], []], [4, [], []]], [5, [], [7, [], []]]]
>>> remove_leaf(1, t2)
[2, [], [3, [], []]]
"""
def remove_root(tree):
    """Odstraní kořen ze stromu."""
    if is_empty(get_left(tree)):
        return get_right(tree)
    else:
        return make_tree(get_value(get_left(tree)),
                         remove_root(get_left(tree)),
                         get_right(tree))
                         

"""
>>> remove_root(t3)
[2, [3, [], [4, [], []]], [5, [6, [], []], [7, [], []]]]
"""

def remove(value, tree):
    """Odstraní hodnotu ze stromu."""

"""
>>> remove(2, t3)
[1, [3, [], [4, [], []]], [5, [6, [], []], [7, [], []]]]
"""
   
# Fibonacciho strom.
#
# Fibonacciho strom pro nulu je list s nulou.
#
# Fibonacciho strom pro číslo jedna je list s číslem jedna.
#
# Fibonacciho strom pro jiné číslo n je strom, kde
#  1. levý podstrom je Fibonacciho strom pro n - 1,
#  2. pravý podstrom je Fibonacciho strom pro n - 2,
#  3. hodnota v kořeni je součet hodnot v kořenech obou podstromů.


def make_fibonacci_tree(n):
    """Vytvoří Fibonacciho strom pro zadané číslo."""

"""
>>> make_fibonacci_tree(3)
[2, [1, [1, [], []], [0, [], []]], [1, [], []]]
"""

# Výška stromu.
#
# Výška prázdného stromu je nula.
#
# Výška neprázdného stromu je jedna plus maximum z výšek obou podstromů.

"""
>>> max(2, 5)
5
"""

def get_height(tree):
    """Vrátí výšku stromu."""

"""
>>> get_height(t1)
1
>>> get_height(EMPTY)
0
>>> get_height(t3)
3
"""

def get_values_dfs(tree):
    """Vrátí pole hodnot ve stromu. Prohledává do hloubky. (depth-first search)"""
    if is_empty(tree):
        return []
    else:
        return ([get_value(tree)]
                + get_values_dfs(get_left(tree))
                + get_values_dfs(get_right(tree)))

"""
>>> get_values_dfs(t3)
[1, 2, 3, 4, 5, 6, 7]
"""

# Les je pole stromů.

# Následující dvě funkce nejsou rekurzivní.
def get_forest_root_values(forest):
    """Vrátí hodnoty v kořenech neprázdných stromů."""
    values = []
    for tree in forest:
        if not is_empty(tree):
            values += [get_value(tree)]
    return values

"""
>>> get_forest_root_values([t1, t2, EMPTY, t3])                 
[1, 2, 1]
"""


def get_forest_subtrees(forest):
    """Vrátí podstromy neprázdných stromů."""

"""
>>> get_forest_subtrees([t1, t2, EMPTY, t3])                     
[[], [], [1, [], []], [3, [], []], [2, [3, [], []], [4, [], []]], [5, [6, [], []], [7, [], []]]]
"""

def get_forest_values_bfs(forest):
    """Vrátí hodnoty v lese. Prohledáváme do šířky. (breadth-first search)"""


"""
>>> get_forest_values_bfs([t3])                 
[1, 2, 5, 3, 4, 6, 7]
"""


def get_values_bfs(tree):
    """Vrátí hodnoty ve stromě. Prohledáváme do šířky. (breadth-first search)"""

"""
>>> get_values_bfs(t3)
[1, 2, 5, 3, 4, 6, 7]
"""

# Další je jen pro zájemce.


# (Binární) vyhledávací strom.

#
# Prázdný strom je vyhledávací strom.
#
# Neprázdný strom je vyhledávací strom pokud:

#  1. levý i pravý podstrom je binární vyhledávací strom,
#  2. hodnoty v levém podstromu jsou menší než hodnota v kořeni a
#     hodnoty v pravém podstromu jsou větší.

# Testovací vyhledávací strom:
t4 = make_tree(
    6,
    make_tree(
        2,
        make_leaf(1),
        make_leaf(4)),
    make_tree(
        10,
        make_leaf(8),
        make_leaf(12)))



def search(value, tree):
    """Rozhodne, zda se hodnota nelézá ve vyhledávacím stromě."""

"""
>>> search(4, t4)
True
>>> search(11, t4)
False
"""


def insert(value, tree):
    """Vloží hodnotu do vyhledávacího stromu."""

"""
>>> insert(11, t4)
[6, [2, [1, [], []], [4, [], []]], [10, [8, [], []], [12, [11, [], []], []]]]
"""


def get_tree_min(tree):
    """Vrátí nejmenší hodnotu v neprázdném vyhledávacím stromu."""

"""
>>> get_tree_min(t4)
1
"""


def get_tree_max(tree):
    """Vrátí největší hodnotu v neprázdném vyhledávacím stromu."""

"""
>>> get_tree_max(t4)
12
"""


def are_all_lesser(tree, num):
    """Rozhodne, zda jsou všechny hodnoty stromu menší než zadané číslo."""

"""
>>> are_all_lesser(make_tree(2, make_leaf(5), EMPTY), 7)
True
>>> are_all_lesser(make_tree(2, make_leaf(5), EMPTY), 4)
False
"""


def are_all_greater(tree, num):
    """Rozhodne, zda jsou všechny prvky stromu větší než zadané číslo."""

"""
>>> are_all_greater(make_tree(2, make_leaf(5), EMPTY), 1)
True
>>> are_all_greater(make_tree(2, make_leaf(5), EMPTY), 3)
False
"""


def is_search_tree(tree):
    """Rozhodne, zda je strom vyhledávací."""

"""
>>> is_search_tree(t4)
True
>>> is_search_tree(t3)
False
"""

# Balancovaný (binární) strom.
#
# Prázdný strom je balancovaný.
#
# Neprázdný strom je balancovaný pokud
# 1. levý i pravý podstrom je balancovaný,
# 2. vzdálenost výšky levého a pravého podstromu je nejvýše jedna.

def distance(num1, num2):
    """Vrátí vzdálenost dvou čísel."""
    return abs(num1 - num2)

"""
>>> distance(3, 5)
2
"""


def is_balanced(tree):
    """Rozhodne, zda je strom balancovaný."""

"""
>>> is_balanced(make_tree(1, make_tree(2, EMPTY, EMPTY), EMPTY))
True
>>> is_balanced(make_tree(1, make_tree(2, make_tree(3, EMPTY, EMPTY), EMPTY), EMPTY))
False
"""


def rotate_left(tree):
    """Učiní kořenem kořen pravého podstromu."""

"""
>>> rotate_left(t4)
[10, [6, [2, [1, [], []], [4, [], []]], [8, [], []]], [12, [], []]]
"""


def rotate_right(tree):
    """Učiní kořenem kořen levého podstromu."""

"""
>>> rotate_right(t4)
[2, [1, [], []], [6, [4, [], []], [10, [8, [], []], [12, [], []]]]]
"""


def move_to_root(tree, value):
    """Přesune hodnotu do kořene."""

"""
>>> move_to_root(t4, 1)
[1, [], [6, [2, [], [4, [], []]], [10, [8, [], []], [12, [], []]]]]
>>> move_to_root(t4, 10)
[10, [6, [2, [1, [], []], [4, [], []]], [8, [], []]], [12, [], []]]
"""
