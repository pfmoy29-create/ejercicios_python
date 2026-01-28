#Escribe un programa que pida un nombre de usuario y una contraseña 
#y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
#sino se da un error.

print('Ingresa el usuario:')
usuario_ingresado = input()

print('Introduce el password :')
password_ingresado = input()

if usuario_ingresado == "pepe" and password_ingresado == "asdasd":
	print("Has entrado al sistema ")

else: 
	print("usuario/password incorrecto ")
     
