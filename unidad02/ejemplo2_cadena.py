fichero = input("Dime el nombre del fichero: ").strip()

if fichero.endswith(".png") or fichero.endswith(".jpg"):
    print("Es fichero")
else:
    print("No es un fichero")