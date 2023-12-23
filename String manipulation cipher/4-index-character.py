#Each string character can be referenced by a numerical index. The index count
# starts at zero. So the first character of a string has an index of 0. 
#For example, in the string "Hello World", "H" is at index 0, "e" is at index 1,
# and so on. Each character of a string can be accessed by using bracket notation:

my_string = 'Hello World'
r = my_string[8]

# You can also access string characters starting from the end of the string. 
# The last character has an index of -1, the second to last -2 and so on. Now
#  modify your existing print() call to print the last character in your string.

text = "Hello World"
print(text[-1])