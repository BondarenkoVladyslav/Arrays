# Zadanie 11: sortowanie listy algorytmem Bubble Sort.
def bubble_sort(arr):
    # Tworzymy kopię, aby nie zmieniać listy przekazanej do funkcji.
    result = arr.copy()
    n = len(result)

    # Po każdej rundzie największy z pozostałych elementów trafia na koniec.
    for i in range(n - 1):
        # Ostatnie i elementów są już na właściwych miejscach.
        for j in range(0, n - i - 1):
            # Jeśli sąsiednie liczby są w złej kolejności, zamieniamy je.
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

print("Fuel consumption before:", car_fuel_consumption)
print("Fuel consumption after: ", bubble_sort(car_fuel_consumption))
print("Transactions before:", bank_transactions)
print("Transactions after: ", bubble_sort(bank_transactions))
