# A function is essentially a reusable block of code. You 
# have already met some built-in functions, like print(),
#  find() and len(). But you can also define custom functions
#  like this:

# def function_name():
#     <code>

# A function declaration starts with the def keyword followed 
# by the function name — a valid variable name — and a pair of
#  parentheses. The declaration ends with a colon.

text = "Hello World"
shift = 3

def caesar():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""
    for char in text.lower():
        if char == " ":
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = index + shift % len(alphabet)
            encrypted_text += alphabet[new_index]

    print("plain text:", text)
    print("encrypted_text:", encrypted_text)

caesar()


