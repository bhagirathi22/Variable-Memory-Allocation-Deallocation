# Task5:
# Create a function that accepts username and password.
# The user should be considered valid only when 
# Username ="Admin" and Password=="python123
def check_login(username, password):
    if username == "Admin" and password == "python123":
        return "Valid user"
    else:
        return "Invalid user"


user_name = input("Enter username: ")
user_password = input("Enter password: ")

print(check_login(user_name, user_password))