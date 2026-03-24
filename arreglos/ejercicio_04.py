# Programa que declara un vector de diez elementos enteros y pide números para
# rellenarlo hasta que se llene el vector o se introduzca un número negativo.
# Entonces se debe imprimir el vector (solo los elementos introducidos).

def VectorPositivo():
    vector = [0] * 10
    tam_vector = 10
    indice = 0
    num = 0
    while indice < tam_vector:
        print(f"Introduce un numero en el vector. Numero {indice + 1}: ", end="")
        num = int(input())
        if num < 0:
            break
        else:
            vector[indice] = num
            indice += 1
    print("\nElementos introducidos en el vector:")
    for i in range(0, indice):
        print(f"{vector[i]} ", end="")
    print() 
VectorPositivo()