# Zadanie 2: zliczanie parzystych liczb za pomocą pętli while.
numbers = [34, 7, 19, 4, 21, 8]
count_even = 0
index = 0

while index < len(numbers):
    # Reszta z dzielenia przez 2 równa 0 oznacza liczbę parzystą.
    if numbers[index] % 2 == 0:
        count_even += 1
    index += 1

print("Array:", numbers)
print("Number of even values:", count_even)
