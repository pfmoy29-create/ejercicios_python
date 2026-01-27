# Calcular el perímetro y área de un rectángulo dada su base y su altura.






print("Calculo de Area y Perimetro de un rectangulo")
base = input ('Ingresa la base')
base = int(base)

height = input('Ingresa la altura:')
height = int(height)

area = base * height
perimeter = base + base + height + height

print("Area:", area)
print("Perimetro:", perimeter)