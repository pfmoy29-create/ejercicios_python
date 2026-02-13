# Este programa determina la posición relativa de dos circunferencias
# basándose en las coordenadas de sus centros y sus radios.

x1 = float(input("Dime coordenada x primera circunferencia: "))
y1 = float(input("Dime coordenada y primera circunferencia: "))
r1 = float(input("Dime radio primera circunferencia: "))

x2 = float(input("Dime coordenada x segunda circunferencia: "))
y2 = float(input("Dime coordenada y segunda circunferencia: "))
r2 = float(input("Dime radio segunda circunferencia: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if distancia > (r1 + r2):
        print("Circunferencias exteriores")
    if distancia == (r1 + r2):
        print("Circunferencias tangentes exteriores")
    if distancia < (r1 + r2) and distancia > abs(r1 - r2):
        print("Circunferencias secantes")
    if distancia == abs(r1 - r2):
        print("Circunferencias tangentes interiores")
    if distancia > 0 and distancia < abs(r1 - r2):
        print("Circunferencias interiores")
    if distancia == 0:
        print("Circunferencias concéntricas")
