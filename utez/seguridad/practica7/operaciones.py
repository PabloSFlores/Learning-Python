'''Crear un modulo que contenga la función factorial y la función tabla de multiplicar. A partir de un programa mostrará el menú de las dos operaciones al usuario y realizará el cálculo respectivo. Tanto el valor del número a calcular su factorial o su tabla de multiplicar debe ser introducido por teclado.'''

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

def tabla_multiplicar(num):
    for i in range(1, 11, 1):
        print(f'{num} x {i} = {int(num * i)}')