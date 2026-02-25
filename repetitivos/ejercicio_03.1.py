#


veces = int(input("Cuantos numeros quieres ingresar?"))

igual_0 = 0
mayor_0 = 0
menor_0 = 0
for i in range (veces):
	num = int(input("Ingresa un numero :"))
	if num == 0:
		igual_0 += 1
	elif num < 0:
		menor_0 += 1
	else:
		mayor_0 += 1

print("ingresaste", igual_0, "ceros")
print("ingresaste" , menor_0, "Mayores a 0")
print("ingresaste", menor_0, "Menores a 0")