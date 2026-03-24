# Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
# sustituye la aparición del primer carácter en la cadena por el segundo carácter.

def sustituir_caracter():
    cad = input("Introduce una cadena: ")
    
    car_buscar = ""
    while len(car_buscar) != 1:
        car_buscar = input("Introduce un caracter a buscar: ")
        if len(car_buscar) != 1:
            print("Por favor, introduce solo un caracter.")

    car_sustituir = ""
    while len(car_sustituir) != 1:
        car_sustituir = input("Introduce un caracter para sustituir: ")
        if len(car_sustituir) != 1:
            print("Por favor, introduce solo un caracter.")

    newcad = ""
    for i in range(len(cad)):
       
        if cad[i] == car_buscar:
          
            newcad += car_sustituir
        else:
            
            newcad += cad[i]
            
    print(f"La cadena modificada es: {newcad}")


sustituir_caracter()