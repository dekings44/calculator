



#Calculator


# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    n1 * n2


# Divide
def divide(n1, n2):
    n1 / n2


signs = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': subtract
    }

num1 = int(input('What is the first number?\n'))
num2 = int(input('What is the second number?\n'))

for symbol in signs:
    print(symbol)