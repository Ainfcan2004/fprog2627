nombre_fichero = input("Nombre del fichero: ").strip()

fichero = nombre_fichero.lower()

if "." not in fichero:
    print(f"El fichero no tiene extensión")
elif fichero.endswith(".py"):
    print(f"Script de Python")
elif fichero.endswith((".jpg", ".png")):
    print(f"Imagen")
elif fichero.endswith((".pdf", ".docx")):
    print(f"Documento")
else:
    print(f"Tipo desconocido")
