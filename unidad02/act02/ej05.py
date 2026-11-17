mayor_instalada = int(input("Versión instalada - número mayor: "))
menor_instalada = int(input("Versión instalada - número menor: "))

mayor_disponible = int(input("Versión disponible - número mayor: "))
menor_disponible = int(input("Versión disponible - número menor: "))

print(f"Instalada: {mayor_instalada}.{menor_instalada} | Disponible: {mayor_disponible}.{menor_disponible}")

if mayor_disponible > mayor_instalada:
    print("Actualización IMPORTANTE disponible: haz una copia de seguridad antes.")
else:
    if mayor_disponible == mayor_instalada:
        if menor_disponible > menor_instalada:
            print("Actualización menor disponible")
        elif menor_disponible == menor_instalada:
            print("El programa está actualizado")
        else:
            print("La versión instalada es más reciente que la publicada")
    else:
        print("La versión instalada es más reciente que la publicada")