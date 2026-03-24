# Proceso para invertir los elementos de un vector
def VectorInverso():
    vector1 = [""] * 5
    vector2 = [""] * 5
    indicador1, indicador2 = 0, 0
    tam_vector1, tam_vector2 = 0, 0
    tam_vector1 = 5
    tam_vector2 = 5
    for indicador1 in range(0, tam_vector1):
        print(f"Dame la cadena {indicador1+1}:", end=" ")
        vector1[indicador1] = input()
    indicador2 = 0
    for indicador1 in range(tam_vector1 - 1, -1, -1):
        vector2[indicador2] = vector1[indicador1]
        indicador2 = indicador2 + 1
    for indicador2 in range(0, tam_vector2):
        print(f"La cadena {indicador2+1}: \"{vector2[indicador2]}\"")
VectorInverso()