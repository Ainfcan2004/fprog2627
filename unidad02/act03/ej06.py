edad_texto = input("Edad: ").strip()

if not edad_texto.isdigit():
    print(f"Error: escribe un número entero")
else:
    edad = int(edad_texto)

    if edad > 120:
        print(f"Error: edad no válida")
    elif edad <= 11:
        print(f"Infancia")
    elif edad <= 17:
        print(f"Adolescencia")
    elif edad <= 64:
        print(f"Edad adulta")
    else:
        print(f"Jubilación")
