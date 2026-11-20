# Zadanie 13: wyświetlanie elementów, które występują dokładnie jeden raz.
numbers = [2, 3, 2, 5, 8, 1, 9, 8]
unique_elements = []

for number in numbers:
    # count() zwraca liczbę wystąpień danej wartości.
    if numbers.count(number) == 1:
        unique_elements.append(number)

print("Array:", *numbers)
print("Unique elements:", *unique_elements)
