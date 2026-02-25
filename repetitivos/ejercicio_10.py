# Tabla de multiplicar 

def tablas_de_multiplicar():

    for tabla in range(1, 11):  
        for num in range(1, 11): 
            print(f"{tabla} * {num} = {tabla * num}")
        input("Presiona Enter para continuar...")  
        
tablas_de_multiplicar()