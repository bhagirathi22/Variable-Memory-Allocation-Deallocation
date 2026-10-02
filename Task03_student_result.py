# Task3:
# Create a function that accepts a student marks and returns 
# *Passed if marks are greater than or equal to 35
# *Fail otherwise.
# *Distinction if marks are greater than or equals to 75.
# create aseperate file
def check_result(marks):
	if marks >= 75:
		return "Passed with Distinction"
	elif marks >= 35:
		return "Passed"
	else:
		return "Fail"


student_marks = float(input("Enter student marks: "))
print(check_result(student_marks))
