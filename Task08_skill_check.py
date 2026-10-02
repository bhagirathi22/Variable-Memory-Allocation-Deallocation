# Task8:
# Create a list of required skills 
# ["pyhton","SQL", "Git", "HTML"]
# Create a function that accepts skill name and checks whether exists in the list.
# Display skill available or skill not available.

required_skills = ["python", "SQL", "Git", "HTML"]


def check_skill(skill_name):
    if skill_name in required_skills:
        return "Skill available"
    else:
        return "Skill not available"


skill = input("Enter a skill name: ")
print(check_skill(skill))