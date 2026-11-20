# Zadanie 5: sortowanie nazw gier i wyświetlanie ich za pomocą while.
computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# sorted() tworzy nową listę uporządkowaną alfabetycznie.
sorted_games = sorted(computer_games)

# Indeks wskazuje aktualną pozycję na liście.
index = 0

# Pętla działa, dopóki indeks jest mniejszy od liczby gier.
while index < len(sorted_games):
    # Numerujemy elementy od 1, dlatego dodajemy 1 do indeksu.
    print(f"{index + 1}. {sorted_games[index]}")
    index += 1
