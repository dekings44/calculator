from art import logo

print(logo)



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

def calculator():

    num1 = float(input('What is the first number?\n'))


    for symbol in signs:
        print(symbol)


    should_continue = True

    while should_continue:

        sign_symbol = input('Please pick a sign from the above\n')

        num2 = float(input('What is the second number?\n'))
        calculation_function = signs[sign_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {sign_symbol} {num2} = {answer}')

        if input(f"Type 'y' to continue calculating with {answer}: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()