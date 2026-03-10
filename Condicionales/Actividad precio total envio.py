'''
Un almacén cobra $9 000 por costos de envío, pero ofrece el envio a domicilio gratis para compras superiores a $100 000. En caso contrario, no hay ningún descuento. Solicite al usuario el valor de la compra y calcule el valor total a pagar.
'''

# La moneda es en Pesos colombianos 
compra = int(input("Ingrese el valor de la compra: "))
envio = 0
if compra < 100000: 
    envio = 9000    
total = compra + envio  

print(f"El valor a pagar es ${total}")  

