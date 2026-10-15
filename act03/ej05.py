examen1=float(input("Nota del examen 1: "))
examen2=float(input("Nota del examen 2: "))
practicas=float(input("Nota de las prácticas: "))

nota_final=examen1 * 0.4 + examen2 * 0.4 + practicas * 0.2

print("\nExamen 1:       ", "*" * int(examen1), examen1)
print("Examen 2:       ", "*" * int(examen2), examen2)
print("Prácticas:      ", "*" * int(practicas), practicas)
print("Nota final:     ", "*" * int(nota_final), round(nota_final, 1))