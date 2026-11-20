# Zadanie 9: rysowanie poziomych słupków z gwiazdek.
numbers = [2, 6, 4, 9, 7]

def star(n):
    # Operator * powtarza tekst "*" dokładnie n razy.
    return "*" * n

for number in numbers:
    print(f"{number}: {star(number)}")
