def insert(root, data, parent=None):
    if root is None:
        root = {"data": data, "left": None, "right": None, "parent": parent}
    elif data < root["data"]:
        root["left"] = insert(root["left"], data, root)
    else:
        root["right"] = insert(root["right"], data, root)
    return root

def print_tree(root):
    if root is not None:
        print_tree(root["left"])
        print(str(root["data"]) + ' ', end='')
        if root["parent"] is not None:
            print(",kde Parent je: " + str(root["parent"]["data"]))
        else:
            print("(Root node)")
        print_tree(root["right"])

root = None

root = insert(root, 1)
root = insert(root, 2)
root = insert(root, 7)
root = insert(root, 8)
root = insert(root, 9)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 6)

print(root)
print_tree(root)