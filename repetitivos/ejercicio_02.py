# Programa que esconde un numero entre 1 y 20

import random

num = random.randint(1,100)

intentos = 1

while intentos <= 10:
	num_user = int(input("Adivina el numero:"))
	if num == num_user:
		print("ERES MUY BUENOS PATSSSS")
		print("En", intentos , "intentos")
		break
	elif num_user < num:
		print("Uno mayor")
	else:
		print("Uno menor")
	intentos += 1

if intentos > 10:
	print("perdiste tanto")