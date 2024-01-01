# Currently, every single letter is always encrypted with the
#  same letter, depending on the specified offset. What if the 
# offset were different for each letter? That would be much 
# more difficult to decrypt. This algorithm is referred to as
#  the Vigenère cipher, where the offset for each letter is
#  determined by another text, called the key.

# Start transforming your Caesar cipher into a Vigenère cipher
#  by removing the two function calls.

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
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    print('plain text:', message)
    print('encrypted text:', encrypted_text)

