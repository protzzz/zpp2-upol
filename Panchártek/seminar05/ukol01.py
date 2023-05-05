root = []

VALUE = 0
LEFT_CHILD = 1
RIGHT_CHILD = 2


def tree_add(node, x):
    if not node:
        node.extend([x, [], []])
        return

    while node[VALUE] != x:
        if x < node[VALUE]:
            if node[LEFT_CHILD]:
                node = node[LEFT_CHILD]
            else:
                node[LEFT_CHILD] = [x, [], []]
                return

        elif x > node[VALUE]:
            if node[RIGHT_CHILD]:
                node = node[RIGHT_CHILD]
            else:
                node[RIGHT_CHILD] = [x, [], []]
                return


tree_add(root, 8)
tree_add(root, 4)
tree_add(root, 23)
tree_add(root, 16)
tree_add(root, 15)
tree_add(root, 42)
print(root)

def tree_find(node, x):
    while node and x != node[VALUE]:
        if x < node[VALUE]:
            node = node[LEFT_CHILD]
        elif x > node[VALUE]:
            node = node[RIGHT_CHILD]
    if x in node:
        return True
    else:
        return False


print(tree_find(root, 11))
print(tree_find(root, 8))
print(tree_find(root, 4))