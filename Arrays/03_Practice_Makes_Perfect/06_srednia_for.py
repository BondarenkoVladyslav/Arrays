# Zadanie 6: obliczanie średniej arytmetycznej przy użyciu pętli for.
numbers = [15, 8, 31, 47, 2, 19]
total = 0

for number in numbers:
    total += number

average = total / len(numbers)
print("Array:", *numbers)  #* rozbija liste na pojedyncze elementy oddzielone spacjami
print(f"Arithmetic mean: {average:.2f}")
