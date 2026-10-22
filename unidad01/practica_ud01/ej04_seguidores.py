iniciales=int(input("Seguidores iniciales: "))
nuevos=int(input("Seguidores nuevos: "))
perdidos=int(input("Seguidores que se van: "))

iniciales = iniciales + nuevos
print("Tras los nuevos:", iniciales)
iniciales = iniciales - perdidos
print("Tras las bajas:", iniciales)
iniciales *=3
print("Tras el vídeo viral:", iniciales)
iniciales /=2
print("Sin los bots:", iniciales)
