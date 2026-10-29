# ============================================================
# Week 3 - Python Basics: Functions (Deep Dive)
# ============================================================
# A function is a reusable block of code that performs ONE task.
# Instead of writing the same code over and over, you write it
# once inside a function and CALL it whenever you need it.
#
# WHY USE FUNCTIONS?
#   ✅ Reusability   — write once, use many times
#   ✅ Organisation  — break large problems into smaller pieces
#   ✅ Readability   — give a meaningful name to a block of code
#   ✅ Debugging     — easier to find and fix errors
#
# SYNTAX:
#   def function_name(parameters):
#       """Docstring — describes what the function does."""
#       # body of the function
#       return value   # optional — sends a result back
# ============================================================


# ──────────────────────────────────────────────────────────────
# SECTION 1: Basic Functions — No Parameters, No Return
# ──────────────────────────────────────────────────────────────

# The simplest function — just runs some code when called.
def say_hello():
    """Print a simple greeting."""
    print("Hello! Welcome to Python functions. 👋")

say_hello()       # Call the function
say_hello()       # You can call it as many times as you want


# ──────────────────────────────────────────────────────────────
# SECTION 2: Functions With Parameters
# ──────────────────────────────────────────────────────────────

# Parameters are placeholders that accept values when the
# function is called. The values you pass in are "arguments".

def greet(name):
    """Greet a person by their name."""
    print(f"Hello, {name}! Nice to meet you.")

greet("Musa")      # "Musa" is the argument for the 'name' parameter
greet("Alice")
greet("Bob")

# Multiple parameters
def introduce(name, age, city):
    """Introduce a person with their details."""
    print(f"My name is {name}, I'm {age} years old, from {city}.")

introduce("Musa", 20, "Nairobi")
introduce("Alice", 22, "Mombasa")


# ──────────────────────────────────────────────────────────────
# SECTION 3: Functions With Return Values
# ──────────────────────────────────────────────────────────────

# 'return' sends a result back to the caller.
# Without return, a function gives back None.

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

result = add(2, 3)         # result now holds 5
print(f"2 + 3 = {result}") # Output: 2 + 3 = 5
print(f"10 + 20 = {add(10, 20)}")  # You can also print directly

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

print(f"5 - 3 = {subtract(5, 3)}")   # Output: 5 - 3 = 2

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

print(f"4 × 6 = {multiply(4, 6)}")   # Output: 4 × 6 = 24

def divide(a, b):
    """Return the division of two numbers. Handles divide by zero."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

print(f"10 / 3 = {divide(10, 3)}")       # Output: 10 / 3 = 3.333...
print(f"10 / 0 = {divide(10, 0)}")       # Output: Error message


# ──────────────────────────────────────────────────────────────
# SECTION 4: A More Complex Function — Step by Step
# ──────────────────────────────────────────────────────────────

# Let's build a function that calculates a math formula.
# Formula: f(x) = (x² + 3x + 5) / (x - 1)

def complex_function(x):
    """
    Calculate: (x² + 3x + 5) / (x - 1)

    Example:
        x = 2 → (4 + 6 + 5) / (2 - 1) = 15 / 1 = 15.0
        x = 5 → (25 + 15 + 5) / (5 - 1) = 45 / 4 = 11.25
    """
    if x == 1:
        return "Error: Division by zero (x cannot be 1)"
    result = (x ** 2 + 3 * x + 5) / (x - 1)
    return result

print(f"f(2) = {complex_function(2)}")    # Output: 15.0
print(f"f(5) = {complex_function(5)}")    # Output: 11.25
print(f"f(1) = {complex_function(1)}")    # Output: Error message


# ──────────────────────────────────────────────────────────────
# SECTION 5: Default Parameter Values
# ──────────────────────────────────────────────────────────────

# You can set a default value for a parameter. If the caller
# doesn't provide a value, the default is used automatically.

def greet_with_time(name, greeting="Good morning"):
    """Greet someone with a customisable greeting."""
    print(f"{greeting}, {name}!")

greet_with_time("Musa")                    # Uses default: "Good morning"
greet_with_time("Alice", "Good evening")   # Overrides default

# Another example: calculating area with default units
def calculate_area(length, width, unit="m"):
    """Calculate area and show the unit."""
    area = length * width
    print(f"Area = {length} × {width} = {area} {unit}²")
    return area

calculate_area(10, 5)           # Area = 10 × 5 = 50 m²
calculate_area(10, 5, "ft")     # Area = 10 × 5 = 50 ft²


# ──────────────────────────────────────────────────────────────
# SECTION 6: Keyword Arguments (Named Arguments)
# ──────────────────────────────────────────────────────────────

# When calling a function, you can specify which parameter
# gets which value by NAME. Order doesn't matter then.

def create_profile(name, age, course, city):
    """Display a student profile."""
    print(f"📋 {name} | Age: {age} | Course: {course} | City: {city}")

# Positional (order matters)
create_profile("Musa", 20, "Fullstack", "Nairobi")

# Keyword (order doesn't matter — much clearer!)
create_profile(age=22, city="Mombasa", name="Alice", course="Data Science")


# ──────────────────────────────────────────────────────────────
# SECTION 7: *args — Accept ANY Number of Arguments
# ──────────────────────────────────────────────────────────────

# Sometimes you don't know how many values will be passed in.
# *args collects them all into a TUPLE.

def total_price(*prices):
    """Calculate the total of any number of prices."""
    total = sum(prices)
    print(f"Items: {prices}")
    print(f"Total: Ksh {total:,.2f}")
    return total

total_price(100, 250, 75)             # 3 items
total_price(50, 80, 120, 200, 35)     # 5 items
total_price(999)                      # 1 item — still works!

# Another practical example
def average(*numbers):
    """Calculate the average of any number of values."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

print(f"Average of 10, 20, 30 = {average(10, 20, 30)}")      # 20.0
print(f"Average of 85, 90, 78, 92 = {average(85, 90, 78, 92)}")  # 86.25


# ──────────────────────────────────────────────────────────────
# SECTION 8: **kwargs — Accept ANY Number of Keyword Arguments
# ──────────────────────────────────────────────────────────────

# **kwargs collects keyword arguments into a DICTIONARY.

def display_profile(**info):
    """Print all the key-value pairs passed in."""
    print("──── Student Profile ────")
    for key, value in info.items():
        print(f"  {key.capitalize()}: {value}")
    print()

display_profile(name="Musa", age=20, course="Fullstack", city="Nairobi")
display_profile(name="Bob", hobby="Football", email="bob@email.com")


# ──────────────────────────────────────────────────────────────
# SECTION 9: Returning MULTIPLE Values
# ──────────────────────────────────────────────────────────────

# Python functions can return more than one value at a time.
# They are returned as a tuple and can be unpacked.

def min_max(numbers):
    """Return both the smallest and largest number in a list."""
    return min(numbers), max(numbers)

smallest, largest = min_max([4, 1, 9, 2, 7])
print(f"Smallest: {smallest}, Largest: {largest}")  # 1, 9

def get_full_name(first, last):
    """Return full name and its length."""
    full = f"{first} {last}"
    return full, len(full)

name, length = get_full_name("Musa", "Maxwel")
print(f"Name: {name} ({length} characters)")


# ──────────────────────────────────────────────────────────────
# SECTION 10: Recursive Functions (Function Calls Itself)
# ──────────────────────────────────────────────────────────────

# A recursive function calls ITSELF to solve smaller sub-problems.
# Every recursion needs a BASE CASE to stop infinite loops.

def factorial(n):
    """
    Calculate n! (n factorial) using recursion.

    How it works step by step for factorial(5):
        factorial(5) = 5 × factorial(4)
        factorial(4) = 4 × factorial(3)
        factorial(3) = 3 × factorial(2)
        factorial(2) = 2 × factorial(1)
        factorial(1) = 1 × factorial(0)
        factorial(0) = 1  ← BASE CASE (stops here)

        So: 5 × 4 × 3 × 2 × 1 × 1 = 120
    """
    if n == 0:
        return 1           # Base case
    return n * factorial(n - 1)   # Recursive case

print(f"5! = {factorial(5)}")     # 120
print(f"0! = {factorial(0)}")     # 1
print(f"7! = {factorial(7)}")     # 5040

# Countdown using recursion
def countdown(n):
    """Count down from n to 1 using recursion."""
    if n <= 0:
        print("🚀 Go!")
        return
    print(n)
    countdown(n - 1)

countdown(5)


# ──────────────────────────────────────────────────────────────
# SECTION 11: Lambda Functions (Anonymous One-Line Functions)
# ──────────────────────────────────────────────────────────────

# A lambda is a small function written in ONE line.
# Syntax: lambda parameters: expression
# Useful for quick operations — you don't even need a name.

square   = lambda x: x ** 2
double   = lambda x: x * 2
add_lam  = lambda a, b: a + b
is_adult = lambda age: "Adult" if age >= 18 else "Minor"

print(f"square(5)     = {square(5)}")          # 25
print(f"double(7)     = {double(7)}")          # 14
print(f"add(3, 4)     = {add_lam(3, 4)}")      # 7
print(f"is_adult(20)  = {is_adult(20)}")       # Adult
print(f"is_adult(15)  = {is_adult(15)}")       # Minor

# Lambda with sorted() — sort students by their score
students = [("Alice", 85), ("Musa", 92), ("Bob", 78), ("Carol", 95)]
ranked = sorted(students, key=lambda s: s[1], reverse=True)
print("🏆 Rankings:", ranked)

# Lambda with filter() — keep only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Lambda with map() — double every number
doubled = list(map(lambda n: n * 2, numbers))
print(f"Doubled: {doubled}")


# ──────────────────────────────────────────────────────────────
# SECTION 12: Variable Scope (Local vs Global)
# ──────────────────────────────────────────────────────────────

# Variables created INSIDE a function are LOCAL — they only
# exist inside that function.
# Variables created OUTSIDE are GLOBAL — accessible everywhere.

school_name = "eMobilis"    # GLOBAL variable

def show_student(name):
    grade = "A"             # LOCAL variable — only exists here
    print(f"{name} from {school_name} got grade {grade}")

show_student("Musa")
# print(grade)  # ❌ NameError — grade doesn't exist outside the function

# To MODIFY a global variable inside a function, use 'global'
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
increment()
print(f"Counter after 3 increments: {counter}")  # 3


# ──────────────────────────────────────────────────────────────
# SECTION 13: Practical Examples — Real-World Functions
# ──────────────────────────────────────────────────────────────

# --- Example 1: Simple Calculator ---
def calculator(a, b, operation):
    """Perform basic arithmetic based on the operation string."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Unknown operation"

print(calculator(10, 5, "add"))        # 15
print(calculator(10, 5, "subtract"))   # 5
print(calculator(10, 5, "multiply"))   # 50
print(calculator(10, 5, "divide"))     # 2.0

# --- Example 2: Password Strength Checker ---
def check_password(password):
    """Check how strong a password is and give feedback."""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Must be at least 8 characters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("❌ Must contain an uppercase letter")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("❌ Must contain a lowercase letter")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("❌ Must contain a digit")

    if any(c in "!@#$%^&*()_+-=" for c in password):
        score += 1
    else:
        feedback.append("❌ Must contain a special character (!@#$...)")

    # Rating
    if score == 5:
        strength = "💪 STRONG"
    elif score >= 3:
        strength = "⚠️  MEDIUM"
    else:
        strength = "🔴 WEAK"

    print(f"\nPassword: {'*' * len(password)}")
    print(f"Strength: {strength} ({score}/5)")
    for item in feedback:
        print(f"  {item}")

check_password("abc")
check_password("Hello123")
check_password("Musa@2024!")

# --- Example 3: Temperature Converter ---
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit: F = (C × 9/5) + 32"""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius: C = (F - 32) × 5/9"""
    return (fahrenheit - 32) * 5 / 9

print(f"\n25°C = {celsius_to_fahrenheit(25):.1f}°F")       # 77.0°F
print(f"100°C = {celsius_to_fahrenheit(100):.1f}°F")      # 212.0°F
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")        # 25.0°C
print(f"32°F = {fahrenheit_to_celsius(32):.1f}°C")        # 0.0°C


# ──────────────────────────────────────────────────────────────
# SUMMARY
# ──────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("         FUNCTIONS — KEY TAKEAWAYS")
print("=" * 55)
print("""
  ✅ def function_name(params):   — defines a function
  ✅ return value                 — sends back a result
  ✅ Default values               — def f(x, y=10):
  ✅ *args                        — accepts many positional args
  ✅ **kwargs                     — accepts many keyword args
  ✅ Lambda                       — lambda x: x * 2
  ✅ Recursion                    — function calling itself
  ✅ Scope                        — local vs global variables
""")
