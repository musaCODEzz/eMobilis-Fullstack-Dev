# ============================================================
# Week 3 - Python Basics: Hello World & print() Function
# ============================================================
# The print() function outputs text to the console.
# It is usually the very first thing you learn in any language.

print("Hello, World!")
print("This is my first Python program.")
print(1 + 1)        # You can print the result of expressions
print(20)           # You can print numbers directly

# --- print() extras ---
# Printing multiple values separated by a comma
print("Name:", "Musa", "Age:", 20)

# Using sep to change the separator (default is a space)
print("apple", "banana", "cherry", sep=" | ")

# Using end to change the line ending (default is \n)
print("Loading", end="...")
print("Done!")

# Printing blank lines for spacing
print()
print("Python is fun!")

# --- Escape characters ---
print("He said: \"Python is awesome!\"")   # \" inside a string
print("Line1\nLine2\nLine3")               # \n = new line
print("Tab\there")                         # \t = tab space
print("Backslash: \\")                     # \\ = literal backslash

# --- f-strings (formatted string literals) ---
name = "Musa"
course = "Fullstack Development"
print(f"Welcome, {name}! You are learning {course}.")

# --- Checking Python version (good habit) ---
import sys
print(f"Python version: {sys.version}")
