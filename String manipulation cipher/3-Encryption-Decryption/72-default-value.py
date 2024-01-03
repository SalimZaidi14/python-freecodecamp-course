# Functions can be called with default arguments. A default argument
#  indicates the value that the function should take if the
#  argument is not passed. For example, the function below accepts 
# three arguments but you can call it passing two arguments. 
# The third one will assume the specified value by default:

# def foo(a, b, c=value):
#     <code>

# The .isalpha() method returns True if all the character of the 
# string on which it is called are letters. For example, the code 
# below returns True:

text = "Salim Salim Salim Salim Salim Salim Salim"
custom_key = "python"

def vigenere(message, key, direction=1):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ""
    key_index = 0

    for char in message.lower():
        #append space to the message
        if char.isalpha() == " ":
            final_message += char
        else:
            #find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            index = alphabet.find(char)
            #define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

encryption = vigenere(text, custom_key)
print(encryption)
decryption = vigenere(encryption, custom_key, -1)
print(decryption)