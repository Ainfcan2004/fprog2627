precio_cafe=1.35
precio_tostada=2.10
precio_zumo=2.80
cantidad_cafe=3
cantidad_tostada=4
cantidad_zumo=1
amigos=4
propina=0.10

total = (precio_cafe * cantidad_cafe)+\
        (precio_tostada * cantidad_tostada)+\
        (precio_zumo * cantidad_zumo)

cada_uno = total / amigos
total_con_propina = total * (1 + propina)

print("Total: ", total, "€", "\n", 
"Cada uno paga: ", cada_uno, "€", "\n", 
"Total con propina: ", total_con_propina, "€")