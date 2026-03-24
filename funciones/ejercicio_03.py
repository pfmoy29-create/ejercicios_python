# Función calcularTemperaturaMedia: Recibe dos números reales que representan 
# dos temperaturas y devuelve la temperatura media.
# Parámetros de entrada: dos temperaturas (real)
# Dato devuelto: La temperatura media (real)

def tmedia (temp1,temp2):
    return(temp1 + temp2) / 2

print("cuantas temperaturas vas a calcular?:")
cantidad = int(input())
for indice in range (cantidad):
    print("Introduce temperatura minima:")
    tmin = float(input())
    print("Introduce temperatura maxima:")
    tmax = float(input())
    print("Temperatura media :", tmedia(tmin,tmax))