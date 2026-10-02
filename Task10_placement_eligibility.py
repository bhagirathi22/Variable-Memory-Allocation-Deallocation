# Task10:
# Create a function that accepts 
# age ,marks,attendence,experience, has_backlog
# determine placement eligibility.
# age>=18, marks>=60, attendance>=75, and has_backlog=False for eligibility.
# experience 0-->Fresher, 1-2-->Junior, more than 2-->Experienced.
# Finally display
# 1.placement eligible : yes/no.
# 2.Candidate category: Fresher/junior/experienced.

def check_placement(age, marks, attendance, experience, has_backlog):
    if age >= 18 and marks >= 60 and attendance >= 75 and not has_backlog:
        eligibility = "Yes"
    else:
        eligibility = "No"

    if experience == 0:
        category = "Fresher"
    elif 0 < experience <= 2:
        category = "Junior"
    elif experience > 2:
        category = "Experienced"
    else:
        category = "Invalid experience"

    return eligibility, category


age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
experience = float(input("Enter years of experience: "))
has_backlog = input("Does the student have a backlog? (yes/no): ").lower() == "yes"

eligibility, category = check_placement(age, marks, attendance, experience, has_backlog)
print("Placement eligible:", eligibility)
print("Candidate category:", category)