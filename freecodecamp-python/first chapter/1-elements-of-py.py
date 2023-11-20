x = 2 #assignment statement
#take a value 2 and stick into a location memory and we name it x
#python remembers that the value of x is 2
x = x + 2 #take the previous value of x and add 2 to it
print(x) #this x is now the new value

#conditonal statements 
x = 100
if x < 10: #there is a question that if x is less than 10 then do the indented step otherwise skip to the next if statemen
    print("smaller")
if x > 20:
    print("larger")

print("finish")

#repeated statements
n = 5
while n > 0:
    print(n)
    n = n - 1
#repeated until the condition satisfies
#while says "as long as n is greater than 0 keep doing the indented step"
print("finish")