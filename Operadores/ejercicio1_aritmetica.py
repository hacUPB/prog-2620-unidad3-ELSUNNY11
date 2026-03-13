"""Ejercicio 1: La cuenta del restaurante
Imagina que fuiste a cenar con 3 amigos (son 4 en total). La cuenta fue de $85. Además, quieren dejar un 15% de propina.
Escribe un programa en Python que calcule:

1. El total de la propina.
2. El total a pagar (cuenta + propina).
3. Cuánto debe pagar cada uno, dividiendo en partes iguales."""
# Datos 
cuenta = 85
porcentaje_propina = 0.15
personas = 4

# Calcular propina
propina = cuenta * porcentaje_propina   

# Total a pagar 
total = cuenta + propina    

# Pago por persona
por_persona = total / personas

# Mostrar resultados    
print("Propina: ", propina)
print("Total a pagar: ",total)
print("Cada persona paga: ",por_persona)