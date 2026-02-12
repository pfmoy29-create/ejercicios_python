# Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos 
# en el plano. Calcula y muestra la distancia entre ellos.

print("Dime las cordenadas del punto 1:")

x1 = int(input("Ingresa x1: "))
y1 = int(input("Ingresa x2: "))

print("Dime las cordenadas del punto 2 :")

x2 = int(input("Ingresa x2 :"))
y2 = int(input("Ingresa y2 :"))

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("La distancia entre los dos puntos es :" , distancia)