#Descripción: calcula la cantidad de estanterías que necesitas en relacion a la cantidad de libros que tengas
#Fecha: 29/10/2026
#Hecho por: Ángel Infante Cansino

libros = int(input("Libros a colocar: "))

estante = libros // 30
estantería = estante // 5
librossueltos = 5 // estante

print("Estanterías completas: ", estantería, )
print("Estantes llenos: ", estante, )
print("Libros sueltos: ", librossueltos)