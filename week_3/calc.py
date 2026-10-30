# A simple arithmetic calculator

def add(x, y):
    # return to 2 decimal places

    return round(x + y, 2)

def subtract(x, y):
    return round(x - y, 2)

def multiply(x, y):
    return round(x * y, 2)

def divide(x, y):
    if y == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return round(x / y, 2)


operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(f"{x} + {y} = {add(x, y)}")
elif operator == "-":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(f"{x} - {y} = {subtract(x, y)}")
elif operator == "*":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(f"{x} * {y} = {multiply(x, y)}")
elif operator == "/":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(f"{x} / {y} = {divide(x, y)}")
else:
    print("Invalid operator. Please enter one of the following: +, -, *, /")