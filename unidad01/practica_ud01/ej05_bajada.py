caracter=input("Carácter: ")
ancho=int(input("Ancho de cada peldaño: "))

escalera = caracter * ancho
primero= escalera + escalera
segundo= primero + escalera
tercero= segundo + escalera

print("\n", tercero, "\n", segundo, "\n", primero, "\n", escalera, "\n")

mide= ancho * 4

print("El primer peldaño mide", mide, "caracteres")
