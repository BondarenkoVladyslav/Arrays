# Moduł MyArrays: własne funkcje do obliczeń na listach liczb.

def second_largest(numbers):
    """Zwraca drugą największą różną wartość z listy."""
    if len(numbers) < 2:
        raise ValueError("Lista musi zawierać co najmniej dwie różne liczby.")

    largest = None
    second = None

    # Szukamy największej i drugiej największej różnej wartości bez max().
    for number in numbers:
        if largest is None or number > largest:
            second = largest
            largest = number
        elif number != largest and (second is None or number > second):
            second = number

    if second is None:
        raise ValueError("Lista musi zawierać co najmniej dwie różne liczby.")
    return second


def difference_largest_smallest(numbers):
    """Zwraca różnicę między największą a najmniejszą wartością."""
    if not numbers:
        raise ValueError("Lista nie może być pusta.")

    smallest = numbers[0]
    largest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
    return largest - smallest


def median(numbers):
    """Zwraca medianę; sortowanie wykonujemy ręcznie, bez sorted() i sort()."""
    if not numbers:
        raise ValueError("Lista nie może być pusta.")

    ordered = numbers.copy()
    # Bubble Sort — ręczne sortowanie rosnące.
    for i in range(len(ordered) - 1):
        for j in range(len(ordered) - i - 1):
            if ordered[j] > ordered[j + 1]:
                ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]

    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def smallest_and_largest(numbers):
    """Zwraca dwuelementową listę: [minimum, maksimum]."""
    if not numbers:
        raise ValueError("Lista nie może być pusta.")

    smallest = numbers[0]
    largest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
    return [smallest, largest]


def numbers_as_string(numbers):
    """Łączy wartości listy w tekst, używając znaku minus jako separatora."""
    return "-".join(str(number) for number in numbers)
