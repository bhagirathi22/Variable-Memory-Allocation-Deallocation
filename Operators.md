# Python Examples: Task01 to Task10

This guide explains all ten Python programs in beginner-friendly language. Each code block is copied from its matching `.py` file. The explanations describe only the behavior that the current code implements; the source files are not changed.

## Common Python Basics

These ideas appear in several programs:

- A **variable** is a name that refers to a value, such as `number1`, `marks`, or `has_backlog`.
- `input("message")` shows a prompt and reads the user's response as text (a string).
- `int(value)` converts suitable text to a whole number. `float(value)` converts suitable text to a number that can have a decimal part.
- `print(value)` displays a value or message.
- `def function_name(...):` defines a function. Defining it prepares the function; calling it, such as `function_name(...)`, runs it.
- A **parameter** is a name inside the function definition. An **argument** is the actual value passed when calling the function.
- `return` sends a value back from a function to the caller and ends that call. `print()` displays a value; it does not send a result back to the caller.
- Indentation (spaces at the start of a line) marks which statements belong to a function or condition.
- A line beginning with `#` is a comment. It explains the program to readers and is not executed.

---

## 1. `Task01_calculator.py`

### Program 1: Basic Arithmetic Calculator

**Purpose:** Calculate several arithmetic results for two numbers.

**What it does:** Reads two numbers and displays their sum, difference, product, quotient, floor quotient, and remainder. Division, floor division, and remainder are only calculated if the second number is not zero.

### Code

```python
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
```

### Code Explanation

- The first two lines are comments describing the task.
- `number1 = float(input(...))` displays the first prompt, reads the response as text, converts it to a decimal-capable number, and stores it in `number1`.
- The next line does the same for `number2`.
- `number1 + number2` adds the two values. The `-` operator subtracts, and `*` multiplies.
- `if number2 != 0:` checks whether `number2` is different from zero. `!=` means “not equal to.”
- `/` performs ordinary division. `//` performs floor division: it rounds the quotient down. Because both inputs are converted to floats, the result may still be displayed as a float, for example `3.0`.
- `%` finds the remainder left after division.
- The indented `print()` statements under `if` run only when `number2` is not zero.
- `else` runs when the second number is zero and prints a warning instead of attempting those three operations.

### How It Executes

1. The program asks for the first number and converts it to a float.
2. It asks for the second number and converts it to a float.
3. It displays addition, subtraction, and multiplication.
4. It checks whether the second number is zero.
5. For a nonzero second number, it displays division, floor division, and remainder. For zero, it displays the warning.

### Example

**Input:** `10`, then `3`

**Expected output:**

```text
Addition: 13.0
Subtraction: 7.0
Multiplication: 30.0
Division: 3.3333333333333335
Floor division: 3.0
Remainder: 1.0
```

### Important Concepts

- `float()` allows decimal input such as `2.5`.
- `+`, `-`, `*`, `/`, `//`, and `%` are arithmetic operators.
- The program itself does not define or call a function; its statements execute from top to bottom.
- **Limitation:** entering text that is not a valid number causes `float()` to raise an error. This program does not handle that error.

---

## 2. `Task02_number_checks.py`

### Program 2: Even, Odd, and Divisibility Checks

**Purpose:** Check an integer for evenness and divisibility by 3 and 5.

**What it does:** Reads an integer, sends it to `check_number()`, and prints a result for each of the three checks.

### Code

```python
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
```

### Function: `check_number(number)`

- **Parameter:** `number` receives the integer provided by the caller.
- **First check:** `number % 2` calculates the remainder after division by 2. If it equals `0`, the function prints that the number is even; otherwise, it prints that it is odd.
- **Second check:** `number % 3 == 0` tests divisibility by 3. A zero remainder means it is divisible without anything left over.
- **Third check:** `number % 5 == 0` performs the same kind of test for 5.
- Each check is its own `if`/`else`, so all three checks run. For example, a number can be both even and divisible by 5.
- **Return value:** This function has no `return` statement. It prints its messages directly and returns Python's default `None` value, which this program does not use.

### Other Code and Execution

- `user_number = int(input(...))` asks for a value, converts it from text to an integer, and stores it.
- `check_number(user_number)` calls the function. `user_number` is the argument passed into the parameter `number`.
- Execution order: define the function, read the integer, call the function, then run the three checks in order.

### Example

**Input:** `15`

**Expected output:**

```text
The number is odd.
The number is divisible by 3.
The number is divisible by 5.
```

### Important Concepts

- `%` is the remainder (modulo) operator.
- `==` checks whether two values are equal.
- `int()` expects a whole-number input.
- **Limitation:** non-integer text, such as `three`, causes `int()` to raise an error; the program does not catch it.

---

## 3. `Task03_student_result.py`

### Program 3: Result Based on Student Marks

**Purpose:** Return a result label based on marks.

**What it does:** Returns distinction for marks of 75 or more, pass for marks from 35 up to but not including 75, and fail for marks below 35.

### Code

```python
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
```

### Function: `check_result(marks)`

- **Parameter:** `marks` receives the student's numeric mark.
- `if marks >= 75:` checks the highest threshold first. `>=` means “greater than or equal to.”
- If that condition is true, `return "Passed with Distinction"` gives the result back and immediately ends this function call. The lower checks are skipped.
- If the first condition is false, `elif marks >= 35:` checks whether the mark is at least 35. If true, the function returns `"Passed"`.
- If both conditions are false, `else` returns `"Fail"`.
- The order is important. Checking the pass threshold first would also match distinction marks and could prevent the distinction result.
- **Return value:** The function returns one string: `"Passed with Distinction"`, `"Passed"`, or `"Fail"`. It does not print the result itself.

### Other Code and Execution

- `student_marks = float(input(...))` reads and converts the mark. `float()` allows values such as `74.5`.
- `print(check_result(student_marks))` calls the function, receives the returned string, and displays it.
- Execution order: read marks, call the function, test the thresholds from highest to lowest, return one result, and print it.

### Example

**Input:** `82.5`

**Expected output:**

```text
Passed with Distinction
```

### Important Concepts

- `if` checks the first condition; `elif` checks another condition only if earlier conditions were false; `else` handles what remains.
- `return` sends a value to the caller and ends the function.
- **Limitation:** the program does not validate a marks range such as 0 through 100. Negative values are classified as `Fail`, and values above 100 as distinction.

---

## 4. `Task04_student_eligibility.py`

### Program 4: Student Eligibility Check

**Purpose:** Check whether a student satisfies all three eligibility requirements.

**What it does:** Returns `Eligible` only when marks are at least 60, attendance is at least 75%, and the student has no backlog.

### Code

```python
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
```

### Function: `check_eligibility(marks, attendance, has_backlog)`

- **Parameters:** `marks` is the student's mark, `attendance` is the attendance percentage, and `has_backlog` is a Boolean (`True` or `False`).
- `marks >= 60` is true when the marks requirement is met.
- `attendance >= 75` is true when the attendance requirement is met.
- `and` means every connected condition must be true.
- `not has_backlog` is true only when `has_backlog` is false, meaning the student has no backlog.
- All three parts must be true for the function to return `"Eligible"`; otherwise, the `else` returns `"Not Eligible"`.
- **Return value:** The function returns one of those two strings. The caller prints the returned string.

### Other Code and Execution

- The first two input statements convert marks and attendance to floats.
- `input(...).lower()` changes the answer to lowercase. `== "yes"` compares it with `yes`, producing `True` for yes and `False` for other responses.
- `print(check_eligibility(marks, attendance, has_backlog))` passes the three values as arguments and displays the returned result.
- Execution order: collect the three values, convert them to the needed types, call the function, evaluate all requirements, and print the result.

### Example

**Input:** marks `80`, attendance `90`, backlog `no`

**Expected output:**

```text
Eligible
```

### Important Concepts

- `and` requires all conditions to be true.
- `not` reverses a Boolean value: `not False` is `True`.
- `.lower()` is a string method that makes letters lowercase.
- **Behavior note:** only the answer `yes`, in any capitalization, becomes `True`. An unexpected answer is treated as no backlog because the program does not ask again or validate it.

---

## 5. `Task05_user_login.py`

### Program 5: Username and Password Check

**Purpose:** Compare the entered username and password with fixed values.

**What it does:** Returns `Valid user` only when the username is exactly `Admin` and the password is exactly `python123`.

### Code

```python
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
```

### Function: `check_login(username, password)`

- **Parameters:** `username` receives the name to check; `password` receives the password to check. Both are strings because they come from `input()`.
- `username == "Admin"` compares the entered name with the required name exactly.
- `password == "python123"` compares the entered password with the required password exactly.
- `and` means both comparisons must be true. Getting only one correct is not enough.
- If both match, the function returns `"Valid user"`. Otherwise, it returns `"Invalid user"`.
- **Return value:** One of those two strings. The function does not display it; the caller prints it.

### Other Code and Execution

- The two `input()` calls read the username and password as text. They are not converted to numbers.
- `check_login(user_name, user_password)` passes the two entered values as arguments.
- `print(...)` displays the returned message.
- Execution order: read both values, call the function, compare both values, return the decision, and display it.

### Example

**Input:** username `Admin`, password `python123`

**Expected output:**

```text
Valid user
```

### Important Concepts

- `==` compares values. Text comparison is case-sensitive, so `admin` is not the same as `Admin`.
- **Security limitation:** this is a learning exercise, not secure login software. The password is written directly in the source code and is not protected or stored securely.

---

## 6. `Task06_discount_calculator.py`

### Program 6: Purchase Discount Calculator

**Purpose:** Find the discount amount and final amount to pay for a purchase.

**What it does:** Uses a 20% discount for purchases of Rs. 5000 or more, 10% for Rs. 3000 or more but below Rs. 5000, and 5% below Rs. 3000.

### Code

```python
# Task6:
# Create a function that accepts the purchase amount.
# apply ₹5000 or more(20% discount)
#       ₹3000  to 4999(10% discount)
#       below ₹3000(5% discount)
# return discount amount and final payable amount

def calculate_discount(amount):
	if amount >= 5000:
		discount_rate = 0.20
	elif amount >= 3000:
		discount_rate = 0.10
	else:
		discount_rate = 0.05

	discount_amount = amount * discount_rate
	final_amount = amount - discount_amount
	return discount_amount, final_amount


purchase_amount = float(input("Enter the purchase amount in rupees: "))
discount, payable = calculate_discount(purchase_amount)

print("Discount amount: Rs.", format(discount, ".2f"))
print("Final payable amount: Rs.", format(payable, ".2f"))
```

### Function: `calculate_discount(amount)`

- **Parameter:** `amount` is the purchase total passed to the function.
- The first `if` checks `amount >= 5000`. If true, `discount_rate` becomes `0.20` (20%).
- If that condition is false, `elif amount >= 3000` checks the next threshold. That makes this branch cover amounts from 3000 up to, but not including, 5000; the rate is `0.10` (10%).
- `else` covers amounts below 3000 and sets the rate to `0.05` (5%).
- `discount_amount = amount * discount_rate` multiplies the purchase amount by the selected rate.
- `final_amount = amount - discount_amount` subtracts the discount from the original amount.
- `return discount_amount, final_amount` sends both results back. Python groups multiple returned values into a tuple.
- **Return values:** First the discount amount, then the final amount. The order matters because the caller assigns them to `discount` and `payable` in that same order.

### Other Code and Execution

- `float(input(...))` reads the purchase amount and converts it to a float.
- `discount, payable = calculate_discount(purchase_amount)` calls the function and unpacks its two results into two variables.
- `format(value, ".2f")` converts the number to display text with exactly two digits after the decimal point.
- Execution order: read the total, select the rate, calculate both amounts, return them, then print formatted values.

### Example

**Input:** `5000`

**Expected output:**

```text
Discount amount: Rs. 1000.00
Final payable amount: Rs. 4000.00
```

### Important Concepts

- A percentage is represented as a decimal in the calculation: 20% is `0.20`.
- `if`/`elif`/`else` ensures exactly one discount rate is selected.
- **Limitation:** the code does not reject a negative purchase amount.

---

## 7. `Task07_access_check.py`

### Program 7: Access Permission Check

**Purpose:** Decide whether a person should be granted access.

**What it does:** Grants access if the person is at least 18 and has an ID, or if the person is an employee. Employee status alone is sufficient under the actual condition.

### Code

```python
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
```

### Function: `check_access(age, has_id, is_employee)`

- **Parameters:** `age` is an integer; `has_id` and `is_employee` are Boolean values.
- `age >= 18` checks whether the person is at least 18 years old.
- `age >= 18 and has_id` is true only when both the age rule and ID rule are true.
- Parentheses group that age-and-ID rule together.
- `or is_employee` makes being an employee an alternate path. If `is_employee` is true, the whole condition is true even if the person is younger than 18 or has no ID.
- The function returns `"Access Granted"` when the condition is true and `"Access Denied"` otherwise.
- **Return value:** One message string. The outer `print()` displays it.

### Other Code and Execution

- `int(input(...))` reads age and converts it to a whole number.
- Each yes/no expression uses `.lower()` and compares the result to `"yes"`. This makes `YES`, `Yes`, and `yes` all produce `True`.
- The three entered values are passed as arguments to `check_access()`.
- Execution order: read the three answers, convert them, call the function, evaluate the grouped Boolean condition, then display the returned decision.

### Example

**Input:** age `16`, ID `no`, employee `yes`

**Expected output:**

```text
Access Granted
```

### Important Concepts

- `and` requires both sides to be true; `or` requires at least one side to be true.
- Parentheses make the intended condition grouping clear.
- **Behavior note:** every ID/employee answer other than `yes` (case-insensitive) becomes `False`.

---

## 8. `Task08_skill_check.py`

### Program 8: Check Whether a Skill Is in the List

**Purpose:** Find out whether a requested skill is included in the program's required skills.

**What it does:** Creates a list of four skills, reads one skill name, and returns a message indicating whether the exact text is in the list.

### Code

```python
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
```

### Function: `check_skill(skill_name)`

- **Parameter:** `skill_name` receives the skill text typed by the user.
- `skill_name in required_skills` checks whether that exact value appears in the list.
- If the test is true, the function returns `"Skill available"`; otherwise, `else` returns `"Skill not available"`.
- **Return value:** One of those two strings. The function does not print; the caller prints its answer.
- `required_skills` is not a parameter. It is a variable outside the function, and this function reads that list directly.

### Other Code and Execution

- `required_skills = [...]` creates a list of strings. A list keeps several values together inside square brackets.
- `skill = input(...)` reads the skill name as text.
- `check_skill(skill)` passes the text as the argument for `skill_name`.
- `print(...)` displays the returned message.
- Execution order: create the list, define the function, read the requested skill, check list membership, then print the result.

### Example

**Input:** `python`

**Expected output:**

```text
Skill available
```

### Important Concepts

- `in` is a membership operator; it checks whether a value is present in a collection.
- Text comparisons are case-sensitive here. `python` matches the list, while `Python` does not.
- **Real-world analogy:** this function is like checking whether a requested item appears on a checklist.

---

## 9. `Task09_calculator_function.py`

### Program 9: Calculator Function with Operator Selection

**Purpose:** Perform one selected arithmetic operation and handle unsupported operators and division by zero.

**What it does:** Reads two numbers and an operator, then calls `calculate()` to return the result or a message.

### Code

```python
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
```

### Function: `calculate(a, operator, b)`

- **Parameters:** `a` is the first number, `operator` is the selected symbol as text, and `b` is the second number.
- The function checks the operator using an `if` followed by `elif` branches. Since these are connected, it returns from the first matching branch and does not check later branches.
- `+` returns `a + b`; `-` returns `a - b`; `*` returns `a * b`.
- `/`, `//`, and `%` each include `b != 0` in their conditions. They return ordinary division, floor division, and remainder respectively, only when the second value is nonzero.
- `**` returns `a` raised to the power `b`.
- `operator in ("/", "//", "%")` checks whether the selected symbol is one of the three division-related operators. If so, and `b == 0`, the function returns `"Cannot divide by zero."`.
- The final `else` returns `"Invalid operator."` for an unsupported symbol.
- **Return value:** Depending on the operation, it returns a number or an explanatory string. The caller prints either result.

### Other Code and Execution

- `number1` and `number2` are read as floats, allowing decimal numbers.
- `operator` remains a string because the program needs to compare it with symbols such as `+` or `//`.
- `calculate(number1, operator, number2)` passes the three inputs in parameter order.
- Execution order: read first number, read operator, read second number, test operation branches in order, return a result/message, and print it.

### Example

**Input:** first number `2`, operator `**`, second number `3`

**Expected output:**

```text
8.0
```

### Important Concepts

- `**` means “raised to the power of”; `2 ** 3` is 8.
- `in` checks membership in a tuple of allowed division operators.
- `and` requires both the operator comparison and the zero check to be true.
- **Limitation:** invalid numeric text causes `float()` to raise an error; the code does not catch it. Negative exponents and other numeric edge cases follow Python's normal arithmetic behavior.

---

## 10. `Task10_placement_eligibility.py`

### Program 10: Placement Eligibility and Experience Category

**Purpose:** Report whether a candidate meets placement conditions and classify their experience.

**What it does:** Eligibility requires age of at least 18, marks of at least 60, attendance of at least 75%, and no backlog. Separately, it classifies experience as Fresher, Junior, Experienced, or Invalid experience.

### Code

```python
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
```

### Function: `check_placement(age, marks, attendance, experience, has_backlog)`

- **Parameters:** `age` is a whole number; `marks`, `attendance`, and `experience` are numeric values; `has_backlog` is `True` or `False`.
- The first `if` checks four requirements joined by `and`: age is at least 18, marks are at least 60, attendance is at least 75, and `not has_backlog` is true. All four must pass for `eligibility` to become `"Yes"`.
- If any eligibility requirement fails, the `else` sets `eligibility` to `"No"`.
- The second condition group is independent of eligibility. It determines a category for the experience value either way.
- `experience == 0` assigns `"Fresher"`.
- `0 < experience <= 2` is a chained comparison. It means experience is greater than zero and at most two, so it assigns `"Junior"`.
- `experience > 2` assigns `"Experienced"`.
- The final `else` assigns `"Invalid experience"`, which includes negative experience values.
- `return eligibility, category` returns both strings together as a tuple. The first returned value is eligibility; the second is category.

### Other Code and Execution

- Age is converted with `int()`. Marks, attendance, and experience are converted with `float()`.
- The backlog answer is lowercased and compared with `"yes"`, producing a Boolean value.
- `eligibility, category = check_placement(...)` calls the function and unpacks the two returned values into matching variables.
- The two final `print()` statements display each result with a label.
- Execution order: read and convert all five inputs, call the function, check eligibility, classify experience, return both results, unpack them, and print them.

### Example

**Input:** age `21`, marks `80`, attendance `85`, experience `1.5`, backlog `no`

**Expected output:**

```text
Placement eligible: Yes
Candidate category: Junior
```

### Important Concepts

- The eligibility test and experience-category test are separate. A candidate can be classified as a Junior while receiving `No` for placement eligibility.
- `and` requires all eligibility requirements; `not` reverses the backlog Boolean.
- `0 < experience <= 2` is a chained comparison.
- **Limitation:** the program does not validate sensible ranges for age, marks, or attendance. It also allows fractional years of experience because that input uses `float()`.

---

## Quick Revision

### Variables and Data Types

- A **variable** is a name associated with a value, such as `marks` or `discount_rate`.
- `int` represents whole numbers; `float` represents numbers that may have decimals.
- `str` represents text, such as an operator symbol or a returned message.
- `bool` represents `True` or `False`. The yes/no conversions in Tasks 4, 7, and 10 create Boolean values.
- A **list** stores multiple values in order. Task 8 uses one for required skills.
- A **tuple** groups values. Functions in Tasks 6 and 10 return multiple values, which Python groups as a tuple.

### Input and Output

- `input()` reads a response as text.
- `int()` and `float()` convert numeric text.
- `print()` displays output.
- `format(value, ".2f")` in Task 6 displays two digits after the decimal point.
- **Input errors:** the programs do not use exception handling, so invalid numeric text can stop a program with a conversion error.

### Operators

- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- Comparison: `==`, `!=`, `>=`, `>`.
- Logical: `and`, `or`, `not`.
- Membership: `in`.
- Assignment: `=`.
- The `%` remainder operator is often used to test divisibility: if `number % divisor == 0`, the number is divisible by that divisor.

### Conditions and Functions

- `if` checks a condition; `elif` checks another option when earlier conditions are false; `else` handles the remaining case.
- `def` creates a function. A function runs only when called.
- Parameters are the function's input names; arguments are the values supplied by the caller.
- `return` sends a result to the caller. A function can return a single value or multiple values.
- Some functions print results inside themselves (Task 2); most of the other functions return results for the outer code to print.
- Chained comparisons such as `0 < experience <= 2` check whether a value falls within a range.

### Concepts Not Used in These Programs

These ten files do not use loops, dictionaries, sets, imports/modules, or exception handling. They do use variables, numeric and string values, Boolean conditions, input/output, operators, functions, parameters, arguments, return values, lists, tuples, and string methods.
