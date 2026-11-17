temperatura1 = float(input("Lectura 1 (°C): "))
temperatura2 = float(input("Lectura 2 (°C): "))
temperatura3 = float(input("Lectura 3 (°C): "))

maxima = max(temperatura1, temperatura2, temperatura3)
minima = min(temperatura1, temperatura2, temperatura3)
media = (temperatura1 + temperatura2 + temperatura3) / 3

print(f"Máxima: {maxima} °C | Mínima: {minima} °C | Media: {media:.1f} °C")

if maxima >= 90:
    print("Estado: CRÍTICO - apagando el equipo")
elif maxima >= 75:
    print("Estado: ALTO - revisa la ventilación")
else:
    print("Estado: normal")

if maxima - minima > 15:
    print("Aviso: lecturas inestables, revisa el sensor")