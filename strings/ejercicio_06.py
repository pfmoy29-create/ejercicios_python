# Realizar un programa que dada una cadena de caracteres por caracteres, genere 
# otra cadena resultado de invertir la primera.

def invertir_cadena():
    cad = input("Introduce una cadena: ")
    invertida = ""
    
    for i in range(len(cad) - 1, -1, -1):
        invertida += cad[i]
    print(f"La cadena invertida es: {invertida}")


invertir_cadena()