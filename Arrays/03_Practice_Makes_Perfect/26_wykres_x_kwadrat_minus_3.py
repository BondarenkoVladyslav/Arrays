# Zadanie 26: rysowanie wykresu funkcji f(x) = x^2 - 3.
import matplotlib.pyplot as plt

x = []
y = []

# Tworzymy argumenty od -100 do 100 włącznie.
for n in range(-100, 101):
    x.append(n)

# Dla każdego x obliczamy wartość funkcji x^2 - 3.
for n in x:
    y.append(n ** 2 - 3)

# Rysujemy wykres i podpisujemy osie.
plt.plot(x, y)
plt.title("f(x) = x^2 - 3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
