descripcion = input("Describe el problema: ").strip()

descripcion_minusculas = descripcion.lower()

if "contraseña" in descripcion_minusculas or "usuario" in descripcion_minusculas:
    departamento = "Cuentas de usuario"
elif "impresora" in descripcion_minusculas or "tóner" in descripcion_minusculas:
    departamento = "Periféricos"
elif "internet" in descripcion_minusculas or "wifi" in descripcion_minusculas or "conexión" in descripcion_minusculas:
    departamento = "Redes"
else:
    departamento = "Soporte general"

if "urgente" in descripcion_minusculas or descripcion.isupper():
    prioridad = "ALTA"
else:
    prioridad = "normal"

print(f"Departamento: {departamento}")
print(f"Prioridad: {prioridad}")
