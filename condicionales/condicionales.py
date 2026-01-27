#Condicionales

#if, else, elif

"""
if ex_bool:
intrucciones:

if exp_bool:
intrucciones
else:
intrucciones

if exp_bool:
intrucciones
elif exp_bool:
intrucciones
else:
intrucciones
"""

print('Inicio')

numero = int(input('Ingresa el numero: '))

if numero > 0:
	print('Es un numero Positivo')
else:
	print(' Es cero')
elif numero == 0:

	print('No es un numero Positivo')

	print('Fin')