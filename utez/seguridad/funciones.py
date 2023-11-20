'''
¿Qué son las funciones?
'''
# Ejemplo 1
def my_function():
    print('Inside my_function()')
    x = range(5, 50, 2)
    for n in x:
        print(n, end='-')

print('Out of the function')
my_function()
print('\nOther Operations')
my_function()
print('\nEnd of the program')


# Ejemplo 2
def my_function_B(colors):
    for x in colors:
        print(x)

my_colors = ['Blue', 'Red', 'Green', 'Yellow']
my_function_B(my_colors)

# Ejemplo 3
def my_function2(fname):
    print(fname + ' Student')

my_function2('Luis')
my_function2('Gina')
my_function2('Carlos')
my_function2('Diana')

# Ejemplo 4
def my_function3(fname, quarter):
    if quarter > 6:
        print(fname + ' is going to be an engineer')
    else:
        print(fname + ' is going to be an technician')

my_function3('Luis',4)
my_function3('Gina',8)
my_function3('Carlos',10)
my_function3('Diana',3)

# Ejemplo 5
# Los argumentos se pueden enviar como clave = valor, de esta forma no importa el orden de los argumentos
def my_function4(student1, student2, student3):
    print('The youngest child is ' + student3)

my_function4(student3 = 'Gaby', student2 = 'Alberto', student1 = 'Angel')

# Ejemplo 6
# Uso de valores por defecto en los argumentos de las funciones
def my_function5(language = 'Python'):
    print('I am programming in ' + language)

my_function5('Java')
my_function5()
my_function5('C')
my_function5()
my_function5('Ruby')

# Ejemplo 7
def my_function6(x = 1):
    return 5 * x

variable1 = my_function6(3)
variable2 = my_function6(7)
print(variable1, variable2, my_function6(9))