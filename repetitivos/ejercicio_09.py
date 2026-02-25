def calcular_potencia():

    try:
        base = float(input("Dame la base de la potencia: "))
    except ValueError:
        print("Error: Por favor, introduce un número para la base.")
        return  

    while True:
        try:
            exponente = int(input("Dame el exponente de la potencia: "))
            if exponente < 0:
                print("ERROR: El exponente debe ser positivo")
            else:
                break  
        except ValueError:
            print("Error: Por favor, introduce un número entero para el exponente.")

    
    potencia = 1
    for i in range(exponente): 

    
    print("Potencia:", potencia)

calcular_potencia()