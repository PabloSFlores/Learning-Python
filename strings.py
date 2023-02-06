string = 'hola je'
# conocer los métodos de una variable
# print(dir(string))
print(string.upper())
print(string.lower())
print(string.swapcase())
print(string.capitalize())
print(string.casefold())
print((string.replace('je', 'Vane')).capitalize())
print(string.split())
print(string.find('e'))
print(string.index('e'))
print(string[5])
print(len(string))

#Concatenaión
name = 'Pablo'

print('Mi nombre es ' + name)
print(f'Mi nombre es {name}')
print('Mi nombre es {0}'.format(name))