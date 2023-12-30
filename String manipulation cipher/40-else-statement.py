# A conditional statement can also have an else clause. 
# This clause can be added to the end of an if statement
# to execute alternative code if the condition is false:

# if condition:
#     <code>
# else:
#     <code>
# As you can see in your output, when the loop iterations 
# reach the space, a space is added to the encrypted
#  string. Then the code outside the if block executes and
#  a c is added to the encrypted string.

# To fix it, add an else clause after encrypted_text += char
#  and indent all the subsequent lines of code.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char #1
    else:
        index = alphabet.find(char)
        new_index = index + shift
        encrypted_text += alphabet[new_index]
        print('char:', char, 'encrypted text:', encrypted_text)

#so as soon as the hello word prints out the the if statement
#finds a space and then add the empty space char then loops 
#again to find the word world.
 
#1 = space

