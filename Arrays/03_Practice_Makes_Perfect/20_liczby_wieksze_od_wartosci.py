# Zadanie 20: zliczanie wartości większych od liczby wpisanej przez użytkownika.
values = [2.5, 7.1, 4.8, 9.3, 1.2, 8.0, 6.4]
limit = float(input("Enter comparison value: "))

count = 0
for value in values:
    if value > limit:
        count += 1

print("Array:", values)
print("Limit:", limit)
print("Number of elements greater than the limit:", count)
