# Zadanie 22: sprawdzanie, czy każdy element pierwszej listy jest w drugiej.
def is_subset(first, second):
    for element in first:
        # Wczesne wyjście, przerywamy i zwracamy False, gdy brakuje choć jednego elementu
        if element not in second:
            return False
    # Wykonuje się tylko wtedy, gdy pętla przeszła do końca
    return True

array1 = [2, 4]
array2 = [1, 2, 3, 4, 5]
print("Array 1:", array1)
print("Array 2:", array2)
print("First array is a subset of the second:", is_subset(array1, array2))