# Zadanie 37: zamiana macierzy 2D w jedną listę 1D.
def flatten_2d_array(matrix):
    flat = []
    # Pętla zewnętrzna przechodzi przez wiersze, a wewnętrzna przez komórki.
    for row in matrix:
        for value in row:
            flat.append(value)
    return flat

matrices = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5], [7, 4], [2, 6]]
]

for matrix in matrices:
    print("2D array:")
    for row in matrix:
        print(*row)
    print("1D array:", flatten_2d_array(matrix))
    print()
