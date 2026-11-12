HORA_MINIMA=1
PRECIO_HORA=25
IVA=0.21
DESPLAZAMIENTO=30

horas=float(input("Horas de trabajo: "))
contrato=input("¿Tiene contrato de mantenimiento? (s/n): ")

horas_facturadas=max(horas, HORA_MINIMA)

mano_obra= horas_facturadas * PRECIO_HORA

if contrato == "s":
    desplazamiento=0
else:
    desplazamiento=DESPLAZAMIENTO

subtotal = mano_obra + desplazamiento
precio_iva = subtotal * IVA
total = subtotal + precio_iva

print(f"Horas facturadas: {horas_facturadas} €")
print(f"Mano de obra: {mano_obra} €")
print(f"Desplazamiento: {desplazamiento} €")
print(f"Subtotal: {subtotal:.2f} €")
print(f"IVA ({IVA*100:.0F}%): {precio_iva:.2f} €")
print(f"TOTAL: {total:.2f} €")