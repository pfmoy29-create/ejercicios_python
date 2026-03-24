# Realizar un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado.

def contiene_subcadena():
    cad = input("Introduce una cadena: ")
    subcad = input("Introduce una subcadena a buscar: ")
    if subcad in cad:
        print("La cadena contiene la subcadena.")
    else:
        print("La cadena no contiene la subcadena.")

contiene_subcadena()