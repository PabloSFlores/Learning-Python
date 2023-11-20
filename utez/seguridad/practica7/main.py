import operaciones
while True:
    print('- - Operaciones - -')
    print('1.- Factorial\n2.- Tabla de multiplicar\n3.- Salir')
    opt = int(input('Operación a realizar: '))
    num = int(input('Ingresa un número: '))
    if opt == 3:
        break
    if opt == 1:
        print(f'El resultado del factorial es: {operaciones.factorial(num)}')
    if opt == 2: 
        print(f'La tabla de multiplicar del número {num} es:')
        operaciones.tabla_multiplicar(num)