# Zadanie 12: sortowanie trzech list metodą Bubble Sort.
def bubblesort(array):
    # Kopia zabezpiecza oryginalną listę przed modyfikacją.
    result = array.copy()
    for i in range(len(result) - 1):
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

arrays = [
    [8, 3, 5, 1, 9],
    [12, -3, 7, 0, 4],
    [22, 11, 33, 2, 18, 5]
]

for array in arrays:
    print("Before:", array)
    print("After: ", bubblesort(array))
    print()
