#

while True:

	while True:
		car = input("Introduce un caracter:")
		if len (car) == 1:
			break
		else:
			print("por favor, Introduce solo un caracter.")


	if car == " ":
		break

	if car.upper() in ["A","E","I","O","U" ]:
		print("VOCAL")
	else:
		print("NO VOCAL")

salir = input("Quieres salir?")