# Calculator

import art
import os

logo = art.logo

def clear():
    _ = os.system("cls")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)

    num1 = float(input("Enter first number: "))

    for operation in operations:
        print(operation)
    active = True

    while active:
        symbol = input("Pick an operation: ")
        num2 = float(input("Enter another number: "))
        calc_func = operations[symbol]

        result = calc_func(num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            num1 = result
        else:
            active = False
            clear()
            calculator()

calculator()
