def load_matrix(file):
    f = open(file, "r")
    matrix = []
    for line in f:
        submatrix = []
        for i in line.split(","):
            try:
                submatrix.append(int(i))
            except ValueError:
                pass
            except Exception as e:
                print(e.__class__ + ": ", + e)
        matrix.append(submatrix)
    print(matrix)
    print(matrix[0][0])


load_matrix("file.txt")