def factorial(numero):
# si el numero es menor que 0 retornar "error"
    if numero < 0:
        return "error"

# multiplicar desde 1 hasta numero u acumular el
 
# si numero es 0 el factorial es 1   
    acumulador = 1
    for factor in range(1, numero+1):
        acumulador = acumulador * factor
        #acumulador *= factor
    return acumulador


resultado = factorial(6)
print(resultado)

