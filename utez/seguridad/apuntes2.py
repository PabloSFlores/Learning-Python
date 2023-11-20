print('-- Parte de hostnames')
hostnames = ["R1", "R2", "R4", "R5"]
print(type(hostnames))

print(len(hostnames))
print(hostnames)

print('-- Parte de lista')
# Imprimir índices de la lista
lista = [1, 2.5, 'cadena', [5, 6], 4]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[3][0])
print(lista[3][1])
print(lista[1:3])
print(lista[1:6])

print('-- Parte de lista | for')
# Iterar elementos de la lista
for el in lista:
    print(el)

print('-- Parte de lista | append')
# Agrega un elemento al final de la lista
lista.append(10)
print(lista)
lista.append([2, 5])
print(lista)

print('-- Parte de lista | extend')
# Permite agregar una lista pero de manera individual, es decir, por elemento
lista.extend([88, 89])
print(lista)

print('-- Parte de lista | insert')
lista.insert(2, "Z")
print(lista)
