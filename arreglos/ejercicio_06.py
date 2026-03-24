# Proceso para determinar los días y el nombre de un mes dado.

def DiasDelMes():
    dias = [0] * 12
    nombre_mes = [""] * 12
    mes = 0

   
    dias[0] = 31 
    dias[1] = 28  
    dias[2] = 31  
    dias[3] = 30  
    dias[4] = 31  
    dias[5] = 30  
    dias[6] = 31  
    dias[7] = 31 
    dias[8] = 30  
    dias[9] = 31  
    dias[10] = 30 
    dias[11] = 31 

    nombre_mes[0] = "Enero"
    nombre_mes[1] = "Febrero"
    nombre_mes[2] = "Marzo"
    nombre_mes[3] = "Abril"
    nombre_mes[4] = "Mayo"
    nombre_mes[5] = "Junio"
    nombre_mes[6] = "Julio"
    nombre_mes[7] = "Agosto"
    nombre_mes[8] = "Septiembre"
    nombre_mes[9] = "Octubre"
    nombre_mes[10] = "Noviembre"
    nombre_mes[11] = "Diciembre"

    
    print("Ingrese el número de un mes (1-12): ", end="")
    mes = int(input())

    if 1 <= mes <= 12:
        indice_mes = mes - 1
        print(f"El mes de {nombre_mes[indice_mes]} tiene {dias[indice_mes]} días.")
    else:
        print("Número de mes inválido. Por favor, ingrese un número entre 1 y 12.")
DiasDelMes()