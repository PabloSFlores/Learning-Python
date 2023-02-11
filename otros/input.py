o = 1
while o != 0:
    print('-- Calculadora --')
    a = float(input("Ingresa el primer valor -> "))
    b = float(input('Ingresa el segundo valor -> '))
    print('-- Operaciones --')
    print('1.- Suma\n2.- Resta\n3.- Multiplicación\n4.- División\n5.- Potencia')
    opc = int(input('Selecciona una opción -> '))

    print('-- Resultado --')
    match opc:
        case 1:
            print(f'{a} + {b} = {a + b}')
        case 2:
            print(f'{a} - {b} = {a - b}')
        case 3:
            print(f'{a} x {b} = {a * b}')
        case 4:
            print(f'{a} / {b} = {a / b}')
        case 5: 
            print(f'{a} ^ {b} = {a ** b}')
        case _:
            print('Sin coincidencia')
    o = int(input('''¿Continuar?\n1.- Si\n0.- No\n-> '''))
