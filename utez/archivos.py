"""
Opciones para los Archivos:
- x -> Crear si no existe, de lo contrario devuelve un error
- w -> Crea el archivo si no existe, si ya existe, sobreecribe su contenido. 
- a -> Crea el archivo si no existe, si ya existe, añade el nuevo texto a su contenido. 

Escritura y lectura
- r -> Abre el archivo solo en modo de lectura
- r+ -> Abre el archivo en modo de lectura y escritura 
- w -> Abre el archivo en modo de escritura (reescribe contenido existente)
- w+ -> Abre el archivo en modo de escritura y lectura
- a -> Abre el archivo en modo de escritura (añade contenido al existente)
- a+ -> Abre el archivo en modo de escritura y lectura (añade contenido al existente)
"""

"""
También se puede usar la siguiente forma:
with open ('path/fileName.txt', 'mode') as variable_name:
    operaciones
"""
# Librería para eliminar archivos
from os import remove

print("- - APRENDIENDO - -")
# -> Crear archivo con: x
print("Creación de archivo con x:")
file = open("utils/example_x.txt", "x")
file.write("Archivo creado con el modo x.\n")
file.writelines(
    [
        "Este archivo fue creado con el modo x\n",
        "Este modo permite crear archivos\n",
        "En caso de que ya exista marca un error.\n",
    ]
)
print(file)
file.close()

print("Creación de archivo con w:")
# -> Lectura con r
file = open("utils/example_x.txt", "r")
# Función seek -> Posiciona el buffer hacia el byte indicado (0 es el inicio)
# Función read -> Lee todo el contenido línea por línea
# Función readline -> Lee una línea (parametro es el índice del último caracter a leer de la línea)
# Función readlines -> Lee todo el contenido en formato de lista de strings
print(file.read())
file.seek(0)
print(file.readline(10))
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

# Crear un archivo con w
file = open("utils/example_w.txt", "w")
file.write("Archivo creado con el modo w.\n")
# El argumento de writelines puede ser una variable declarada como una lista
text_lines = [
    "Este archivo fue creado con el modo w\n",
    "Este modo permite crear archivos\n",
    "En caso de que ya exista, sobreescribe el contenido.\n",
]
file.writelines(text_lines)
print(file)
file.close()

# -> Lectura con r
file = open("utils/example_w.txt", "r")
print(file.read())
file.seek(0)
print(file.readline(10))
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

# Caso practico
print("\n")
print("- - EJERCICIO - -")
# Crear archivo
# -> Uso de modo x para crear una sola vez
with open("utils/file.txt", "x") as file:
    print("Created file: ", file)

# Escribir algo
# -> Uso de modo w para escribir
with open("utils/file.txt", "w") as file:
    file.write("Lista de compras:\n")

# Leer lo escrito
# -> Uso de modo r para leer
with open("utils/file.txt", "r") as file:
    print(file.read())

# Escribir algo nuevo y leer para notar que fue reemplazado
# -> Uso de modo w+ para escribir y leer
with open("utils/file.txt", "w+") as file:
    file.write("Lista de pendientes:\n")
    # -> Uso de seek() para mover el punto al inicio
    file.seek(0)
    print(file.read())

# Añadir en lugar de sobreescribir
# -> Uso de a(append) para añadir
with open("utils/file.txt", "a") as file:
    file.write("- Hacer la tarea\n")

with open("utils/file.txt", "r") as file:
    print(file.read())

# Añadir y leer
# -> Uso de a+ para añadir y leer
# -> r+ es lo mismo
with open("utils/file.txt", "a+") as file:
    file.write("- Hacer la comida\n")
    file.write("- Lavar ropa\n")
    file.write("- Alimentar a mi mascota\n")
    file.seek(0)
    print(file.read())

# Leer
# -> uso de r para leer
with open("utils/file.txt", "r") as file:
    # Alternativa de impresión
    for line in file:
        print(line)

with open("utils/file.txt", "w+") as file:
    print("Realizando tareas...")
    # Sobreescribir
    file.write("TAREAS TERMINADAS")

    # Impresión final
    file.seek(0)
    print("Resultado: ", file.read())

# Eliminación de archivos
remove("utils/file.txt")
remove("utils/example_x.txt")
remove("utils/example_w.txt")
