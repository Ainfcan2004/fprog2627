ip = input("Dirección IP: ").strip()

if ip.count(".") != 3 or " " in ip:
    print(f"Formato no válido")
elif ip.startswith("127."):
    print(f"{ip} es una IP de loopback (el propio equipo)")
elif ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.16."):
    print(f"{ip} es una IP privada")
else:
    print(f"{ip} es una IP pública")
