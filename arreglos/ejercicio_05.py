import random
def OrdenarVector():
    vector = [0] * 10
    cambios = 0
    aux = 0
    indice = 0
    tam_vector = 10
    for indice in range(0, tam_vector):
        vector[indice] = random.randint(1, 10)
    cambios = 1  
    while cambios != 0:
        cambios = 0  
        for indice in range(0, tam_vector - 1):
            if vector[indice] > vector[indice + 1]:
                aux = vector[indice]
                vector[indice] = vector[indice + 1]
                vector[indice + 1] = aux
                cambios += 1  
    print("Vector ordenado de menor a mayor:")
    for indice in range(0, tam_vector):
        print(f"{vector[indice]} ", end="")
    print() 
OrdenarVector()