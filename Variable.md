1.# Python Variables and Memory Allocation

## 1. What is a variable in Python?

A variable in Python is not a container that stores a value directly. Instead, it is a name that refers to an object stored in memory.

Example:

```python
x = 10
```

In this case:

- The name `x` is a variable
- The value `10` is an object in memory
- The variable `x` points to that object

So conceptually it is:

```python
x -> 10
```

This is different from the idea of a box containing data. In Python, variables are references to objects.

---

## 2. Everything in Python is an object

This is one of the most important concepts in Python.

```python
x = 10
name = "Yati"
marks = 85.5
numbers = [10, 20, 30]
```

Here:

- `x` refers to an integer object
- `name` refers to a string object
- `marks` refers to a float object
- `numbers` refers to a list object

Every object in Python has three core properties:

1. Identity
   - A unique identifier for the object
   - Obtained using `id(object)`

2. Type
   - The category of the object
   - Obtained using `type(object)`

3. Value
   - The actual data stored in the object

Example:

```python
x = 10
print(id(x))
print(type(x))
print(x)
```

This shows:

- `id(x)` gives the identity of the object
- `type(x)` tells us the type of the object
- `x` prints the value of the object

---

## 3. Python data types

Python has many built-in data types. A standard classification is:

- Numeric
  - `int`
  - `float`
  - `complex`
- Boolean
  - `bool`
- Text
  - `str`
- Sequence
  - `list`
  - `tuple`
  - `range`
- Set
  - `set`
  - `frozenset`
- Mapping
  - `dict`
- Binary
  - `bytes`
  - `bytearray`
  - `memoryview`
- Special
  - `None`

---

## 4. Numeric types

### 4.1 Integer (`int`)

Integers are whole numbers.

```python
age = 25
count = -10
```

### 4.2 Float (`float`)

Floats represent decimal values.

```python
price = 99.50
percentage = 85.75
```

### 4.3 Complex (`complex`)

Complex numbers contain a real and imaginary part.

```python
z = 3 + 4j
```

---

## 5. Boolean type

Boolean values represent truth or falsehood.

```python
is_active = True
is_logged_in = False
```

Examples of boolean conversion:

```python
bool(0)      # False
bool(1)      # True
bool("")    # False
bool("Hello")  # True
```

---

## 6. String (`str`)

A string is an immutable sequence of characters.

```python
name = "String"
```

String indexing works like this:

```python
name[0]   # first character
name[1]   # second character
```

Strings are immutable, meaning they cannot be changed in place once created.

---

## 7. List (`list`)

A list is an ordered, mutable collection.

```python
numbers = [10, 20, 30]
```

Properties of a list:

- Ordered
- Mutable
- Allows duplicates
- Can store different types of data

Example:

```python
data = [10, "python", 25.5, True]
```

Lists can be changed after creation.

---

## 8. Tuple (`tuple`)

A tuple is an ordered, immutable collection.

```python
point = (10, 20)
```

Properties of a tuple:

- Ordered
- Immutable
- Allows duplicates

Tuples cannot be changed after creation, unlike lists.

---

## 9. Set (`set`)

A set is an unordered collection of unique elements.

```python
numbers = {10, 20, 20, 30}
```

This will become:

```python
{10, 20, 30}
```

Properties:

- Unique elements only
- Mutable
- Not index-based like lists

---

## 10. Dictionary (`dict`)

A dictionary stores data in key-value pairs.

```python
student = {"id": 101, "name": "Yati", "marks": 85}
```

This is useful for representing structured data.

Example:

```python
student["name"]   # Yati
```

---

## 11. `None`

`None` represents the absence of a value.

```python
result = None
```

Important: `None` is not the same as:

- `0`
- `False`
- `""`
- `[]`

These are different values with different meanings.

---

## 12. Mutable vs Immutable objects

### Immutable objects

Immutable objects cannot be changed after they are created.

Examples:

- `int`
- `float`
- `bool`
- `str`
- `tuple`
- `frozenset`

### Mutable objects

Mutable objects can be modified after creation.

Examples:

- `list`
- `dict`
- `set`
- `bytearray`

---

## 13. Rebinding vs modification

The object referenced by a variable may be mutable or immutable.

Example with immutable object:

```python
x = 10
x = 20
```

This does not modify the old integer object `10`. Instead, the variable `x` is rebound to a new object `20`.

So the real idea is:

```python
x -> 10
x -> 20
```

The old object `10` is not changed.

---

## 14. Memory example with aliasing

```python
a = 10
b = a
```

Conceptually:

```python
a -> 10
b -> 10
```

Both names refer to the same integer object.

Now if we do:

```python
a = 20
```

Then:

```python
a -> 20
b -> 10
```

`b` still points to the original object `10`.

---

## 15. Mutable object example

```python
a = [10, 20]
b = a
b.append(30)
print(a)
```

Output:

```python
[10, 20, 30]
```

Why?

Because both `a` and `b` reference the same list object. The `append()` method modifies the same object in memory.

Conceptually:

```python
a --> [10, 20]
b --> [10, 20]
```

After `append(30)`: the single list object becomes:

```python
[10, 20, 30]
```

---

## 16. `==` vs `is`

### `==`

This checks whether two values are equal.

```python
a == b
```

### `is`

This checks whether two variables refer to the same object.

```python
a is b
```

Example:

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a is b)  # False
```

Even though the values are equal, they are different objects in memory.

---

## 17. Where is memory used?

At a conceptual level, Python programs use memory for:

- Program code
- Objects
  - integers
  - strings
  - lists
  - dictionaries
  - functions
  - custom objects

In CPython, objects are managed by Python’s memory system. Memory is obtained from the underlying process and managed automatically.

Key idea:

> Python variable names are references to objects, and CPython manages object memory dynamically.

The exact implementation details may vary across Python implementations.

---

## 18. Reference counting in CPython

CPython mainly uses a technique called reference counting.

Example:

```python
a = [1, 2, 3]
b = a
```

Conceptually:

```python
a --> [1, 2, 3]
b --> [1, 2, 3]
```

There are two references to the same object.

Now:

```python
del b
```

The reference count decreases. The object still exists as long as `a` refers to it.

---

## 19. What is garbage collection?

Garbage collection is the process of identifying objects that are no longer reachable and reclaiming their memory.

Python has automatic memory management, so programmers usually do not need to manually call `free()` or delete memory as in some other languages.

This means Python handles memory cleanup for us.

---

## 20. Reference counting + garbage collector

Python uses a combination of:

1. Reference counting
   - Immediately tracks how many references point to an object

2. Cyclic garbage collection
   - Handles reference cycles that reference counting alone cannot reclaim

Example of a reference cycle:

```python
a = []
a.append(a)
```

Here, the list contains itself. This creates a cycle.

Reference counting cannot always detect this kind of structure, so Python uses a cyclic garbage collector (`gc`) to clean it up.

---

## 21. `del` does not always mean immediate destruction

The `del` statement removes a variable name or reference.

Example:

```python
numbers = [1, 2, 3]
del numbers
```

This does not necessarily destroy the object immediately.

Why?

Because the object may still be referenced elsewhere.

Example:

```python
numbers = [1, 2, 3]
b = numbers

del numbers
print(b)   # [1, 2, 3]
```

The object still exists because `b` still points to it.

So `del` removes a reference, not necessarily the object itself.

---

## 22. When does an object become garbage?

An object becomes garbage when no names or references point to it.

Example:

```python
numbers = [1, 2, 3]
b = numbers

del numbers
del b
```

Now there are no remaining references to that list object.

At that point, it becomes eligible for memory reclamation.

The exact time when memory is actually returned to the system may depend on the Python implementation and runtime behavior.

---

## 23. Summary of the variable-object-memory relationship

```text
VARIABLE --> OBJECT --> MEMORY
          |
          +--> identity
          +--> type
          +--> value
```

If an object is no longer reachable:

```text
OBJECT --> NO LONGER REACHABLE --> GARBAGE COLLECTION --> MEMORY REUSE/RECOVERY
```

---

## 24. Final concept

If Python has automatic garbage collection, why does `del numbers` not always destroy the object immediately?

Because:

- `del` removes only the variable name or reference
- The object may still be referenced by other variables
- The object remains alive as long as at least one reference points to it
- Memory is cleaned up only when the object becomes unreachable and the collector reclaims it

This is the core relationship between variables, objects, references, and memory in Python.

---

## 25. Quick revision points

- A variable is a name that references an object.
- Everything in Python is an object.
- Objects have identity, type, and value.
- Data types include numeric, boolean, strings, lists, tuples, sets, dictionaries, and `None`.
- Mutable objects can change; immutable objects cannot.
- `==` compares values; `is` compares object identity.
- Python uses reference counting and garbage collection for memory management.
- `del` removes a reference, not necessarily the object itself.

---

## 26. Short conclusion

Python memory management is automatic and object-based. Variables are not standalone data storage units; they are names pointing to objects in memory. Python keeps track of references, reuses memory when objects become unreachable, and uses garbage collection to manage cycles and other difficult cases.

This understanding is essential for writing efficient, correct, and interview-ready Python programs.

