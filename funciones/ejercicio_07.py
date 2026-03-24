# Función que verifica el login y cuenta intentos fallidos
# Recibe nombre, contraseña y una lista para llevar la cuenta de intentos (por referencia)
def login(nombre, contrasena, intentos):
    es_login_correcto = False
    if nombre == "usuario1" and contrasena == "asdasd":
        es_login_correcto = True
    else:
        
        intentos[0] += 1
    return es_login_correcto

if __name__ == "_main_":
    intentos_fallidos = [0]
    MAX_INTENTOS = 3  
    
    while intentos_fallidos[0] < MAX_INTENTOS:
        usuario = input("Introduce el nombre de usuario: ")
        clave = input("Introduce la contraseña: ")
        login_exitoso = login(usuario, clave, intentos_fallidos)
        if login_exitoso:
            print("¡Login exitoso! Bienvenido al sistema.")
            break
        else:
            intentos_restantes = MAX_INTENTOS - intentos_fallidos[0]
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")
    
    if intentos_fallidos[0] >= MAX_INTENTOS:
        print("Se han agotado todos los intentos. Acceso denegado.")