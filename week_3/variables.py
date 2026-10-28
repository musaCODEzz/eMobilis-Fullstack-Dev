# ============================================================
# Week 3 - Python Basics: Variables & Constants
# ============================================================
# A variable is a named container that stores a value in memory.
# Python is dynamically typed — you don't declare a type explicitly.

# --- Basic variable assignment ---
x = 5
print(x)

firstName = "Musa"
lastName = "Maxwel"
fullName = firstName + " " + lastName   # String concatenation
print(fullName)

# --- Naming conventions ---
# snake_case is the Python standard for variable names
student_name = "Alice"
student_age = 22
is_enrolled = True

# camelCase is NOT standard in Python (used in JS), but it works
myVariable = "not recommended in Python"

# Variables are case-sensitive
name = "Musa"
Name = "Another Musa"
print(name, Name)   # These are TWO different variables

# --- Multiple assignment (shorthand) ---
a, b, c = 10, 20, 30
print(a, b, c)

# Assign the same value to multiple variables at once
x = y = z = 100
print(x, y, z)

# --- Reassigning variables ---
score = 0
print("Initial score:", score)
score = 50
print("Updated score:", score)
score += 10     # Short form of score = score + 10
print("After bonus:", score)

# --- Checking a variable's type ---
age = 25
height = 5.9
username = "musa123"
active = True
nothing = None

print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(username))   # <class 'str'>
print(type(active))     # <class 'bool'>
print(type(nothing))    # <class 'NoneType'>

# --- Constants (by convention, ALL_CAPS) ---
# Python has no built-in constant keyword, but naming in ALL_CAPS
# signals to other developers "do not change this value".
PI = 3.14159
MAX_STUDENTS = 50
print(f"PI = {PI}, Max students = {MAX_STUDENTS}")

# --- Deleting a variable ---
temp = "temporary"
del temp
# print(temp)  # This would raise a NameError — variable is gone

# --- Swapping two variables (Python shortcut) ---
x = "apple"
y = "banana"
x, y = y, x    # Swap without a temp variable!
print(x, y)    # banana apple

# --- Variable scope preview ---
# Variables created inside a function are LOCAL (you'll learn this soon)
# Variables at the top level are GLOBAL
global_var = "I am accessible everywhere"
print(global_var)
