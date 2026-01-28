#Algoritmo que pida un número y diga si es positivo, negativo o 0.

print("Dime el numero :")
num_input = input()

num = int(num_input)

if num == 0:
	print("Es igual a 0")
elif num > 0:
	print("Es positivo ")
else:
	print("Es negativo ")