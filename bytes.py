def caracter_byte(caracter):
    return format(ord(caracter), '08b')

def letra_byte(letra):
    return ' '.join(format(ord(caracter), '08b') for caracter in letra)

def menu():
    while True:
        print("Seleccione una opción:")
        print("1. Generar representación en byte de un carácter")
        print("2. Generar representación en byte de una palabra")
        print("4. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == '1':
            caracter = input("Ingrese un carácter: ")
            print(f"Representación en byte: {caracter_byte(caracter)}")
        elif opcion == '2':
            letra = input("Ingrese una palabra: ")
            print(f"Representación en byte: {letra_byte(letra)}")
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
