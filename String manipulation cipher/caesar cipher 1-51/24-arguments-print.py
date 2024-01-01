# An argument is an object or an expression passed to a 
# function — between the parentheses — when it is called. 
# The print function can take multiple arguments, separated 
# by a comma.

# Add a second argument to print(char) so that it prints
#  the character and its index inside the alphabet.

#find is returning -1 for upper case characters. lets add
#.lower() to text.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    print(char, index, new_index)