# Zadanie 25: rysowanie odcinka od punktu (1, 3) do punktu (8, 10).
import matplotlib.pyplot as plt

# Listy grupują osobno współrzędne X oraz Y obu punktów: (1, 3) i (8, 10)
xpoints = [1, 8]
ypoints = [3, 10]

# Łączy punkty odcinkiem; marker="o" zaznacza widoczne kropki na końcach
plt.plot(xpoints, ypoints, marker="o")
plt.title("Line from (1, 3) to (8, 10)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()