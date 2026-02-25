# Ejercicio de intervalos

def intervalo():
   
    suma_dentro_intervalo = 0
    cont_fuera_intervalo = 0
    igual_limites = False

    
    while True:
        try:
            lim_inf = int(input("Introduce el límite inferior del intervalo: "))
            lim_sup = int(input("Introduce el límite superior del intervalo: "))
            if lim_inf > lim_sup:
                print("ERROR: El límite inferior debe ser menor que el superior.")
            else:
                break  
        except ValueError:
            print("Error: Por favor, introduce números enteros.")

    
    while True:
        try:
            num = int(input("Introduce un número (0, para salir): "))
            if num == 0:
                break  
           
            if num > lim_inf and num < lim_sup:
                suma_dentro_intervalo += num
            else:
               
                cont_fuera_intervalo += 1

            
            if num == lim_inf or num == lim_sup:
                igual_limites = True

        except ValueError:
            print("Error: Por favor, introduce un número entero.")

    
    print("La suma de los números dentro del intervalo es", suma_dentro_intervalo)
    print("La cantidad de números fuera del intervalo es", cont_fuera_intervalo)
    if igual_limites:
        print("Se ha introducido algún número igual a los límites del intervalo.")
    else:
        print("No se ha introducido ningún número igual a los límites del intervalo.")


intervalo()