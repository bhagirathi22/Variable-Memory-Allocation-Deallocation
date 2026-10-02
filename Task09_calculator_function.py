# Task9:
# Create calculate(a,operator,b)
# The function should support (+,-,*,/,//,% and **)
# handle invalid operators and division by zero.

def calculate(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/" and b != 0:
        return a / b
    elif operator == "//" and b != 0:
        return a // b
    elif operator == "%" and b != 0:
        return a % b
    elif operator == "**":
        return a ** b
    elif operator in ("/", "//", "%") and b == 0:
        return "Cannot divide by zero."
    else:
        return "Invalid operator."


number1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /, //, %, **): ")
number2 = float(input("Enter the second number: "))

print(calculate(number1, operator, number2))