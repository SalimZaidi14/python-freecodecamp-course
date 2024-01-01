#You can access the number of characters in a string with the
#built-in len() function.
text = "Hello World"
print(len(text))

#Another useful built-in function is type(), which returns
#the data type of a variable.

print(type(text))

num = 8000
print(type(num))

#find() returns the index of the matching character inside 
# the string. If the character is not found, it returns -1.

#You can transform a string into its lowercase equivalent 
# with the lower() function.

text = "Hello World"
print(text.lower())

text = 'Hello World'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0])
print(index)