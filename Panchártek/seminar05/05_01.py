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
                
def tree_find(node, x):
    if node[VALUE] == x:
        return True
    elif x < node[VALUE]:
        if not node[LEFT_CHILD]:
            return False
        return tree_find(node[LEFT_CHILD], x)
    else:
        if not node[RIGHT_CHILD]:
            return False
        return tree_find(node[RIGHT_CHILD], x)

root = []

tree_add(root, 8)
tree_add(root, 4)
tree_add(root, 16)
tree_add(root, 15)
tree_add(root, 42)
tree_add(root, 23)

print(root)  

print(tree_find(root, 10))
print(tree_find(root, 8))
print(tree_find(root, 4))
print(tree_find(root, 16))
print(tree_find(root, 1))
print(tree_find([], 2))