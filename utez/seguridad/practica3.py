'''
Crear un programa en python que desde teclado
genere un diccionario llamado ingredientes(min 3)
y el costo de los mismos, e indique a que descuentos
soy acreedor bajo los siguientes criterios:
1. 15% -> Si el total de mis ingredientes > 100
2. 10% -> Si el total de mis ingredientes < 100 y > 50
3. 5%  -> Si el total de mis ingredientes < 50 y > 25 
4. 0%  -> Si el total de mis ingredientes < 25
'''
ingredientes = {}
descuento = 0
acumulado = 0
total = 0

while True:
    # Obtener valores
    ingrediente = str(input('Ingresa el ingrediente: '))
    costo = float(input(f'Ingresa el costo del {ingrediente}: $'))
    # Guardar valores
    ingredientes[ingrediente] = costo
    # Imprimir
    print(ingredientes)
    # Condición de salida
    if len(ingredientes.keys()) == 3:
        break
    else:
        print('Faltan ingredientes')

# Calcular acumulado
for ingrediente in ingredientes:
    acumulado += int(ingredientes[ingrediente])
# Calcular descuento
if acumulado >= 100:
    descuento = 15
elif acumulado < 100 and acumulado >= 50:
    descuento = 10
elif acumulado < 50 and acumulado > 25:
    descuento = 5
else:
    descuento = 0

# Calculo del total según el descuento
total = acumulado - (acumulado * (descuento / 100))

# Impresion de los resultados
print(f'Tu descuento es de {descuento}%')
print(f'Total a pagar: ${total}')
