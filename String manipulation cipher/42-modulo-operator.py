# When the loop reaches the letter Z, the sum index + shift
#  exceeds the length of the string alphabet.

# In this case, the modulo operator, %, can be used to
#  return the remainder of the division between two numbers.
#  For example: 5 % 2 is equal to 1, because 5 divided by 2 
# has a quotient of 2 and a remainder of 1.

# Surround index + shift with parentheses, and modulo the 
# expression with 26, which is the alphabet length.

text = "Hello World"
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz12345"
encrypted_text = ""

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift)%len(alphabet)
        encrypted_text += alphabet[new_index]
        print("char:", char, "encrypted text:", encrypted_text)