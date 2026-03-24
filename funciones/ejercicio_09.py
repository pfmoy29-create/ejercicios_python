
def calcular_mcd(num1, num2): 
    resto = 0
    if num1 < num2:
        num1, num2 = num2, num1
    resto = num1 % num2
    if resto == 0:
        mcd = num2
    else:
        mcd = calcular_mcd(num2, resto)
    return mcd
def proceso_mcd_euclides():
    numero1, numero2 = 0, 0
    print("Número 1:", end=" ")
    numero1 = int(input())
    print("Número 2:", end=" ")
    numero2 = int(input())
    print("MCD:", calcular_mcd(numero1, numero2))
    
proceso_mcd_euclides()