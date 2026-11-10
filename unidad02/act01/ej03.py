# Calcula cuántas cajas, packs y botellas sueltas salen al empaquetar.
BOTELLAS_PACK = 6
PACKS_CAJA = 4

botellas = int(input("Botellas a empaquetar: "))
botellas_caja = BOTELLAS_PACK * PACKS_CAJA

cajas = botellas // botellas_caja
# Esperaba sobran = 10 y el depurador mostraba 5. La variable sobran debería contener las botellas que quedan después de llenar las cajas. Pero el programa está utilizando // (división entera), cuando debería utilizar % (resto).
sobran = botellas % botellas_caja
packs = sobran // BOTELLAS_PACK
sueltas = sobran % BOTELLAS_PACK

print("Cajas completas:", cajas)
print("Packs sueltos:", packs)
print("Botellas sueltas:", sueltas)