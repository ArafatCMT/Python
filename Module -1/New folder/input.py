# write a program add two numbers
number1 = input("Enter the first number : ")
number2 = input("Enter the second number: ")
# print(type(number1))
#by default the input from user will be string type

# typecasting
number1 = int(number1)
number2 = int(number2)


# print(type(number2))
sum = number1 + number2
print("The sum of two numbers : ", sum)

# a,b = input().split() # single line input with separate by space
# print(a,b)