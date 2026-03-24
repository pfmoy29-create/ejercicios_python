# Función recursiva para calcular el factorial
def calcular_factorial(num):
    if num == 1:
        return 1
    else:
        return num * calcular_factorial(num - 1)

if __name__ == "_main_":
    numero1 = int(input("Número: "))
    if numero1 < 1:
        print("El factorial solo se calcula para números enteros positivos.")
    else:
        resultado = calcular_factorial(numero1)
        print(f"El factorial es: {resultado}")