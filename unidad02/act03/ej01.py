USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "Fprog2627"

usuario = input("Usuario: ").strip().lower()
contrasena = input("Contraseña: ")

if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
    print(f"Acceso concedido")
else:
    print(f"Usuario o contraseña incorrectos")
