'''
Realizar un script en python, que desde teclado ingrese los
elementos de la lista septimoA, el usuario debe indicar la 
posición en la que se debe agregar su nombre
'''

# Definition
students = []
print('**- Alumnos -**')
while True:
    name = input('Ingresa el nombre completo > ')
    i = int(input('Ingresa el índice en el que lo deseas agregar > '))
    students.insert(i, name)

    print('Lista de estudiantes: ')
    for student in students:
        print(f'- {student}')

    opt = int(input('\n¿Salir?\n1.-Si\n2.-No\n> '))
    if (opt == 1):
        break

'''
Innvestigar los siguientes métodos:
- count()
- remove()
- index()
- copy()
- reverse()
- sort()
- max()
- min()
'''
