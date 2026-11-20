# Zadanie 9: znalezienie kategorii z największymi wydatkami.
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# max() znajduje największy wydatek.
highest_expense = max(expenses)

# index() zwraca pozycję największej wartości na liście.
highest_index = expenses.index(highest_expense)

# Ten sam indeks wskazuje nazwę kategorii i jej koszt.
print("The most expensive category:", categories[highest_index])
print("Expense:", highest_expense)
