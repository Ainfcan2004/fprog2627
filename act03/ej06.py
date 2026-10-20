total=int(input("Tareas totales: "))
completadas=int(input("Tareas completadas: "))

porcentaje=completadas * 100 // total

barras=porcentaje // 10
carga="[" + "#" * barras + "." * (10 - barras) + "]"

print("Progreso: " + carga + " " + str(porcentaje) + " %")