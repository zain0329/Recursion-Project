# Recursive Power Method Program by Zain Malik
#create variables
x = 0
y = 2
#create function
# the following function calls itself if x + y = 0 and raises a number to a power otherwise
def exponentBIG(x,y):
    if x + y == 0:
        return exponentBIG(x,y)
    else:
        print("Welcome to the Recursive Power Method Program")
        x = float(input("Enter a number: "))
        y = float(input("Enter another number that the first number will be raised to the power of: "))
        exponent = x ** y
        print('Your answer is ', exponent)
# call function
exponentBIG(x,y)
