# ============================================================
# Week 3 - Python Basics: Operators
# ============================================================
# Operators are symbols that perform operations on values
# (called operands). Python has 7 categories of operators.

print("=" * 50)
print("1. ARITHMETIC OPERATORS")
print("=" * 50)

x = 10
y = 3

print(f"{x} + {y}  = {x + y}")   # Addition        → 13
print(f"{x} - {y}  = {x - y}")   # Subtraction     → 7
print(f"{x} * {y}  = {x * y}")   # Multiplication  → 30
print(f"{x} / {y}  = {x / y}")   # Division        → 3.333 (always float)
print(f"{x} % {y}  = {x % y}")   # Modulus (remainder) → 1
print(f"{x} ** {y} = {x ** y}")  # Exponentiation  → 1000
print(f"{x} // {y} = {x // y}")  # Floor division  → 3 (rounds down)

# Real-world use of modulus: check if a number is even/odd
number = 17
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

print()
print("=" * 50)
print("2. COMPARISON / RELATIONAL OPERATORS")
print("=" * 50)
# These always return True or False

a = 10
b = 5

print(f"{a} > {b}   →", a > b)    # Greater than        → True
print(f"{a} < {b}   →", a < b)    # Less than           → False
print(f"{a} == {b}  →", a == b)   # Equal to            → False
print(f"{a} != {b}  →", a != b)   # Not equal           → True
print(f"{a} >= {b}  →", a >= b)   # Greater or equal    → True
print(f"{a} <= {b}  →", a <= b)   # Less or equal       → False

# NOTE: = is assignment, == is comparison!
x = 5       # assigns 5 to x
print(x == 5)   # True — checks if x equals 5

print()
print("=" * 50)
print("3. LOGICAL OPERATORS")
print("=" * 50)
# Combine multiple boolean expressions

p = True
q = False

print(f"True  and False → {p and q}")  # Both must be True → False
print(f"True  or  False → {p or q}")   # At least one True → True
print(f"not   True      → {not p}")    # Reverses the value → False

# Practical example
age = 20
has_id = True
if age >= 18 and has_id:
    print("Access granted!")
else:
    print("Access denied.")

# Short-circuit evaluation
# Python stops evaluating as soon as the result is known
print(False and print("this won't run"))  # 'and' stops at False
print(True  or  print("this won't run")) # 'or'  stops at True

print()
print("=" * 50)
print("4. ASSIGNMENT OPERATORS")
print("=" * 50)

x = 10
print(f"Initial x = {x}")

x += 5;  print(f"x += 5  → {x}")   # x = x + 5 → 15
x -= 3;  print(f"x -= 3  → {x}")   # x = x - 3 → 12
x *= 2;  print(f"x *= 2  → {x}")   # x = x * 2 → 24
x //= 5; print(f"x //= 5 → {x}")   # x = x // 5 → 4
x **= 3; print(f"x **= 3 → {x}")   # x = x ** 3 → 64
x %= 10; print(f"x %%= 10 → {x}")  # x = x % 10 → 4

print()
print("=" * 50)
print("5. BITWISE OPERATORS  (work on binary bits)")
print("=" * 50)

x = 10   # binary: 1010
y = 4    # binary: 0100

print(f"10 & 4  (AND) = {x & y}")    # 0000 → 0
print(f"10 | 4  (OR)  = {x | y}")    # 1110 → 14
print(f"10 ^ 4  (XOR) = {x ^ y}")    # 1110 → 14
print(f"~10     (NOT) = {~x}")        # Flips all bits → -11
print(f"10 << 1 (LEFT SHIFT)  = {x << 1}")   # 10100 → 20
print(f"10 >> 1 (RIGHT SHIFT) = {x >> 1}")   # 0101  → 5

# Why use bitwise? Permission flags, networking, low-level programming.

print()
print("=" * 50)
print("6. IDENTITY OPERATORS  (is / is not)")
print("=" * 50)
# Checks if two variables point to the SAME object in memory.
# Different from == which checks if VALUES are equal.

x = [1, 2, 3]
y = [1, 2, 3]
z = x           # z points to the exact same list as x

print(f"x == y  → {x == y}")     # True  (same values)
print(f"x is y  → {x is y}")     # False (different objects in memory)
print(f"x is z  → {x is z}")     # True  (same object)
print(f"x is not y → {x is not y}")  # True

# Small integers (-5 to 256) are cached, so 'is' can be True
a = 5
b = 5
print(f"a is b (small int) → {a is b}")  # True (Python caches these)

print()
print("=" * 50)
print("7. MEMBERSHIP OPERATORS  (in / not in)")
print("=" * 50)
# Checks if a value exists inside a sequence (list, string, tuple, set)

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)        # True
print("mango" in fruits)        # False
print("mango" not in fruits)    # True

# Works on strings too
email = "musa@gmail.com"
print("@" in email)             # True
print(".com" in email)          # True

# Works on dictionaries (checks KEYS by default)
person = {"name": "Musa", "age": 20}
print("name" in person)         # True
print("email" in person)        # False

print()
print("=" * 50)
print("OPERATOR PRECEDENCE (PEMDAS/BODMAS)")
print("=" * 50)
# Python follows math order of operations:
# () Parentheses → ** Exponentiation → * / // % → + -

result = 2 + 3 * 4 ** 2
print(f"2 + 3 * 4 ** 2 = {result}")   # 2 + 3*16 = 2+48 = 50

result_with_parens = (2 + 3) * (4 ** 2)
print(f"(2+3) * (4**2) = {result_with_parens}")  # 5*16 = 80
