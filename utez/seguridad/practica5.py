# FOR
devices = ["R1", "R2", "R3", "S1", "S2"]
for item in devices:
    # end -> configuración de secuencia de escape del print
    print(item, end=":")

# Condiciones dentro del for
for item in devices:
    if 'R' in item:
        print(item)

# Crear una lista a partir de los elementos de otra lista
switches = []
for item in devices:
    if "S" in item:
        switches.append(item)

print(switches)  # ["S1", "S2"]

# FOR con range
# (Initial value, final value, steps)
x = range(500, 5, -5)
for n in x:
    print(n, end="-")

# WHILE
x = int(input('Enter a number to count to: '))  # x = int(x)
y = 1
while y <= x:
    print(y)
    y = y+1

# DO WHILE
x = int(input('Enter a number to count to: '))  # x = int(x)
y = 1
while True:
    print(y)
    y = y+1
    if y > x:
        break

# Doble ciclo WHILE
while True:
    x = input('Enter a number to count to: ')
    if x == 'q' or x == 'quit':
        break
    x = int(x)
    y = 1
    while True:
        print(y)
        y = y+1
        if y > x:
            break
