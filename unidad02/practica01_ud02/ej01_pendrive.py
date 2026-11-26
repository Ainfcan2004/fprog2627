copia_seguridad=10
peque=16
media=32
grand=64
gigant=128
capacidad_pendrive=int(input("Capacidad del pendrive (16, 32, 64 o 128 GB) : "))
capacidad_usada=int(input("GB ocupados: "))

capacidad_actual=capacidad_pendrive - capacidad_usada

#if capacidad_pendrive != peque or media or grand or gigant:
#    print("Error: no hay pendrives de esa capacidad")
#else:
if capacidad_actual == 0:
    print("El pendrive está lleno: usa otro pendrive")
elif capacidad_actual < 10:
    faltan= 10 - capacidad_actual
    print("Quedan", capacidad_actual, "GB libres: la copia de seguridad (10 GB) no cabe, faltan", faltan, "GB")
elif capacidad_actual > 10:
    print("Quedan ", capacidad_actual, "libres: la copia (10 GB) cabe")
else:
    print("Error: no hay pendrives de esa capacidad")