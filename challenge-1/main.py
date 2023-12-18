def decode_message(message):
    words = message.lower().split()
    
    word_count = {}
    result = []

    for word in words:
        word_key = word.lower()

        if word_key not in word_count:
            word_count[word_key] = 1
        else:
            word_count[word_key] += 1

    for word in words:
        word_key = word.lower()
        if word_key in word_count:
            result.append(word_key + str(word_count[word_key]))
            del word_count[word_key]

    decoded_message = ''.join(result)
    
    return decoded_message

import sys

if len(sys.argv) != 2:
    print("Uso: python script.py <ruta_del_archivo>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, 'r') as file:
        message = file.read()
except FileNotFoundError:
    print("El archivo no se encontró en la ruta especificada.")
    sys.exit(1)

result = decode_message(message)

print(result)
