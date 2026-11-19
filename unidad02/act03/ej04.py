LONGITUD_MINIMA = 8
LONGITUD_FUERTE = 12

usuario = input("Usuario: ").strip()
contrasena = input("Nueva contraseña: ")

if len(contrasena) < LONGITUD_MINIMA:
    print(f"Error: debe tener al menos {LONGITUD_MINIMA} caracteres")
elif " " in contrasena:
    print(f"Error: no puede contener espacios")
elif contrasena.isdigit():
    print(f"Error: no puede estar formada solo por números")
elif contrasena.isalpha():
    print(f"Error: no puede estar formada solo por letras")
elif not any(letra.isupper() for letra in contrasena):
    print(f"Error: debe tener al menos una letra mayúscula")
elif usuario.lower() in contrasena.lower():
    print(f"Error: no puede contener el nombre de usuario")
else:
    print(f"Contraseña válida")

    if len(contrasena) >= LONGITUD_FUERTE:
        print(f"Nivel: fuerte")
    else:
        print(f"Nivel: aceptable")
