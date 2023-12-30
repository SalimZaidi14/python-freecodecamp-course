# Currently, spaces get encrypted as c. To maintain the 
# original spacing in the plain message, you'll require a 
# conditional if statement. This is composed of the if 
# keyword, a condition, and a colon :.

# if <condition>:
#     <code>

# At the top of your for loop, replace print(char == ' ') 
# with an if statement. The condition of this if statement 
# should evaluate to True if char is an empty space and 
# False otherwise. Inside the if body, print the string 
# space!. Remember to indent this line.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        print("space!")
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)

# Now, instead of printing space!, use the addition
# assignment operator to add the space to the current value 
# of encrypted_text.
    
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)