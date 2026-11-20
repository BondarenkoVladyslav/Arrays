# Zadanie 5: wpisywanie jedynek na głównej przekątnej macierzy 3x3.
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Elementy głównej przekątnej mają ten sam indeks wiersza i kolumny.
for i in range(len(matrix)):
    matrix[i][i] = 1

# Wyświetlamy macierz wiersz po wierszu.
for row in matrix:
    print(*row)  #* rozbija liste na pojedyncze elementy oddzielone spacjami
