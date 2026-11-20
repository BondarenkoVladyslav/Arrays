# Zadanie 8: znalezienie imienia o największej liczbie znaków.
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest_name = names[0]
for name in names:
    # len() zwraca liczbę znaków w aktualnym imieniu.
    if len(name) > len(longest_name):
        longest_name = name

print("Names:", *names)  #* rozbija liste na pojedyncze elementy oddzielone spacjami
print("Longest name:", longest_name)
