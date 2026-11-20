# Zadanie 28: wyświetlanie dwuwymiarowej listy o dwóch wierszach i czterech kolumnach.
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

for row in matrix:
    # *row przekazuje elementy wiersza jako osobne argumenty print().
    print(*row)
