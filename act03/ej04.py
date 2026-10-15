caracter=input("Carácter para el borde: ")
ancho=int(input("Ancho interior: "))
alto=int(input("Alto interior: "))

print(caracter * (ancho + 2))
print((caracter + " " * ancho + caracter + "\n") * alto, end="")
print(caracter * (ancho + 2))