# Genere una contraseña de texto que será la contraseña. Luego pida al usuario que ingrese la contraseña. Mientras la contraseña no sea la correcta
# debe continuar a pedir la contraseña. Si esta es correcta, se deja continuar al resto de programa.

password = "Santiago2006"
texto = input("Ingrese la contraseña: ")
while password != texto:
    print("Contraseña incorrecta")
    texto = input("Ingrese la contraseña nuevamente: ")

print("Acceso permitido")