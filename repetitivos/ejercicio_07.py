# Realizar un algoritmo que muestre la tabla de multiplicar de un numero
# intrducido por teclado.

tabla = int(input("De que numero quieres mostrar la tabla de multiplicar:"))

for num in range (1,11):
	print(num, "*", tabla, "=", num * tabla)