largo=float(input("Largo de la habitación (m): "))
ancho=float(input("Ancho de la habitación (m): "))

superficie= largo * ancho
coste= superficie * 12.50

print("Superficie: ", superficie, "m2")
print("Coste del suelo:", coste, "€")