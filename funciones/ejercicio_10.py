
def Convertir_A_Segundos(hor, min, seg):
    total_segundos = (hor * 3600) + (min * 60) + seg
    return total_segundos
def Convertir_A_HMS(segund, hor, min, seg):
    seg = segund % 60
    total_minutos = segund // 60
    min = total_minutos % 60
    hor = total_minutos // 60
    return hor, min, seg

def ConvertirHoras():
    hor, min, seg = 0, 0, 0
    opcion = 0
    while opcion != 3:
        print("1.- Convertir a segundos")
        print("2.- Convertir a horas, minutos y segundos")
        print("3.- Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            hor = int(input("Horas: "))
            min = int(input("Minutos: "))
            seg = int(input("Segundos: "))
            print(f"Corresponde a {Convertir_A_Segundos(hor, min, seg)} segundos.")
        elif opcion == 2:
            segund = int(input("Segundos: "))
            hor, min, seg = Convertir_A_HMS(segund, hor, min, seg)
            print(f"Corresponde a {hor}:\"{min}\":\"{seg}\"")
        else:
            print("Opción incorrecta")

ConvertirHoras()