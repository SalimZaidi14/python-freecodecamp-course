#strings are immutable that is cannot be changed once they
#are created

text = "Hello World"

#If you try to change the individual characters of a 
#string, you will get a TypeError. However, a variable
# can be reassigned another string:

text = "Hello World"
text = "Albatross"

#Now you need to create a new_char variable at the end 
# of your loop body. Set its value to alphabet[new_index].

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift
    new_char = alphabet[new_index]
    print(new_char)

#final-
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    new_char = alphabet[new_index]
    print('char:', char, 'new char:', new_char)