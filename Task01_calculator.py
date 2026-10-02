# Task1:
# Write a calculator program which should return addition, substraction, multiplication, division, floor division, reminder.
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("Addition:", number1 + number2)
print("Subtraction:", number1 - number2)
print("Multiplication:", number1 * number2)

if number2 != 0:
    print("Division:", number1 / number2)
    print("Floor division:", number1 // number2)
    print("Remainder:", number1 % number2)
else:
    print("Division, floor division, and remainder are not possible with zero.")