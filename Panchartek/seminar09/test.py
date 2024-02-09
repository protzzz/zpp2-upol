
def load_matrix(file):
    f = open(file, "r")
    seznam = []
    radek = f.read()
    list = []
    for i in radek:
        if i == ",":
            continue
        elif i == '\n':
            continue
        list.append(int(i))
    seznam.append(list)
    f.close()
    return seznam

print(load_matrix("file.txt"))