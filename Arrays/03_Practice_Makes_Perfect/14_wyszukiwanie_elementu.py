# Zadanie 14: funkcja sprawdza, czy liczba występuje na liście.
def occurs(number, array):
    # Operator 'in' bezpośrednio zwraca wartość logiczną True False
    return number in array

numbers = [15, 38, 7, 23, 14]
number = int(input("Number: "))

# Operator * rozpakowuje listę, wypisując same elementy oddzielone spacją
print("Array:", *numbers)
if occurs(number, numbers):
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")