# Zadanie 4: obliczanie drugiej potęgi każdego elementu listy.
numbers = [8, 2, 5, 1, 9]

# Wyrażenie list comprehension tworzy nową listę kwadratów.
squares = [number ** 2 for number in numbers]

print("Array:", *numbers)  #* rozbija liste na pojedyncze elementy oddzielone spacjami
print("2nd power:", *squares)
