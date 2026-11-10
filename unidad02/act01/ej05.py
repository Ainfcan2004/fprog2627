# Sigue las monedas de un equipo de un videojuego.
PERSONAJES = 5

# Esperaba monedas = 10 (int) y el depurador mostraba "10" (str). La variable monedas es de tipo str (texto), mientras que ganadas es de tipo int (número entero).
monedas = int(input("Monedas iniciales: "))
ganadas = int(input("Monedas ganadas en la partida: "))
gastadas = int(input("Monedas gastadas en la tienda: "))

monedas += ganadas
print("Tras la partida:", monedas)
monedas -= gastadas
print("Tras la tienda:", monedas)
monedas //= PERSONAJES
print("Cada personaje:", monedas)