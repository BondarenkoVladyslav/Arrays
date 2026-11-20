# Zadanie 7: obliczanie statystyk wyników testu.
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

question_number = len(test_results)  # Liczba wszystkich pytań.
correct_answers = 0
for answer in test_results:
    if answer is True:
        correct_answers += 1  # Dodajemy jeden za każdą poprawną odpowiedź.

incorrect_answers = question_number - correct_answers
correct_percentage = correct_answers / question_number * 100

print("TEST STATISTICS")
print("Number of questions:", question_number)
print("Number of correct answers:", correct_answers)
print("Number of incorrect answers:", incorrect_answers)
print(f"Percentage of correct answers: {correct_percentage:.2f}%")
