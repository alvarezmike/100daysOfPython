# calculator
from art import logo

print(logo)


# add
def add(n1, n2):
    return n1 + n2


# substract
def substract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


# dictionary
operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide

}
should_continue = True
while should_continue:
    num1 = float(input("What is the first number? : "))
    num2 = float(input("What is the second number? : "))

    for operator in operation:
        print(operator)

    operation_symbol = input("Pick an operation from the line above: ")

    if operation_symbol == "+":
        answer = add(num1, num2)

    elif operation_symbol == "-":
        answer = substract(num1, num2)

    elif operation_symbol == "*":
        answer = multiply(num1, num2)

    elif operation_symbol == "/":
        answer = divide(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_question = input("Do you want to make another calculation. Type 'yes' or 'no': ")
    if continue_question == 'yes':
        should_continue = True
    elif continue_question == 'no':
        should_continue = False
        print("Program ended.")