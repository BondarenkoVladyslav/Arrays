# Zadanie 33: zamiana pierwszego i ostatniego wiersza macierzy 3x5.
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before:")
for row in matrix:
    print(*row)

# Zamieniamy całe listy reprezentujące wiersze.
matrix[0], matrix[-1] = matrix[-1], matrix[0]

print("After:")
for row in matrix:
    print(*row)
