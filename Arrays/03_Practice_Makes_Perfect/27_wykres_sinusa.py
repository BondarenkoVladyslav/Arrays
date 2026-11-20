# Zadanie 27: rysowanie funkcji y = sin(x) dla kątów od 0 do 360 stopni.
import math
import matplotlib.pyplot as plt

angles = list(range(0, 361))
# math.sin() przyjmuje radiany, dlatego konwertujemy stopnie przez math.radians().
sine_values = [math.sin(math.radians(angle)) for angle in angles]

plt.plot(angles, sine_values)
plt.title("y = sin(x)")
plt.xlabel("Angle in degrees")
plt.ylabel("sin(x)")
plt.xticks(range(0, 361, 30))
plt.grid(True)
plt.show()
