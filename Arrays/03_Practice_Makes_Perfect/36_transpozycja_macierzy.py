# Zadanie 36 transponowanie macierzy zamiana wierszy na kolumny.
def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    transposed = []
    # Odwrócona kolejność pętli, iterujemy najpierw po kolumnach, aby budować z nich nowe wiersze
    for column in range(columns):
        new_row = []
        for row in range(rows):
            # Pobieramy elementy z tej samej kolumny w kolejnych wierszach
            new_row.append(matrix[row][column])
        transposed.append(new_row)
    return transposed

matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
    [[5, 6, 7, 8]]
]

for matrix in matrices:
    print("Original:")
    for row in matrix:
        print(*row)
    print("Transposed:")
    for row in transpose_matrix(matrix):
        print(*row)
    print()