# Muestra el número de versión de un programa en tres formatos.
mayor = input("Versión mayor: ")
menor = input("Versión menor: ")
parche = input("Parche: ")

version = mayor + "." + menor + "." + parche
etiqueta = "v" + version
largo = "versión " + mayor + ", revisión " + menor + ", parche " + menor

print("Versión:", version)
print("Etiqueta de Git:", etiqueta)
print("Formato largo:", largo)