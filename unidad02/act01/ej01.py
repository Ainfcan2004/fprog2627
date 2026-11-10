# Muestra el número de versión de un programa en tres formatos.
mayor = input("Versión mayor: ")
menor = input("Versión menor: ")
parche = input("Parche: ")

version = mayor + "." + menor + "." + parche
etiqueta = "v" + version
# Esperaba parche = "3" y el depurador mostraba parche = "15". porque se habai vuelto a poner la variable menor en parche en lugar de la variable parche
largo = "versión " + mayor + ", revisión " + menor + ", parche " + parche

print("Versión:", version)
print("Etiqueta de Git:", etiqueta)
print("Formato largo:", largo)