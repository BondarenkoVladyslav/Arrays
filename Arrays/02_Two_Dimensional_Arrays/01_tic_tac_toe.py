# Zadanie 1: wyświetlanie planszy do gry Tic-Tac-Toe.
tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

# Pętla zewnętrzna przechodzi po kolejnych wierszach planszy.
for row in tic_tac_toe_board:
    # Pętla wewnętrzna wyświetla komórki bieżącego wiersza.
    for cell in row:
        # end=" " pozostawia kursor w tym samym wierszu.
        print(cell, end=" ")
    # Po zakończeniu wiersza przechodzimy do nowej linii.
    print()
