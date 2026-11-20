# Zadanie 2: modyfikowanie wskazanych elementów listy.
numbers = [1, 2, 3, 4, 5]
print("Array:", numbers)

# Zmniejszamy pierwszy element (indeks 0) o jeden.
numbers[0] -= 1
print("Array:", numbers)

# Zwiększamy ostatni element o cztery.
numbers[len(numbers) - 1] += 4
print("Array:", numbers)

# Mnożymy środkowy element przez dwa.
middle_index = len(numbers) // 2
numbers[middle_index] *= 2
print("Array:", numbers)
