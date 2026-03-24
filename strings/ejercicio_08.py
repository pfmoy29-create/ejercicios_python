# Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a 
# minúsculas y viceversa.

def convertir_may_min():
    cad = input("Introduce una cadena: ")
    newcad = ""
    
    for i in range(len(cad)):
        caracter_actual = cad[i]
        
       
        if caracter_actual.isupper():
            
            newcad += caracter_actual.lower()
        
        elif caracter_actual.islower():
           
            newcad += caracter_actual.upper()
        else:
            
            newcad += caracter_actual
            
    print(f"La cadena convertida es: {newcad}")


convertir_may_min()