 # Realizar un algoritmos que lea un número y que muestre su raíz cuadrada 
# y su raíz cúbica.
# PSeInt no tiene ninguna función predefinida que permita calcular la raíz cúbica,
# ¿cómo se puede calcular?

num = int(input("Dime el numero :"))

raiz_cuadrada = num ** 0.5
raiz_cubica = num ** (1/3)

print("raiz_cuadrada :" , raiz_cuadrada)
print("raiz_cubica :" , raiz_cubica)