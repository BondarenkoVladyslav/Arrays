# Zadanie 21: przenoszenie liczb parzystych przed nieparzyste.
arr = [7, 9, 2, 4, 5, 6]
even_numbers = []
odd_numbers = []

for number in arr:
    # Liczba parzysta daje resztę 0 przy dzieleniu przez 2.
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Łączymy listy: najpierw parzyste, później nieparzyste.
arr = even_numbers + odd_numbers
print("arr =", arr)
