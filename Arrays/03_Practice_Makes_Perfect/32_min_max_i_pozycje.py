# Zadanie 32 znalezienie minimum i maksimum oraz ich pozycji w macierzy.
matrix = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

# Punkt odniesienia z pierwszego elementu (warto ustawić (1, 1), gdy [0][0] jest ekstremum)
minimum = matrix[0][0]
maximum = matrix[0][0]
min_position = (0, 0)
max_position = (0, 0)

# Iterujemy po indeksach zamiast bezpośrednio po wartościach, aby zapisać pozycję
for row_index in range(len(matrix)):
    for column_index in range(len(matrix[row_index])):
        value = matrix[row_index][column_index]

        if value < minimum:
            minimum = value
            # Dodajemy 1, aby przeliczyć indeksy (od 0) na numer wiersza i kolumny (od 1)
            min_position = (row_index + 1, column_index + 1)
        if value > maximum:
            maximum = value
            max_position = (row_index + 1, column_index + 1)

print("Minimum:", minimum, "row:", min_position[0], "column:", min_position[1])
print("Maximum:", maximum, "row:", max_position[0], "column:", max_position[1])