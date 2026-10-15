nombre=input("¿como te llamas? ")
apellido=input("¿y tu apellido? ")
edad=input("¿cuantos años tienes? ")
ciudad=input("¿en que ciudad vives? ")

si=int(edad)+1

print("="*35)
print("\tFICHA DE ALUMNO/A")
print("="*35)

print("Nombre: ", nombre, apellido)
print("Edad:   ", edad)
print("Ciudad: ", ciudad)

print("-"*35)
print("El año que viene tendrás ", si, " años.")
print("="*35)