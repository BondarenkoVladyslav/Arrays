
# Lista przechowuje pięć liczb w ustalonej kolejności.
arr = [2, 3, 7, 5, 4]

# Wyświetlamy całą listę oraz liczbę jej elementów.
print("Array:", arr)
print("Number of elements:", len(arr))

# Indeksy listy zaczynają się od zera: pierwszy element ma indeks 0.
print("First value:", arr[0])
print("Second value:", arr[1])

# Ostatni element pobieramy przez indeks len(arr) - 1.
# Przedostatni ma indeks len(arr) - 2; nie używamy indeksów ujemnych.
print("Last value:", arr[len(arr) - 1])
print("Last but one value:", arr[len(arr) - 2])

# Dodajemy pierwszy i ostatni element.
print("Sum of first and last value:", arr[0] + arr[len(arr) - 1])

# Dla listy o nieparzystej długości środkowy element ma indeks len(arr) // 2.
print("Middle value:", arr[len(arr) // 2])

# Pętla for przechodzi kolejno przez wszystkie wartości.
print("Values separated by a space:", end=" ")
for value in arr:
    print(value, end=" ")
print()
