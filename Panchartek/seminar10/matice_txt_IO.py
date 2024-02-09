def uloz_matici(file, matrix):
    f = open(file, "w")
    for i in matrix:
        for j in range(len(i)):
            f.write(str(i[j]))
            if j < len(i) - 1:
                f.write(",")
        f.write("\n")
    f.close

def nacti_matici(file):
    f = open(file, "r")
    matrix = []
    for line in f:
        submatrix = []
        for i in line.strip().split(","):
            try:
                submatrix.append(int(i))
            except ValueError:
                pass
            except Exception as e:
                print(e.__class__ + ": ", + e)
        matrix.append(submatrix)
    f.close
    return matrix