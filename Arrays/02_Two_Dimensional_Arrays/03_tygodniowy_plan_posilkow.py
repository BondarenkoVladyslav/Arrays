# Zadanie 3: wyświetlanie planu posiłków na cały tydzień.
# Każdy wewnętrzny wiersz zawiera: śniadanie, lunch i kolację.
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]

def weekday(day_number):
    # Zamieniamy numer dnia 1–7 na nazwę dnia tygodnia.
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
    return weekdays[day_number - 1]

def day_meal_plan(plan, day_number):
    # Pobieramy posiłki dla wybranego dnia.
    meals = plan[day_number - 1]
    # Łączymy trzy nazwy w jeden tekst oddzielony przecinkami.
    return ", ".join(meals)

print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
for day_number in range(1, len(meal_plan) + 1):
    print(f"{weekday(day_number)}: {day_meal_plan(meal_plan, day_number)}")
