# Zadanie 35: tworzenie i wyświetlanie macierzy jednostkowych.
def identity_matrix(n):
    # Macierz n x n początkowo zawiera same zera.
    matrix = [[0 for column in range(n)] for row in range(n)]

    # Na głównej przekątnej ustawiamy jedynki.
    for i in range(n):
        matrix[i][i] = 1
    return matrix

def print_matrix(matrix):
    # Wyświetlamy każdy wiersz macierzy.
    for row in matrix:
        print(*row)

for size in [3, 5, 8]:
    print(f"Identity matrix {size}x{size}:")
    print_matrix(identity_matrix(size))
    print()
