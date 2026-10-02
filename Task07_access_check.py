# Task7:
# Create a function that accepts age, has_id, is_employee.
#  allow access age >= 18 and has_id==TRUE 
# or when is_employee==TRUE 
# return access granted or access denied.
# crete a seperate file with question.

def check_access(age, has_id, is_employee):
    if (age >= 18 and has_id) or is_employee:
        return "Access Granted"
    else:
        return "Access Denied"


age = int(input("Enter age: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"
is_employee = input("Are you an employee? (yes/no): ").lower() == "yes"

print(check_access(age, has_id, is_employee))