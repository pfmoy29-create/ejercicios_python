# Diseñar el algoritmo correspondiente a un programa, que:
# * Crea una tabla bidimensional de longitud 5x5 y nombre 'matriz'.
# * Carga la tabla con valores numéricos enteros.
# * Suma todos los elementos de cada fila y todos los elementos de cada columna
# visualizando los resultados en pantalla.

def SumarFilasColumnasMatriz():
    matriz = [[0 for _ in range(5)] for _ in range(5)]
    fila = 0
    col = 0
    num_filas = 2
    num_cols = 2
    print("--- Ingrese los elementos de la matriz (5x5) ---")
    for fila in range(num_filas):
        for col in range(num_cols):
            matriz[fila][col] = int(input(f"Ingrese el elemento en la fila {fila+1}, columna {col+1}: "))
    print("\n--- Suma de cada fila ---")
    for fila in range(num_filas):
        suma_fila = 0
        for col in range(num_cols):
            suma_fila += matriz[fila][col]
        print(f"Suma de la fila {fila+1}: {suma_fila}")
    print("\n--- Suma de cada columna ---")
    for col in range(num_cols):
        suma_columna = 0
        for fila in range(num_filas):
            suma_columna += matriz[fila][col]
        print(f"Suma de la columna {col+1}: {suma_columna}")
SumarFilasColumnasMatriz()