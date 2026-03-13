"""Para subir a la nueva montaña rusa del parque, los visitantes deben medir al menos 150 cm.
Escribe un programa donde declares una variable altura_visitante (asígnale el valor que quieras). 
Luego, utiliza un operador relacional para imprimir True si puede subir o False si no puede."""

altura_visitante = int(input("Ingrese la altura suya: "))

if altura_visitante >= 150:
    print("Puede subir")
else:
    print("No puede subir")