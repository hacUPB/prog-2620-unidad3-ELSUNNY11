'''La tienda ofrece una promoción, por la compra de 3 artículos, el costo del elemento de menor valor tiene un descuento del 50%'''

artículo1 = int(input("Ingrese el precio del articulo 1: "))
artículo2 = int(input("Ingrese el precio del arículo 2: "))
artículo3 = int(input("Ingrese el precio del arículo 3: ")) 

total = artículo1 + artículo2 + artículo3

if artículo1 < artículo2:
    temp = artículo1
else:
    temp = artículo2

if temp < artículo3:
    menor = temp
else:
    menor = artículo1   

total1 = total - (menor * 0.5)

print(f"Debe pagar con descuento: {total1}")
print(f"Precio sin descuento: {total}")


