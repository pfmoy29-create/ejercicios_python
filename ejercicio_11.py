# Pide al usuario dos números y muestra la "distancia" entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

import math

print("Calcular distancia")

num_01 = int(input("Dime el numero_01:"))
num_02 = int(input("Dime el numero_02:"))

distancia = abs(num_01 - num_02)

print("distancia: ", abs(num_01 - num_02))