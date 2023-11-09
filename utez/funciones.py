print('- - EJERCICIO - -')
# Funciones sin parámetros
def funcion():
    return 'Función sin parámetros'

# Funcinoes sin retorno
def funcion_sin_retorno():
    print('Función sin parámetros y sin retorno')

# Función de valores obligatorios
# - Suma dos valores
def suma(a, b):
    return a + b

# Función con valores opcionales
# - Repite la palabra 2 veces por defecto
def repetir_palabra(palabra, veces=2):
    print(palabra * veces)

s = suma
print(funcion())
funcion_sin_retorno()
print(suma(2,4))
print(s(2,b=4))
# error -> print(s(b=4,2))
print(repetir_palabra('Hola'))
print(repetir_palabra('Hola',5))

class Mascota():
    i = 0
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        Mascota.i += 1
    
    # Método de instancia
    def dormir(self):
        print('zzZ')
    
    # Método de clase
    @classmethod
    def veterinaria(cls):
        print(f'Hay {cls.i} mascotas en la veterinaria')
    
    # Métodos estáticos
    @staticmethod
    def es_cachorro(edad):
        return edad < 2

m1 = Mascota('Michi','Gato',12)

print(m1.dormir())
print(Mascota.veterinaria())
print(Mascota.es_cachorro(m1.edad))