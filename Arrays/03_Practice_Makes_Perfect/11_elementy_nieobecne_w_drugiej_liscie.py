# Zadanie 11: wypisywanie liczb z pierwszej listy, których nie ma w drugiej.
first = [4, 36, 12, 28, 9, 44, 5]
second = [5, 1, 36]

# Sprawdzamy każdy element pierwszej listy operatorem not in.
not_in_second = []
for number in first:
    if number not in second:
        not_in_second.append(number)

print("Numbers only in the first array:", *not_in_second)
