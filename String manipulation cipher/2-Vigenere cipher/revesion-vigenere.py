text = "Salim Salim"
custom_key = "python"

def vigenere(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""
    key_index = 0

    for char in message.lower():
        if char == " ":
            encrypted_text += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            index = alphabet.find(char)
            offset = alphabet.index(key_char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text

encryption = vigenere(text, custom_key)
print(encryption)