# algoritmo que pida numeros hasta que se intrduzca

suma = 0
numero = 0
while True:
	num = int(input("Ingresa un numero :"))
	if num == 0:
		break
	numero += 1
	suma += num

print("La suma de numero es :" , suma)
print("El promedio de los numeros es", suma / numero)