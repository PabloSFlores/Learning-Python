'''- - - - - - - - - - - - - - - - - - - - - - -'''
'''CONDICIONALES'''
# Ejemplo 1
nativeVLAN = 1
dataVLAN = 100
if nativeVLAN == dataVLAN:
    print('The netive VLAN and the data VLAN are the same')
else:
    print('This native VLAN and the data VLAN are different')

# Ejemplo 2
if 'la' in 'hola':
    print('Está')

# Ejemplo 3
nativeVLAN = 100
dataVLAN = 100
if nativeVLAN == dataVLAN or dataVLAN < 100:
    print('Éxito XD')
else:
    print('Falla :()')

# Ejemplo 4
aclNum = int(input('What is the IPv4 ACL number?'))
if aclNum >= 1 and aclNum <= 99:
    print('This is a standard IPv4 ACL.')
elif aclNum >= 100 and aclNum <= 199:
    print('This is a extended IPv4 ACL.')
else:
    print('This is not a standard or extended Ipv4 ACL.')
