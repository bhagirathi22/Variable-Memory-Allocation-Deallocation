# Task2:
# Create function that accepts an integer and determines 
# *whether the number is even or odd.
# *whether it is divisible by 3.
# *whether it is divisible by 5.
# create a seperate file for this task

def check_number(number):
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

    if number % 3 == 0:
        print("The number is divisible by 3.")
    else:
        print("The number is not divisible by 3.")

    if number % 5 == 0:
        print("The number is divisible by 5.")
    else:
        print("The number is not divisible by 5.")


user_number = int(input("Enter an integer: "))
check_number(user_number)