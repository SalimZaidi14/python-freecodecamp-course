# Now you should see the output again. Although this approach
#  works, it doesn't significantly enhance the code's
#  reusability. Repeatedly calling your function will result 
# in the same outcome. However, functions can be declared with 
# parameters to introduce versatility and customization:

# def function_name(param_1, param_2):
#     <code>

# Parameters are variables that you can use inside your 
# function. A function can be declared with different number 
# of parameters. In the example above, param_1 and param_2 are
#  parameters.

#therefore add message and offset referring to text and shift

text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(text, shift)
caesar(text, 13)