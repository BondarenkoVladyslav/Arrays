# Zadanie 23: zwracanie losowego elementu listy.
import random

def rand_elem(array):
    # Sprawdzamy, czy lista zawiera elementy, zanim wylosujemy indeks.
    if not array:
        raise ValueError("Nie można losować z pustej listy.")
    # Losujemy indeks z zakresu od 0 do len(array)-1 (randrange wyklucza górną granicę)
    return array[random.randrange(len(array))]

values = ["apple", "banana", "orange", "pear", "plum"]
print("Array:", values)
print("Randomly selected elements:")
for i in range(5):
    print(rand_elem(values))
