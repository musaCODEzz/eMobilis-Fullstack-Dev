# ============================================================
# Week 3 - Python Basics: Data Types
# ============================================================
# Python has several built-in data types. Understanding them is
# essential because different types behave differently.

# ----------------------------------------------------------
# 1. STRING (str) — sequence of characters in quotes
# ----------------------------------------------------------
name = "Musa"
print(name)
print(type(name))       # <class 'str'>

# String methods
print(name.upper())     # MUSA
print(name.lower())     # musa
print(len(name))        # 4  (number of characters)
print(name[0])          # M  (indexing — starts at 0)
print(name[-1])         # a  (negative index — from the end)
print(name[1:3])        # us (slicing)

sentence = "  Hello, Python!  "
print(sentence.strip())         # Remove whitespace
print(sentence.replace("Python", "World"))

# Checking membership in a string
print("Musa" in "My name is Musa")   # True

# ----------------------------------------------------------
# 2. INTEGER (int) — whole numbers (no decimal point)
# ----------------------------------------------------------
age = 20
print(age)
print(type(age))        # <class 'int'>
print(age + 5)
print(age * 2)

# Large numbers can use underscores for readability
population = 1_000_000
print(population)       # 1000000

# Convert string to int
num_str = "42"
num_int = int(num_str)
print(num_int + 8)      # 50

# ----------------------------------------------------------
# 3. FLOAT (float) — decimal numbers
# ----------------------------------------------------------
height = 5.9
print(height)
print(type(height))     # <class 'float'>

pi = 3.14159
print(round(pi, 2))     # 3.14 (round to 2 decimal places)

# Convert string to float
price_str = "19.99"
price = float(price_str)
print(price * 2)        # 39.98

# Integer division can produce a float
print(7 / 2)            # 3.5  (always float in Python 3)
print(7 // 2)           # 3    (floor division = integer result)

# ----------------------------------------------------------
# 4. BOOLEAN (bool) — True or False (capital T and F)
# ----------------------------------------------------------
is_adult = True
print(is_adult)
print(type(is_adult))   # <class 'bool'>

# Booleans from comparisons
print(10 > 5)           # True
print(10 == 5)          # False

# Truthy and Falsy values
print(bool(0))          # False
print(bool(""))         # False
print(bool(None))       # False
print(bool(1))          # True
print(bool("hello"))    # True

# ----------------------------------------------------------
# 5. LIST — ordered, changeable, allows duplicates
# ----------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])        # apple
print(fruits[-1])       # cherry
print(len(fruits))      # 3

fruits.append("mango")      # Add to end
fruits.insert(1, "blueberry")  # Insert at index 1
print(fruits)

fruits.remove("banana")     # Remove by value
print(fruits)

fruits.pop()                # Remove last item
print(fruits)

# Loop through a list
for fruit in fruits:
    print(f" - {fruit}")

# List slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])     # [20, 30, 40]
print(numbers[:3])      # [10, 20, 30]
print(numbers[::2])     # [10, 30, 50] (every 2nd item)

# ----------------------------------------------------------
# 6. TUPLE — ordered, UNCHANGEABLE, allows duplicates
# ----------------------------------------------------------
coordinates = (10.0, 20.0)
print(coordinates)
print(type(coordinates))    # <class 'tuple'>
print(coordinates[0])       # 10.0

# Tuples are immutable (cannot change after creation)
# coordinates[0] = 99  # This would raise a TypeError!

# Useful for fixed data: RGB colours, GPS coordinates, etc.
red = (255, 0, 0)
print(f"Red colour: {red}")

# ----------------------------------------------------------
# 7. DICTIONARY (dict) — key:value pairs, ordered, changeable
# ----------------------------------------------------------
person = {"name": "Musa", "age": 20}
print(person)
print(person["name"])   # Access by key
print(person.get("age"))  # Safer — returns None if key missing

person["email"] = "musa@email.com"     # Add new key
person["age"] = 21                     # Update existing key
print(person)

# Looping through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary methods
print(person.keys())    # All keys
print(person.values())  # All values

# ----------------------------------------------------------
# 8. SET — unordered, NO duplicates, unchangeable items
# ----------------------------------------------------------
unique_numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(unique_numbers)   # Duplicates are automatically removed

fruits_set = {"apple", "banana", "cherry"}
fruits_set.add("mango")
print(fruits_set)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)    # Union — all items from both
print(a & b)    # Intersection — items in both
print(a - b)    # Difference — items in a but not in b

# ----------------------------------------------------------
# 9. NONE — represents the absence of a value
# ----------------------------------------------------------
nothing = None
print(nothing)
print(type(nothing))    # <class 'NoneType'>

# None is often used as a default/placeholder
result = None
if result is None:
    print("No result yet.")

# ----------------------------------------------------------
# 10. Mixed List (Python allows mixed types in a list)
# ----------------------------------------------------------
my_list = [1, "Hello", 3.14, True, [1, 2, 3]]
print(my_list)
print(my_list[4][1])    # Access nested list — returns 2

# ----------------------------------------------------------
# Type Conversion (Casting)
# ----------------------------------------------------------
print(int(3.9))         # 3   (truncates decimal)
print(float(5))         # 5.0
print(str(100))         # "100"
print(list((1, 2, 3)))  # [1, 2, 3] — tuple to list
print(tuple([1, 2, 3])) # (1, 2, 3) — list to tuple
