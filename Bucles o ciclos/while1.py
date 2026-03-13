# Solicitar dos números al usuario e imprimir los valores pares que hay entre dichos números.   

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Identificar al menor y mayor entre los dos
if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1

# Mostrar números pares entre ellos

while menor <= mayor:
    if menor % 2 == 0:
        print(menor)
    menor += 1
