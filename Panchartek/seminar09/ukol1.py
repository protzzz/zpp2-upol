def save_martix(file, matrix):
    f = open(file, "w")
    for i in matrix:
        for j in range(len(i)):
            f.write(str(i[j]))
            if j < len(i) - 1:
                f.write(",")
        f.write("\n")
    f.close

save_martix("file.txt", [[1,2,3,3],[4,5,5,6],[6,7,10]])

# def save_martix(file, matrix):
#     f = open(file, "w")
#     for i in matrix:
#         for j in range(len(i)):
#             f.write(str(i[j]))
#             if j < len(i) - 1:
#                 f.write(",")
#         f.write("\n")
#     f.close

# save_martix("file.csv", [[1,2,3],[4,5,6],[7,8,9]])