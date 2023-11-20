'''- - - - - - - - - - - - - - - - - - - - - - -'''
'''DICCIONARIOS'''
# Creación
ipAddress = {
    'R1': '10.1.1.1',
    'R2': '10.2.2.1',
    'R3': '10.3.3.1'
}
print(type(ipAddress))
# Impresión
print(ipAddress)
# Acceder a un valor por clave
print(ipAddress['R1'])
# Agregar o reemplazar
ipAddress['S1'] = '10.1.1.10'
print(ipAddress)
# Verificar existencia
print('R3' in ipAddress)

# Ejemplo 1
ipAddress2 = {
    'R1': '10.1.1.1',
    'R2': '10.2.2.1',
    'R3': '10.3.3.1'
}
ipAddress2['R3'] = ['10.3.3.1', '10.3.3.2', '10.3.3.3']
print(ipAddress2)

# Ejemplo 2
''' Forma de recorrer
for akey in diccionario:
    print(akey, ':', diccionario[akey])'''

diccionario = {
    'nombre': 'Carlos',
    'edad': '22',
    'cursos': ['Python', 'java', 'JavaScript']
}

print(diccionario['nombre'])  # Carlos
print(diccionario['edad'])  # 22
print(diccionario['cursos'])  # ['Python', 'java', 'JavaScript']
print(diccionario['cursos'][0])  # Python

'''Diccionarios => Métodos'''
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# keys() -> Devuelve un array de las claves
keys = diccionario.keys()
print(keys)  # dict_keys['a','b','c','d']

# values() -> Devuelve un array de los valores
values = diccionario.values()
print(values)  # dict_values[1,2,3,4]

# clear() -> Limpia el diccionario
diccionario.clear()
print(diccionario)  # {}

# get() -> Obtiene un valor por su clave
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(diccionario.get('b'))  # 2

# setDefault -> Funciona como un get() | Agrega un nuevo elemento al diccionario
# Primer forma de función
print(diccionario.setdefault('b'))  # 2
# Segunda forma de funcionar
diccionario.setdefault('e', 5)
print(diccionario)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# update() -> Si existe la clave, actualiza, si no, lo agrega
dicc1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dicc2 = {'c': 6, 'b': 7, 'e': 8, 'f': 12}
dicc1.update(dicc2)
print(dicc1)
