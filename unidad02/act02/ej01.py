LIMITE_AVISO=90
LIMITE_COMPLETO=100

capacidad_disco=float(input("Capacidad total (GB):"))
capacidad_usada=float(input("Capacidad usada (GB):"))

disco_ocupado = capacidad_usada / capacidad_disco * 100

print(f"Disco ocupado: {disco_ocupado:.1f} %")

if disco_ocupado == LIMITE_COMPLETO:
    print("Espacio suficiente")
elif disco_ocupado >= LIMITE_AVISO:
    print("¡Aviso El disco esta casi lleno!")
else:
    print("Espacio suficiente")