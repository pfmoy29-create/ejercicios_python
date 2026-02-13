# nota, edad y sexo del usuario

nota = int(input("Introduce la nota:"))
edad = int(input("Introduce la edad :"))
sexo = (input("Introduce el sexo (F/M):"))

if nota >= 5 and edad >= 18:
	if sexo == "F":
		print("Aceptada")
	else:
		if sexo == "M":
			print("Posible")
		else:
			print("No Aceptada")
else:
				print("No Aceptada")