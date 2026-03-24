# Función EsMultiplo: Recibe dos número e indica si el primero el múltiplo del 
# segundo. Para ello calculo el resto de la división, si es 0 es múltiplo.
# Parámetros de entrada: dos números
# Dato devuelto: múltiplo: Valor lógico verdadero si el primero es múltiplo 
# del segundo, Falso en caso contrario.

def es_multiplo (num1,num2):
    return num1 % num2 == 0

# Definir numero1,numero2 como entero:
print("Numero 1:")
numero1 = int(input())
print("Numero 2:")
numero2 = int(input())

if es_multiplo(numero1,numero2):
    print(numero1,"es multiplo de", numero2)
else:
    print(numero1,"no es multiplo de",numero2)