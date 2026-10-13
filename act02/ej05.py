examen1=6.5
examen2=4.0
proyecto=7.2

teoria=(examen1 + examen2) / 2
final=((examen1 + examen2) / 2) * 0.4 + proyecto * 0.6
aprobado=((examen1 + examen2) / 2) * 0.4 + proyecto * 0.6 >= 5

print("Media de teoría: ", teoria)
print("Nota final: ", final)
print("¿Aprobado?: ", aprobado)

sin= (examen1 + examen2 / 2 * 0.4 + proyecto * 0.6)
print("Nota final sin paréntesis:", sin)
