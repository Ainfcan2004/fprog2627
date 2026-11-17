PUERTO_MIN = 0
PUERTO_MAX = 65535
LIMITE_BIEN_CONOCIDO = 1023
LIMITE_REGISTRADO = 49151

puerto = int(input("Número de puerto: "))

if puerto < PUERTO_MIN:
    print("Puerto no válido")
elif puerto > PUERTO_MAX:
    print("Puerto no válido")
elif puerto <= LIMITE_BIEN_CONOCIDO:
    print("Puerto bien conocido")

    match puerto:
        case 21:
            print("Servicio: FTP")
        case 22:
            print("Servicio: SSH")
        case 53:
            print("Servicio: DNS")
        case 80:
            print("Servicio: HTTP")
        case 443:
            print("Servicio: HTTPS")
        case _:
            print("Servicio: otro")

elif puerto <= LIMITE_REGISTRADO:
    print("Puerto registrado")
else:
    print("Puerto dinámico")