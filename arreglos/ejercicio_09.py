# Programa que guarda la temperatura mínima y máxima de 5 días.
# Realiza un programa que pida la temperatura media de cada día
# Los días con menos temperatura
# Se lee una temperatura por teclado y se muestran los días cuya temperatura
# máxima coincide con ella. Si no existe ningún día se muestra un mensaje de
# información.

def GestionTemperaturas():
    temperatura = [[0, 0] for _ in range(5)]
    existe_temperatura = False
    indice = 0
    cant_dias = 5
    temp_max = -100  
    temp_min = 100  
    print("--- Ingreso de temperaturas ---")
    for indice in range(cant_dias):
        while True:
            temp_min_dia = int(input(f"Ingrese la temperatura mínima del día {indice + 1}: "))
            temp_max_dia = int(input(f"Ingrese la temperatura máxima del día {indice + 1}: "))
            if temp_min_dia <= temp_max_dia:
                temperatura[indice][0] = temp_min_dia
                temperatura[indice][1] = temp_max_dia
                if temp_min_dia < temp_min:
                    temp_min = temp_min_dia
                if temp_max_dia > temp_max:
                    temp_max = temp_max_dia
                break
            else:
                print("Error: La temperatura mínima no puede ser mayor que la máxima. Intente de nuevo.")
    print("\n--- Resultados ---")
    print("Temperatura media de cada día:")
    for indice in range(cant_dias):
        temp_media_dia = (temperatura[indice][0] + temperatura[indice][1]) / 2
        print(f"Día {indice + 1}: {temp_media_dia:.1f}°C")
    print(f"\nDías con la temperatura mínima general ({temp_min}°C):")
    for indice in range(cant_dias):
        if temperatura[indice][0] == temp_min:
            print(f"- Día {indice + 1}")
    temp_a_buscar = int(input("\nIngrese una temperatura para buscar días con esa máxima: "))
    print(f"Días con temperatura máxima de {temp_a_buscar}°C:")
    for indice in range(cant_dias):
        if temperatura[indice][1] == temp_a_buscar:
            print(f"- Día {indice + 1}")
            existe_temperatura = True
    if not existe_temperatura:
        print("No existe ningún día con esa temperatura máxima.")

GestionTemperaturas()