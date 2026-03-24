# Programa que declara tres vectores 'vector1', 'vector2' y 'vector3' de cinco
# enteros cada uno, pide valores para 'vector1' y 'vector2' y calcule
# vector3=vector1+vector2.
def SumarVectores():
    vector1 = [0] * 5
    vector2 = [0] * 5
    vector3 = [0] * 5
    
    tam_vector = 5
    indice = 0
    for indice in range(0, tam_vector):
        print(f"Introduce el elemento {indice+1} del vector1: ", end="")
        vector1[indice] = int(input())
    for indice in range(0, tam_vector):
        print(f"Introduce el elemento {indice+1} del vector2: ", end="")
        vector2[indice] = int(input())
    for indice in range(0, tam_vector):
        vector3[indice] = vector1[indice] + vector2[indice]
    print("\nElementos del vector3 (suma de vector1 y vector2):")
    for indice in range(0, tam_vector):
        print(f"{vector3[indice]} ", end="")
    print() 
SumarVectores()