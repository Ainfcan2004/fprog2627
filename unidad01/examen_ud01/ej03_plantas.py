#Descripción: el registro del inventario de plantas de un vivero
#Fecha: 29/10/2026
#Hecho por: Ángel Infante Cansino

plantas = int(input("Plantas iniciales: "))
compradas = int(input("Plantas compradas: "))
secadas = int(input("Plantas que se secan: "))

plantas += compradas
print("Tras la compra: ", plantas)

plantas -= secadas
print("Tras la compra: ", plantas)

plantas = plantas * 3
print("Tras los esquejes: ", plantas)

plantas = plantas // 5
print("En cada invernadero: ", round(plantas))