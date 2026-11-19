ANIOS_GARANTIA = 3

anios = int(input("Años del equipo: "))
causa = input("Causa de la avería: ").strip().lower()

if anios < ANIOS_GARANTIA and not ("golpe" in causa or "agua" in causa):
    print(f"Reparación cubierta por la garantía")
else:
    print(f"Reparación no cubierta: hay que hacer un presupuesto al cliente")
