precio = float(input("Precio del precio sin IVA: "))
iva = int(input("Porcentaje de IVA (%): "))

cuota_iva = precio * iva / 100
precio_final = precio + cuota_iva

print("Base imponible:", precio, "€")
print("IVA (", iva, "%):", cuota_iva, "€")
print("Total a pagar:", precio_final, "€")