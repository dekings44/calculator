



#Calculator


# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


signs = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': subtract
    }

num1 = int(input('What is the first number?\n'))


for symbol in signs:
    print(symbol)

sign_symbol = input('Please pick a sign from the above\n')

num2 = int(input('What is the second number?\n'))
calculation_function = signs[sign_symbol]
answer = calculation_function(num1, num2)

print(f'{num1} {sign_symbol} {num2} = {answer}')

sign_symbol = input('Please pick a sign from the above\n')

num3 = int(input('What is the next number?\n'))
calculation_function = signs[sign_symbol]
answer2 = calculation_function(calculation_function(num1, num2), num3)

print(f'{answer} {sign_symbol} {num3} = {answer2}')