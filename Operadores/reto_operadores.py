# Variables
edad_usuario = 18
saldo_billetera = 70.0
tiene_suscripcion_premium = True

precio_juego = 60

# Calcular precio con posible descuento
if tiene_suscripcion_premium:
    precio_final = precio_juego * 0.9
else:
    precio_final = precio_juego

# Verificar si la compra es posible
compra_exitosa = (edad_usuario >= 17) and (saldo_billetera >= precio_final)

print(compra_exitosa)

"""Reto Final – Operadores en Python

En este reto lo que más se me dificultó fue combinar correctamente los operadores lógicos y relacionales para evaluar si la compra podía realizarse o no. Especialmente entender cómo usar `and` para que se cumplieran varias condiciones al mismo tiempo, como la edad mínima y tener suficiente saldo.

También tuve que pensar primero en calcular el precio final del juego aplicando el descuento del 10% si el usuario tenía suscripción premium. Para resolverlo, separé el problema en pasos: primero calculé el precio final usando operadores aritméticos y luego evalué las condiciones usando operadores relacionales y lógicos. De esta manera el programa quedó más claro y fácil de entender."""