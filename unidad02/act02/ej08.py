tamano = float(input("Tamaño del fichero: "))
unidad = input("Unidad (MB, GB o TB): ").upper()
velocidad = float(input("Velocidad de la conexión (Mb/s): "))

match unidad:
    case "MB":
        tamano_mb = tamano
    case "GB":
        tamano_mb = tamano * 1000
    case "TB":
        tamano_mb = tamano * 1000000
    case _:
        tamano_mb = -1

if tamano_mb == -1:
    print("Error: unidad no válida")
elif velocidad <= 0:
    print("Error: la velocidad debe ser mayor que 0")
else:
    segundos = round(tamano_mb * 8 / velocidad)

    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    print(f"Tiempo estimado: {horas} h {minutos} min {segundos_restantes} s")

    if horas >= 1:
        print("Descarga larga: prográmala para la noche")