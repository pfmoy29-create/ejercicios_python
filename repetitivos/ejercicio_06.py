# Escribir un programa que imprima pares entre dos numeros


num1= int(input("Introduce el numero 1:"))
num2 = int(input("Introduce el numero 2:"))

if num1 % 2 == 1:
	num1 = num1 + num1

for num in range(num1, num2 + 1,2):
	print(num, end= " ")