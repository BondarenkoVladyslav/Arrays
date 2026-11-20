# Zadanie 3: funkcja zwraca nazwę dnia na podstawie numeru 1–7.
def weekday(day_number):
    # Lista przechowuje nazwy dni w kolejności od poniedziałku.
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]

    # Zamieniamy numer dnia (1–7) na indeks listy (0–6).
    if 1 <= day_number <= 7:
        return weekdays[day_number - 1]

    # Dla niepoprawnego numeru zwracamy czytelny komunikat.
    return "Incorrect day number"

# Testujemy wartości wymagane w zadaniu.
for number in [1, 4, 7]:
    print(f"Day {number}: {weekday(number)}")
