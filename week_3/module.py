# ============================================================
# Week 3 - Python Basics: Modules & Packages
# ============================================================
# A MODULE is simply a .py file that contains functions,
# classes, and variables you can REUSE in other files.
#
# WHY USE MODULES?
#   ✅ Organisation — split a big program into smaller files
#   ✅ Reusability  — write once, import anywhere
#   ✅ Namespace    — avoid name clashes between variables
#
# Python comes with 200+ BUILT-IN modules (called the
# Standard Library) — you don't need to install them!
# ============================================================


# ──────────────────────────────────────────────────────────────
# SECTION 1: Importing a Built-in Module — math
# ──────────────────────────────────────────────────────────────

# The 'math' module gives you mathematical functions and constants.
import math

print("=" * 55)
print("1. THE math MODULE")
print("=" * 55)

# Constants
print(f"  π (pi)    = {math.pi}")           # 3.141592653589793
print(f"  e (euler) = {math.e}")            # 2.718281828459045

# Functions
print(f"  sqrt(16)  = {math.sqrt(16)}")     # 4.0
print(f"  pow(2,10) = {math.pow(2, 10)}")   # 1024.0
print(f"  ceil(4.2) = {math.ceil(4.2)}")    # 5  (round UP)
print(f"  floor(4.9)= {math.floor(4.9)}")   # 4  (round DOWN)
print(f"  factorial(5) = {math.factorial(5)}")  # 120

# Practical example: area of a circle
radius = 7
area = math.pi * radius ** 2
print(f"\n  Circle with radius {radius}: Area = {area:.2f}")


# ──────────────────────────────────────────────────────────────
# SECTION 2: Importing a Built-in Module — random
# ──────────────────────────────────────────────────────────────

import random

print()
print("=" * 55)
print("2. THE random MODULE")
print("=" * 55)

# Random integer between a and b (inclusive)
print(f"  Random int (1-10):  {random.randint(1, 10)}")

# Random float between 0 and 1
print(f"  Random float (0-1): {random.random():.4f}")

# Random choice from a list
fruits = ["apple", "banana", "mango", "cherry", "grape"]
print(f"  Random fruit:       {random.choice(fruits)}")

# Shuffle a list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"  Shuffled list:      {numbers}")

# Random sample (pick N items without repeating)
print(f"  Pick 3 fruits:      {random.sample(fruits, 3)}")

# Practical example: simple dice roll
def roll_dice():
    """Simulate rolling two six-sided dice."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"  🎲 Rolled: {die1} + {die2} = {total}")
    return total

roll_dice()
roll_dice()


# ──────────────────────────────────────────────────────────────
# SECTION 3: Importing a Built-in Module — datetime
# ──────────────────────────────────────────────────────────────

from datetime import datetime, timedelta

print()
print("=" * 55)
print("3. THE datetime MODULE")
print("=" * 55)

# Current date and time
now = datetime.now()
print(f"  Now:          {now}")
print(f"  Date only:    {now.date()}")
print(f"  Time only:    {now.time()}")
print(f"  Year:         {now.year}")
print(f"  Month:        {now.month}")
print(f"  Day:          {now.day}")

# Format a date nicely
formatted = now.strftime("%A, %d %B %Y at %I:%M %p")
print(f"  Formatted:    {formatted}")

# Date arithmetic
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
print(f"  Tomorrow:     {tomorrow.date()}")
print(f"  Next week:    {next_week.date()}")

# Calculate age
birthday = datetime(2004, 5, 15)
age_days = (now - birthday).days
age_years = age_days // 365
print(f"  Born {birthday.date()} → approximately {age_years} years old")


# ──────────────────────────────────────────────────────────────
# SECTION 4: Importing a Built-in Module — os
# ──────────────────────────────────────────────────────────────

import os

print()
print("=" * 55)
print("4. THE os MODULE (Operating System interaction)")
print("=" * 55)

# Current working directory
print(f"  Current directory: {os.getcwd()}")

# Check if a file exists
print(f"  'function.py' exists? {os.path.exists('function.py')}")

# List files in current directory
files = os.listdir(".")
print(f"  Files here: {files[:5]}...")  # Show first 5

# Get the size of a file
if os.path.exists("function.py"):
    size = os.path.getsize("function.py")
    print(f"  'function.py' size: {size} bytes")

# Join paths safely (works on Windows + Mac + Linux)
path = os.path.join("week_3", "function.py")
print(f"  Joined path: {path}")


# ──────────────────────────────────────────────────────────────
# SECTION 5: Different Ways to Import
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("5. IMPORT STYLES")
print("=" * 55)

# Style 1: import the whole module
#   import math
#   math.sqrt(16)     ← must use "math." prefix

# Style 2: import specific items
#   from math import sqrt, pi
#   sqrt(16)          ← no prefix needed
#   pi                ← directly accessible

# Style 3: import with an alias (nickname)
#   import datetime as dt
#   dt.datetime.now()

# Style 4: import everything (NOT recommended — pollutes namespace)
#   from math import *
#   sqrt(16)          ← works but you don't know where sqrt came from

# Let's demonstrate Style 2 and 3:
from math import sqrt, pi
print(f"  sqrt(25)  = {sqrt(25)}")   # No "math." prefix needed
print(f"  pi        = {pi:.4f}")

import statistics as stats
data = [10, 20, 30, 40, 50]
print(f"  mean({data})   = {stats.mean(data)}")
print(f"  median({data}) = {stats.median(data)}")
print(f"  stdev({data})  = {stats.stdev(data):.2f}")


# ──────────────────────────────────────────────────────────────
# SECTION 6: Importing YOUR OWN Module
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("6. IMPORTING YOUR OWN MODULE")
print("=" * 55)

# The file 'function.py' in this same folder IS a module!
# You can import it by its filename (without .py):
#
#   import function
#   print(function.add(2, 3))        → 5
#   print(function.subtract(5, 3))   → 2
#   print(function.multiply(4, 6))   → 24
#
# Or import specific functions:
#   from function import add, multiply
#   print(add(10, 20))               → 30

# ⚠️  We're not running the import here to avoid re-executing
# all the print statements in function.py. In a real project,
# you'd structure your modules with:
#
#   if __name__ == "__main__":
#       # Code here only runs when the file is executed directly.
#       # It does NOT run when the file is imported as a module.
#       print(add(2, 3))

print("""
  To import function.py:
    import function
    function.add(2, 3)        → 5
    function.subtract(5, 3)   → 2
    function.multiply(4, 6)   → 24

  To import just what you need:
    from function import add, multiply
    add(10, 20)               → 30
""")


# ──────────────────────────────────────────────────────────────
# SECTION 7: The __name__ == "__main__" Guard
# ──────────────────────────────────────────────────────────────

print("=" * 55)
print("7. THE __name__ GUARD")
print("=" * 55)

# When Python runs a file directly, __name__ is set to "__main__".
# When a file is imported, __name__ is set to the module name.
#
# This lets you write code that ONLY runs when the file is
# executed directly — not when it's imported.

print(f"  This file's __name__ = '{__name__}'")
# If you run this file directly: __name__ = '__main__'
# If you import this file:      __name__ = 'module'

print("""
  HOW TO USE IT:

  # In function.py, add this at the bottom:
  if __name__ == "__main__":
      # This code runs ONLY when you do: python function.py
      # It does NOT run when you do: import function
      print(add(2, 3))
      print(multiply(4, 6))
""")


# ──────────────────────────────────────────────────────────────
# SECTION 8: Installing Third-Party Modules (pip)
# ──────────────────────────────────────────────────────────────

print("=" * 55)
print("8. INSTALLING PACKAGES WITH pip")
print("=" * 55)

print("""
  Python's package manager is called 'pip'.
  It downloads modules from PyPI (Python Package Index).

  Common commands:
    pip install requests        → install a package
    pip install flask           → install Flask web framework
    pip uninstall requests      → remove a package
    pip list                    → see all installed packages
    pip freeze > requirements.txt → save dependencies to a file

  Popular third-party packages:
    📦 requests   — make HTTP requests (call APIs)
    📦 flask      — build web applications
    📦 django     — full-featured web framework
    📦 pandas     — data analysis & manipulation
    📦 numpy      — numerical computing
    📦 matplotlib — create charts and graphs
    📦 pillow     — image processing
""")


# ──────────────────────────────────────────────────────────────
# SECTION 9: Useful Built-in Modules — Quick Reference
# ──────────────────────────────────────────────────────────────

print("=" * 55)
print("9. USEFUL BUILT-IN MODULES — CHEAT SHEET")
print("=" * 55)

# Let's demo a few more handy modules:

# --- string module ---
import string
print(f"  Alphabet:    {string.ascii_lowercase}")
print(f"  Uppercase:   {string.ascii_uppercase}")
print(f"  Digits:      {string.digits}")
print(f"  Punctuation: {string.punctuation}")

# --- json module (working with JSON data) ---
import json

student = {"name": "Musa", "age": 20, "courses": ["Python", "Web Dev"]}

# Convert Python dict → JSON string
json_string = json.dumps(student, indent=2)
print(f"\n  Python → JSON:\n{json_string}")

# Convert JSON string → Python dict
parsed = json.loads(json_string)
print(f"  JSON → Python: {parsed['name']}, age {parsed['age']}")

# --- sys module ---
import sys
print(f"\n  Python version: {sys.version}")
print(f"  Platform:       {sys.platform}")


# ──────────────────────────────────────────────────────────────
# SUMMARY
# ──────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("         MODULES — KEY TAKEAWAYS")
print("=" * 55)
print("""
  ✅ import module               — import entire module
  ✅ from module import item     — import specific item(s)
  ✅ import module as alias      — give it a short name
  ✅ Your .py files ARE modules  — import them the same way
  ✅ __name__ == "__main__"      — guard code from running on import
  ✅ pip install package_name    — install third-party packages
  ✅ Standard Library has 200+ modules — math, random, datetime, os, json ...
""")
