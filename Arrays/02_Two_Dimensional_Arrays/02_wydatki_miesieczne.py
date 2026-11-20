# Zadanie 2: obliczanie wydatków według kategorii, tygodni i całego miesiąca.
# Każdy wiersz oznacza tydzień, a kolumny: Food, Transport, Utilities.
monthly_expenses = [
    [200, 50, 100],
    [180, 60, 110],
    [220, 55, 105],
    [210, 65, 95]
]

category_totals = [0, 0, 0]  # Suma dla trzech kategorii.
week_totals = []             # Suma dla każdego tygodnia.
month_total = 0

# Pętla przechodzi przez każdy tydzień.
for week in monthly_expenses:
    weekly_total = 0

    # Liczymy wydatki w każdej kategorii danego tygodnia.
    for category_index in range(len(week)):
        amount = week[category_index]
        category_totals[category_index] += amount
        weekly_total += amount

    week_totals.append(weekly_total) #append dodaje nowy element w koniec listy
    month_total += weekly_total

print("MONTHLY EXPENSES")
print("Food:", category_totals[0])
print("Transport:", category_totals[1])
print("Utilities:", category_totals[2])
for index, total in enumerate(week_totals, start=1):
    print(f"Week {index}:", total)
print("TOTAL:", month_total)
