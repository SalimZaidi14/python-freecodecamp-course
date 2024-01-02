# At the moment, your function prints some strings, but these 
# values cannot be used by other parts of code to perform any
#  actions. For that purpose, you need to use a return statement.
#  You need to write return followed by the value that the 
# function should return. Once the return statement is found,
#  that value is returned and the execution of the function 
# stops, proceeding to the next line of code after the
#  function call.

text = 'Salim Zaidi'
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

    return encrypted_text

encryption = vigenere(text, custom_key)
print(encryption)