# Zadanie 29: sumowanie elementów ostatniej kolumny macierzy.
matrix = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

total = 0
for row in matrix:
    # Indeks -1 wskazuje ostatnią kolumnę w każdym wierszu.
    total += row[-1]

print("Sum of values in the last column:", total)
