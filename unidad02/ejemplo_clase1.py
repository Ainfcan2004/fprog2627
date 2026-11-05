segundos = int(input("Segundos: "))
minutos = segundos % 60
resto = segundos // 60
print(f"{minutos} minutos y {resto} segundos")