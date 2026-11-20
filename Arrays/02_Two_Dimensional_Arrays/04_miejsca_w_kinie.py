# Zadanie 4: statystyki miejsc w sali kinowej i status wybranego miejsca.
# A oznacza miejsce dostępne (Available), B — zarezerwowane (Booked).
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    # Liczba miejsc to liczba wierszy pomnożona przez liczbę kolumn.
    return len(seats) * len(seats[0])

def seats_available(seats):
    # Zliczamy wszystkie komórki oznaczone literą A.
    total = 0
    for row in seats:
        for seat in row:
            if seat == 'A':
                total += 1
    return total

def seats_booked(seats):
    # Zliczamy wszystkie komórki oznaczone literą B.
    total = 0
    for row in seats:
        for seat in row:
            if seat == 'B':
                total += 1
    return total

def seat_status(seats, row, place):
    # Argumenty row i place są numerowane od 1, indeksy listy od 0.
    if not (1 <= row <= len(seats) and 1 <= place <= len(seats[0])):
        return "Incorrect seat number"
    status = seats[row - 1][place - 1]
    return "Available" if status == 'A' else "Booked"

print("CINEMA INFORMATION TABLE")
print("Total seats:", seats_total(cinema_seats))
print("Seats available:", seats_available(cinema_seats))
print("Seats booked:", seats_booked(cinema_seats))
print("Seat in row 1, place 1:", seat_status(cinema_seats, 1, 1))
print("Seat in row 5, place 5:", seat_status(cinema_seats, 5, 5))
print("Seat in row 3, place 5:", seat_status(cinema_seats, 3, 5))
