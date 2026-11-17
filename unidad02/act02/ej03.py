MIN_BATERIA = 0
MAX_BATERIA = 100
LIMITE_ALTA = 80
LIMITE_MEDIA = 20

bateria = int(input("Batería (%): "))

if bateria < MIN_BATERIA:
    print("Valor no válido")
elif bateria > MAX_BATERIA:
    print("Valor no válido")
elif bateria >= LIMITE_ALTA:
    print("Batería alta")
elif bateria >= LIMITE_MEDIA:
    print("Batería media")
elif bateria > MIN_BATERIA:
    print("Batería baja: conecta el cargador")
else:
    print("Batería agotada: apagando el equipo")