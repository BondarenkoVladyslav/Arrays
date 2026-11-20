# Zadanie 34 zamiana pierwszej i ostatniej kolumny macierzy 3x5.
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before:")
for row in matrix:
    print(*row)

# Dla każdego wiersza zamieniamy element o indeksie 0 z elementem -1.
for row in matrix:
    row[0], row[-1] = row[-1], row[0]

print("After:")
for row in matrix:
    print(*row)
