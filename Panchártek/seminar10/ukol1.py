import matice_txt_IO

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matice_txt_IO.uloz_matici("matice.txt", M)
nactena_matice = matice_txt_IO.nacti_matici("matice.txt")
print(nactena_matice)