# Zadanie 30: funkcja tworzy macierz o wymiarach x na y, wypełnioną zerami.
def create_2d_arr(x, y):
    # Każdy wiersz jest osobną listą, więc można zmieniać komórki niezależnie.
    return [[0 for column in range(y)] for row in range(x)]

matrix = create_2d_arr(3, 5)

for row in matrix:
    print(*row)
