# Función que calcula el máximo y mínimo de un vector (lista en Python)
# Usa parámetros por referencia (mediante listas, ya que Python pasa objetos por referencia)
def calcular_max_min(vector, max_min):
    
    max_min[0] = vector[0]
    max_min[1] = vector[0]
    
  
    for num in vector:
        if num > max_min[0]:
            max_min[0] = num
        if num < max_min[1]:
            max_min[1] = num
if _name_ == "_main_":
    lista = [0] * 10
    size_lista = 10
    
    print("Ingresa 10 números enteros:")
    for i in range(size_lista):
        lista[i] = int(input(f"Número {i+1}: "))
    
    max_min = [0, 0]
    calcular_max_min(lista, max_min)
    
    print(f"\nEl valor máximo es: {max_min[0]}")
    print(f"El valor mínimo es: {max_min[1]}")