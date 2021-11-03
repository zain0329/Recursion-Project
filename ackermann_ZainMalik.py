# Ackermann's function Program by Zain Malik
# create variables + print statements
print("Welcome to Ackermann's function")
m = float(input('Enter a value for m: '))
n = float(input('Enter a value for n: '))

# create function
def ackermann(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1,1)
    else:
        return ackermann(m - 1, ackermann(m,n - 1))
# call function
print(ackermann(m,n))
