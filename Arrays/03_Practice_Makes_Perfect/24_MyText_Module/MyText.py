# Moduł MyText: funkcje do analizy tekstu.

def word_count(text):
    """Zwraca liczbę słów w tekście."""
    return len(text.split())


def words_longest_first(text):
    """Zwraca słowa od najdłuższego do najkrótszego."""
    words = text.split()
    return sorted(words, key=len, reverse=True)


def words_alphabetically(text):
    """Zwraca słowa w kolejności alfabetycznej bez rozróżniania wielkości liter."""
    words = text.split()
    return sorted(words, key=str.casefold)
