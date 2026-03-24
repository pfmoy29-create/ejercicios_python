import math  # Importamos la librería math para usar el valor de PI

# Función que calcula área y perímetro de una circunferencia
# Devolvemos ambos valores directamente (forma más sencilla en Python)
def calcular_area_perimetro(radio):
    area = math.pi * radio ** 2  
    perimetro = 2 * math.pi * radio 
    return area, perimetro

if __name__ == "_main_":
    radio = float(input("Introduce el radio: "))
    
    area, perimetro = calcular_area_perimetro(radio)
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")