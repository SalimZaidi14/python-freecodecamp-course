# The .index() method is identical to the .find() method but 
# it throws a ValueError exception if it is unable to find the
#  substring.

text = 'Hello Zaira'
custom_key = "python"

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        #append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            #find the right key character to encode
            key_char = key[key_index % len(key)]
            #you will need to increment key_index after each 
            #iteration
            key_index += 1
            #define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    print('plain text:', message)
    print('encrypted text:', encrypted_text)

