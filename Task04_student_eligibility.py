# Task4:
# Create a function that accepts
# *marks
# *attendance percentage
# *backlog status
# A student is eligible only when marks>=60 and attendence >=75% backlog=false. 
# return eligible or not eligible.
def check_eligibility(marks, attendance, has_backlog):
	if marks >= 60 and attendance >= 75 and not has_backlog:
		return "Eligible"
	else:
		return "Not Eligible"


marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
has_backlog = input("Does the student have a backlog? (yes/no): ").lower() == "yes"

print(check_eligibility(marks, attendance, has_backlog))
