# Calcula cuántas estanterías y estantes se llenan con los libros de una biblioteca.
LIBROS_ESTANTE = 30
ESTANTES_ESTANTERIA = 5

total = int(input("Libros a colocar: "))
# Esperaba libros_estanteria = 150 y el depurador mostraba 35. El programa está sumando 30 + 5, cuando debería multiplicar 30 × 5.
libros_estanteria = LIBROS_ESTANTE * ESTANTES_ESTANTERIA

estanterias = total // libros_estanteria
resto = total % libros_estanteria
estantes = resto // LIBROS_ESTANTE
sueltos = resto % LIBROS_ESTANTE

print("Estanterías completas:", estanterias)
print("Estantes llenos en la última:", estantes)
print("Libros sueltos:", sueltos)