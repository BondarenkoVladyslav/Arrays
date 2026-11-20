# Zadanie 7: obliczanie średniej arytmetycznej przy użyciu pętli while.
numbers = [15, 8, 31, 47, 2, 19]
total = 0
index = 0

while index < len(numbers):
    total += numbers[index]
    index += 1

average = total / len(numbers)
print("Array:", *numbers)  #* rozbija liste na pojedyncze elementy oddzielone spacjami
print(f"Arithmetic mean: {average:.2f}")
