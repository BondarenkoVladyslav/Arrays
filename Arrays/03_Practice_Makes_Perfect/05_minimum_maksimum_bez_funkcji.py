# Zadanie 5: znalezienie minimum i maksimum bez min() oraz max().
numbers = [-15, 8, -31, 47, -2, 19]

# Przyjmujemy, że pierwszy element jest początkowo min i max.
minimum = numbers[0]
maximum = numbers[0]

# Porównujemy każdy kolejny element z aktualnym minimum i maksimum.
for number in numbers[1:]:
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number

print("Array:", numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)
