# Zadanie 1: tworzenie list przy użyciu różnych sposobów.
import random  # Moduł random umożliwia losowanie liczb.

arr1 = [3, 7, 1, 0, 4]
arr2 = [[2, 3], [7, 1], [0, 4]]
arr3 = [7 for i in range(5)]                    # Pięć razy wartość 7.
arr4 = [i for i in range(1, 10)]               # Liczby od 1 do 9.
arr5 = [i * 2 for i in range(1, 10)]           # Wielokrotności 2 od 2 do 18.
arr6 = [random.randint(1, 20) for i in range(10)]  # Dziesięć liczb losowych.
arr7 = [[] for i in range(5)]                  # Pięć niezależnych pustych list.
arr8 = [[1 for i in range(2)] for j in range(4)]  # Macierz 4x2 wypełniona jedynkami.
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]

# Dodatkowe listy wymagane w poleceniu.
arr10 = [4, 0, 3]
arr11 = [0 for i in range(15)]
arr12 = [random.randint(1, 30) for i in range(10)]
arr13 = [random.randint(0, 1) for i in range(20)]
arr14 = [[False for i in range(2)] for j in range(5)]

# Słownik ułatwia wyświetlenie nazwy i zawartości każdej listy.
arrays = {
    "arr1": arr1, "arr2": arr2, "arr3": arr3, "arr4": arr4,
    "arr5": arr5, "arr6": arr6, "arr7": arr7, "arr8": arr8,
    "arr9": arr9, "arr10": arr10, "arr11": arr11,
    "arr12": arr12, "arr13": arr13, "arr14": arr14
}
for name, values in arrays.items():
    print(f"{name} = {values}")
