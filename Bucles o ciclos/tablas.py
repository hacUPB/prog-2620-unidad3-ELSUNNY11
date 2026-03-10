numero = int(input("Ingrese el número: "))

for i in range(1,10,2): # Range los números son inicio, fin, pasos
    print(f"{numero} x {i} = {numero*i}")

print("Ingrese 10 valores: ")
for i in range(10):
    valor = int(input(f"Ingrese el valor {i+1}: "))