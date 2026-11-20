# Zadanie 3: wyświetlanie listy od końca do początku.
numbers = [15, 8, 31, 47, 2, 19]
print("Existing array:", *numbers)  #* rozbija liste na pojedyncze elementy oddzielone spacjami

# reversed() przechodzi po elementach w odwrotnej kolejności.
print("Reverse array:", *reversed(numbers))
