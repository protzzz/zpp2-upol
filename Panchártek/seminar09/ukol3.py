def cteni_souboru(file):
    f = open(file, "r")
    while True:
        symbol = f.read(1)
        if symbol == '':
            break
        print(symbol, end='')
    f.close()

def pocet_souboru(file):
    f = open(file, "r")
    pocet = []
    for line in f:
        for i in line.strip().split(","):
            pocet.append(int(i))
    result = sum(pocet)
    f.close
    return result

cteni_souboru("file.txt")
print("Pocet cisel souboru:", pocet_souboru("file.txt"))