# Programa que guarda los nombres y las edades de los alumnos de un curso.
# Realiza un programa que introduzca el nombre y la edad de cada alumno.
# El proceso de lectura de datos terminará cuando se introduzca como nombre
# un asterisco (*) Al finalizar se mostrara los siguientes datos:
# * Todos lo alumnos mayores de edad.
# * Los alumnos mayores (los que tienen más edad)

def InformacionAlumnos():

    edad = [0] * 30
    
    nombre = [""] * 30
    edad_max = 0
    indice = 0
    tam_vector = 30 
    while indice < tam_vector:
        print(f"Introduce el nombre del alumno {indice + 1} (o * para finalizar): ", end="")
        nombre_actual = input()
        if nombre_actual == "*":
            break
        else:
            print(f"Introduce la edad de {nombre_actual}: ", end="")
            edad_actual = int(input())
            nombre[indice] = nombre_actual
            edad[indice] = edad_actual
            if edad_actual > edad_max:
                edad_max = edad_actual
            indice += 1
    print("\n--- Alumnos mayores de edad ---")
    alumnos_mayores_de_edad_encontrados = False
    for i in range(0, indice):
        if edad[i] >= 18:
            print(f"- {nombre[i]} (Edad: {edad[i]})")
            alumnos_mayores_de_edad_encontrados = True
    if not alumnos_mayores_de_edad_encontrados:
        print("No se ingresaron alumnos mayores de edad.")
    print("\n--- Alumno(s) con la edad máxima ---")
    alumnos_con_edad_maxima_encontrados = False
    for i in range(0, indice):
        if edad[i] == edad_max:
            print(f"- {nombre[i]} (Edad: {edad[i]})")
            alumnos_con_edad_maxima_encontrados = True
    if not alumnos_con_edad_maxima_encontrados and indice > 0:
        print("No se pudo determinar el alumno con la edad máxima.")
    elif indice == 0:
        print("No se ingresaron datos de alumnos.")
InformacionAlumnos()