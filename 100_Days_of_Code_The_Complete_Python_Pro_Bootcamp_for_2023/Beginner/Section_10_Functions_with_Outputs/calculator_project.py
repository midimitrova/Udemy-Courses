def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculator():
    num1 = float(input('What is the first number?: '))
    for symbol, func in operations.items():
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What is the next number?: '))
        if operation_symbol == '/' and num2 == 0:
            print('You can not divide by 0!')
            continue
        else:
            calculation_function = operations[operation_symbol]
            first_result = calculation_function(num1, num2)
            print(f'{num1} {operation_symbol} {num2} = {first_result:.2f}')

        user_choice = input(f"Type 'y' to continue calculating with {first_result:.2f} "
                            f"or type 'n' to start new calculation.: ").strip().lower()
        if user_choice == 'y':
            num1 = first_result
        else:
            should_continue = False
            calculator()


calculator()
