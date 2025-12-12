def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_continue = True
    num1 = float(input("Please enter the first number: "))

    while should_continue:
        for operation in operations:
            print(operation)
        symbol = input("Please select an operation: ")
        num2 = float(input("Please enter the second number: "))
        answer = operations[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        decision = input(f"Please enter 'y' to continue making calculations with {answer} or enter 'n' to start a new calculation: ")

        if decision == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()
