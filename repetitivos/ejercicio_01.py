# Programa

num = int(input("Ingresa un numero :"))

factorial = 1
for i in range(num):
	factorial *= (i + 1)

print("El factorial de ", num, 'es', factorial)