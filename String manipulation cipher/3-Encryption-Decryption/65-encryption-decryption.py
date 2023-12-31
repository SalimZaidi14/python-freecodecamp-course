# Encryption and decryption are opposite processes and 
# your function can do both with a couple of tweaks.

text = "Salim Salim Salim Salim Salim Salim Salim"
custom_key = "python"

def vigenere(message, key, direction):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ""
    key_index = 0

    for char in message.lower():
        #append space to the message
        if char == " ":
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

encryption = vigenere(text, custom_key, 1)
print(encryption)
decryption = vigenere(encryption, custom_key, -1)
print(decryption)

#How the decryption works-
#when we multiply -1 to offset, we mean negative value of
#offset.

#first char of text = S
#first char of key = p

#S + p = h (from hyepa)
#S + p = 33
#33%26 = 7 (index of h) hence hyepa
#S = h - p (p is offset so negative value of p
#hence we get Salim Zaidi

#ALSO-
#encryption = final message
