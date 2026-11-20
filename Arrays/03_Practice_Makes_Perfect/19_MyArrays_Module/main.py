# Zadanie 19: użycie własnego modułu MyArrays.
import MyArrays

numbers = [7, 3, 8, 5, 2]

print("Numbers:", ",".join(str(number) for number in numbers))
print("Second largest number:", MyArrays.second_largest(numbers))
print("Difference between largest and smallest:",
      MyArrays.difference_largest_smallest(numbers))
print("Median:", MyArrays.median(numbers))
print("Smallest and largest number:",
      ",".join(str(number) for number in MyArrays.smallest_and_largest(numbers)))
print("Numbers as a string:", MyArrays.numbers_as_string(numbers))
