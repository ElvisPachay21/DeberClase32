# Definir el diccionario para almacenar los valores por usuario
usuarios = {}

# Definir datos de prueba
usuarios["Gustavo"] = 400.00
usuarios["Carlos"] = 200.00

def registrar_usuarios():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        print("El usuario ya está registrado")
    else:
        usuarios[nombre] = 0.00
        print(f"Usuario {nombre} agregado correctamente")

def depositar():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        monto = float(input("Introduce el monto a depositar: "))
        usuarios[nombre] += monto
        print(f"Se han depositado {monto} a la cuenta de {nombre}.")
    else:
        print(f"Usuario {nombre} no existe")

def retirar():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        retiro = float(input("Introduce el monto a retirar: "))
        if retiro > usuarios[nombre]:
            print(f"Fondos insuficientes. El saldo actual es {usuarios[nombre]}.")
        else:
            usuarios[nombre] -= retiro
            print(f"Se han retirado {retiro} de la cuenta de {nombre}.")
    else:
        print("Usuario no existente en el registro")

def consultar_saldo():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        print(f"El saldo actual de {nombre} es {usuarios[nombre]}.")
    else:
        print(f"Usuario {nombre} no existe")

def menu():
    while True:
        print("Menú Principal")
        print("1. Registrar usuario")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Consultar saldo")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            registrar_usuarios()
        elif opcion == '2':
            depositar()
        elif opcion == '3':
            retirar()
        elif opcion == '4':
            consultar_saldo()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")


menu()
