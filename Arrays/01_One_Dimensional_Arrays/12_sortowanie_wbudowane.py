# Zadanie 12: sortowanie danych za pomocą wbudowanej funkcji sorted().
# sorted() zwraca nową, posortowaną listę i nie zmienia oryginału.
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
file_names = [
    "report.docx", "presentation.pptx", "data.csv", "photo.jpg",
    "notes.txt", "invoice.pdf", "resume.docx", "budget.xlsx",
    "meeting.mp4", "schedule.pdf"
]

print("Distances ascending:", sorted(distances_traveled))
# reverse=True ustawia kolejność malejącą.
print("Temperatures descending:", sorted(daily_temperatures, reverse=True))
print("File names ascending:", sorted(file_names))
