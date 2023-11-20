# Defición de alfabetos
letters_lower = "abcdefghijklmnñopqrstuvwxyz"
letters_upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Función para cifrar
def encode(word, level):
    encoded_word = ""
    # Iterar la palabra letra por letra
    for letter in word:
        # Asignar alfabeto según la letra
        letters = letters_lower if letter in letters_lower else letters_upper
        # Calcular el índice de la letra a sustituir
        index = (letters.find(letter) + level) % len(letters)
        # Concatenar nuevo texto
        # Si la letra existe en el alfabeto elegido se asigna la nueva, si no, se mantiene
        encoded_word += letters[index] if letter in letters else letter
    # Retornar palabra generada
    return encoded_word

# Función para descifrar 
# Realiza el cálculo invertido
def decode(word, level):
    decoded_word = ""
    for letter in word:
        letters = letters_lower if letter in letters_lower else letters_upper
        index = (letters.find(letter) - level) % len(letters)
        decoded_word += letters[index] if letter in letters else letter
    return decoded_word

# Interacción principal
while True:
    print("-- Cifrado César --")
    opt = int(input("Elije una opción:\n1.- Cifrar palabara\n2.- Descifrar palabra\n0.- Salir\nOpción: "))
    if opt == 0:
        break
    word = str(input("Ingresa la palabra: "))
    if opt == 1:
        level = int(input("Ingresa la clave de cifrado: "))
        print(f"La palabra cifrada es: {encode(word, level)}")
    elif opt == 2:
        level = int(input("Ingresa la clave de descifrado: "))
        print(f"La palabra descifrada es: {decode(word, level)}")
    else:
        print("Opción no válida")