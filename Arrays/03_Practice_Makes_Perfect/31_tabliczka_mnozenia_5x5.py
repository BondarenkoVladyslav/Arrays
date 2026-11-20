# Zadanie 31: wypełnianie macierzy 5x5 tabliczką mnożenia.
size = 5
matrix = [[0 for column in range(size)] for row in range(size)]

for row in range(size):
    for column in range(size):
        # Numery wierszy i kolumn zaczynają się od 1 w tabliczce.
        matrix[row][column] = (row + 1) * (column + 1)

for row in matrix:
    # :2d ustawia stałą szerokość dwóch znaków dla równego układu.
    print(" ".join(f"{value:2d}" for value in row))
