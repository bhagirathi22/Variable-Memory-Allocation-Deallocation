# Python Functions - Detailed Notes

## 1. Why Functions?

Functions are used to write reusable code. Instead of writing the same code again and again, we can define a function once and call it multiple times.

Example:

```python
print("Bhagirathi")
print("Yati")
print("Gouthami")
```

This can be simplified using a function.

---

## 2. What Exactly is a Function?

A function is a block of reusable code that performs a specific task.

Example:

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

A function helps us keep the program organized and avoid repetition.

Another example:

```python
def welcome(name):
    print("Welcome", name)

welcome("Bhagirathi")
welcome("Yati")
welcome("Gouthami")
```

---

## 3. What Problem Did the Function Solve?

Functions solve the following problems:

- Code reuse
- Less repetition
- Better organization
- Easier maintenance
- Easier testing

Instead of writing the same logic again and again, we build one function and reuse it whenever needed.

---

## 4. Defining vs Calling a Function

### Definition

```python
def greet():
    print("Hello")
```

This only defines the function. It does not execute it.

### Calling

```python
greet()
```

This executes the function body and prints the output.

---

## 5. Function Without Parameters

A function without parameters does not receive any input.

Example:

```python
def welcome():
    print("Welcome to Nighan2 Labs")

welcome()
```

This is the simplest form of a function.

---

## 6. Function with Parameters

A parameter is a variable defined in the function, while an argument is the value passed when calling the function.

Example:

```python
def welcome(name):
    print("Welcome", name)

welcome("Bhagirathi")
```

Here:

- `name` is a parameter
- `"Bhagirathi"` is an argument

---

## 7. Multiple Parameters

A function may have more than one parameter.

Example:

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

This function accepts two values and adds them.

---

## 8. Return - The Most Important Concept

The `return` statement is used to send a value back to the caller.

### Without `return`

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

This prints the result but does not return it.

### With `return`

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Key difference:

- `print()` displays something on the screen
- `return` sends a value back to the caller

---

## 9. What Happens After Return?

When Python reaches a `return` statement, the function stops execution immediately.

Example:

```python
def test():
    return 10
    print("Hello")

print(test())
```

The line `print("Hello")` will not execute because the function already returned.

---

## 10. Multiple Return Values

Python allows a function to return more than one value.

Example:

```python
def calculate(a, b):
    return a + b, a - b, a * b

x, y, z = calculate(10, 5)
print(x)
print(y)
print(z)
```

Output:

```python
15
5
50
```

This means the function actually returns a tuple of values.

---

## 11. Default Parameters

A default parameter is a value assigned to a parameter if the caller does not pass one.

Example:

```python
def greet(name="Bhagirathi"):
    print("Hello", name)

greet()
greet("Yati")
```

Output:

```python
Hello Bhagirathi
Hello Yati
```

Default parameters are useful when a common value is often used.

---

## 12. Positional Arguments

Positional arguments are passed in the order of the parameters.

Example:

```python
def student(name, age):
    print(name, age)

student("Bhavana", 20)
```

The first argument matches the first parameter, and the second matches the second.

---

## 13. Keyword Arguments

Keyword arguments are passed by parameter name.

Example:

```python
def students(name="Bhagirathi", age=21):
    print(name, age)

students(age=25, name="Yati")
```

The order does not matter when using keyword arguments.

---

## 14. Positional and Keyword Arguments

We can mix both types as long as they are used in correct order.

Example:

```python
def student(name, age, course):
    print(name, age, course)

student("Bhagirathi", age=22, course="BCA")
```

This is valid because positional arguments come first, then keyword arguments.

Invalid example:

```python
student(name="Bhagirathi", 21, course="BCA")
```

This is invalid because a positional argument cannot appear after a keyword argument.

---

## 15. `*args`

`*args` allows a function to accept a variable number of positional arguments.

Example:

```python
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(1, 2, 3, 4, 5))
```

`*args` collects all positional arguments into a tuple.

---

## 16. `**kwargs`

`**kwargs` allows a function to accept a variable number of keyword arguments.

Example:

```python
def student(**details):
    print(details)

student(name="Bhagirathi", age=21, course="BCA")
```

This creates a dictionary-like mapping of keyword arguments.

---

## 17. Combining Positional and Keyword Arguments

A function can be designed to accept both positional and keyword arguments together.

Example:

```python
def example(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)

example(1, 2, 3, 4, x=10, y=20)
```

This is a very flexible function structure.

---

## 18. Scope: Local vs Global

### Local variable

A local variable is created inside a function and can be used only inside that function.

Example:

```python
def test():
    x = 10
    print(x)

test()
```

Here, `x` is local to `test()`.

### Global variable

A global variable is created outside a function and is accessible throughout the program.

Example:

```python
x = 100

def test():
    print(x)

test()
```

The function can read the global variable.

---

## 19. `global` Keyword

The `global` keyword allows us to modify a global variable inside a function.

Example:

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)
```

Output:

```python
1
```

Note: Global variables should be used carefully. It is usually better to pass values as parameters and return results instead of changing global state unnecessarily.

---

## 20. Local Scope Inside a Function

A variable declared inside a function cannot be accessed outside it.

Example:

```python
def test():
    x = 10

test()
print(x)
```

This causes a `NameError` because `x` is local to `test()`.

---

## 21. Functions Can Call Other Functions

A function can call another function to perform a task.

Example:

```python
def add(a, b):
    return a + b

def display():
    result = add(10, 20)
    print(result)

display()
```

This demonstrates a simple flow:

- Validate input
- Perform calculation
- Store or return result
- Display output

---

## 22. Final Summary

Functions are one of the most important building blocks in Python because they help us:

- reduce repetition,
- organize logic,
- divide programs into smaller tasks,
- and improve readability.

Important points to remember:

- A function is a reusable block of code.
- Parameters are variables in the function definition.
- Arguments are actual values passed during function call.
- `return` sends a value back to the caller.
- Functions can have default values, variable-length arguments, and keyword arguments.
- Scope determines where a variable can be accessed.

---

## 23. Quick Revision

1. What is a function?  
   A reusable block of code that performs a specific task.

2. What is a parameter?  
   A variable used in the function definition.

3. What is an argument?  
   A value passed while calling the function.

4. What is `return`?  
   It sends a value back to the caller.

5. What is `*args`?  
   It accepts variable numbers of positional arguments.

6. What is `**kwargs`?  
   It accepts variable numbers of keyword arguments.

7. What is local scope?  
   Variables available only inside a function.

8. What is global scope?  
   Variables available throughout the program.

---

## 24. Conclusion

Python functions help us write clean, reusable, and maintainable programs. A proper understanding of parameters, return values, scope, and argument types is essential for writing effective function-based code.

 


        
       

  
 
  
      


