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

with open('../data/Message_01.txt', 'r') as file:
    message = file.read()

result = decode_message(message=message)

print(result)
