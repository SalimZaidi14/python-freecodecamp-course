# Some words are reserved keywords (e.g. for, while, True). 
#They have a special meaning in Python, so you cannot use 
#them for variable names.

# Variable names cannot start with a number, and they can 
#only contain alpha-numeric characters or underscores.

# Variable names are case sensitive, i.e. my_var is 
#different to my_Var and MY_VAR.

# Finally, it is a common convention to write variable 
#names using snake_case, where each space is replaced by an 
#underscore character and the words are written in lowercase
# letters.

my_string = "Hello"

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in text:
    index = alphabet.find(text[i].lower())
    shifted = alphabet.find(index + shift)
    print(shifted)
