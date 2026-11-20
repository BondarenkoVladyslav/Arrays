# Zadanie 10: sprawdzanie, czy dwie listy są identyczne.
def compare(array1, array2):
    # Listy są takie same, jeśli mają tę samą długość i te same wartości
    # na odpowiadających sobie pozycjach.
    if len(array1) != len(array2):
        return False

    for index in range(len(array1)):
        if array1[index] != array2[index]:
            return False

    return True

test_pairs = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

for array1, array2 in test_pairs:
    same = compare(array1, array2)
    print("Array1:", *array1)
    print("Array2:", *array2)
    print("Comparison:", "arrays are the same" if same else "arrays are different")
    print()
