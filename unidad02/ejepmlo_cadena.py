respuesta = input("¿Eres mayor de edad? (s/n)").strip()

if respuesta.lower() == "s":
    print("Acceso permitido")
elif respuesta.lower() == "n":
    print("Acceso denegado")
else:
    print("Opción no válida")