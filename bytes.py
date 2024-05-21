def caracter_byte(caracter):
    return format(ord(caracter), '08b')

def ascii_byte(byte):
    caracter = chr(int(byte, 2))
    return f'{caracter}-{ord(caracter)}'

def letra_byte(letra):
    return ' '.join(format(ord(caracter), '08b') for caracter in letra)

def menu():
    while True:
        print("Seleccione una opción:")
        print("1. Generar representación en byte de un carácter")
        print("2. Generar representación en byte de una palabra")
        print("3. Generar representación ASCII de un byte")
        print("4. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == '1':
            caracter = input("Ingrese un carácter: ")
            print(f"Representación en byte: {caracter_byte(caracter)}")
        elif opcion == '2':
            letra = input("Ingrese una palabra: ")
            print(f"Representación en byte: {letra_byte(letra)}")
        elif opcion == '3':
            byte = input("Ingrese un byte en formato binario: ")
            print(f"Representación ASCII: {ascii_byte(byte)}")
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
