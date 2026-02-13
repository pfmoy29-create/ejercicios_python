# Realiza un algoritmo que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
# El exponente sea positivo, sólo tienes que imprimir la potencia.

import math 

print('Calcular potencia')

base = int(input('Dime la base: '))
exponente = int(input('Dime el exponente: '))

if exponente > 0: 
	resultado = base ** exponente
	print('La potencia es: ',base ** exponente)
elif exponente == 0:
	print('La potencia es 1')
else:
	resultado = 1 / (base ** abs(exponente))
	print('La potencia es ',1/(base ** abs(exponente)))