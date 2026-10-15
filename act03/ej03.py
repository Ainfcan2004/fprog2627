segundos=int(input("Introduce una cantidad de segundos: "))

horas=segundos // 3600
minutos=(segundos % 3600) // 60
segundos_restantes=segundos % 60

print(segundos, "segundos son", horas, "h", minutos, "min", segundos_restantes, "s")
print("Formato reloj:", horas, ":", minutos, ":", segundos_restantes)