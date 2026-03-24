# Programa para calcular la nota media, máxima y mínima de 5 calificaciones.


notas = [0] * 10 
tam_notas = 5     
indice = 0        
nota_media = 0.0  
suma = 0.0        
nota_max = 0     
nota_min = 10     

for indice in range(0, tam_notas):

    print(f"Ingrese la calificación {indice + 1} (entre 0 y 10): ", end="")
    while True:
        nota_actual = int(input())
        if 0 <= nota_actual <= 10:
            notas[indice] = nota_actual
            suma += nota_actual  
            
            if nota_actual > nota_max:
                nota_max = nota_actual
           
            if nota_actual < nota_min:
                nota_min = nota_actual
            break  
        else:
            print("Error: La calificación debe estar entre 0 y 10. Intente de nuevo: ", end="")
nota_media = suma / tam_notas
print("\n--- Resultados ---")
print("Calificaciones ingresadas:")
for indice in range(0, tam_notas):
    print(f"Calificación {indice + 1}: {notas[indice]}")

print(f"\nNota media: {nota_media}")
print(f"Nota máxima: {nota_max}")
print(f"Nota mínima: {nota_min}")