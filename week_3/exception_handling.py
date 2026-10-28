# ============================================================
# Week 3 - Python Basics: Exception Handling
# ============================================================
# Errors (exceptions) happen. Exception handling lets your
# program deal with them GRACEFULLY instead of crashing.
#
# SYNTAX:
#   try:
#       # code that might fail
#   except ExceptionType:
#       # runs if that exception occurs
#   else:
#       # runs if NO exception occurred
#   finally:
#       # ALWAYS runs (cleanup code)

print("=" * 50)
print("1. BASIC try-except")
print("=" * 50)

try:
    a = 10
    b = int("0")   # int("0") = 0 at runtime — intentional demo
    c = a / b
    print(c)
except ZeroDivisionError:
    print("❌ Error: You cannot divide by zero!")

print()
print("=" * 50)
print("2. CATCHING MULTIPLE EXCEPTIONS")
print("=" * 50)

def safe_divide(x, y):
    """Divide x by y safely."""
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("❌ ZeroDivisionError: Cannot divide by zero.")
    except TypeError:
        print("❌ TypeError: Both values must be numbers.")
    return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # ZeroDivisionError
print(safe_divide(10, "a")) # TypeError

print()
print("=" * 50)
print("3. try-except-else-finally")
print("=" * 50)

def read_number():
    try:
        num = int(input("Enter a whole number: "))
    except ValueError:
        print("❌ That's not a valid integer!")
    else:
        print(f"✅ Great! You entered {num}. Doubled: {num * 2}")
    finally:
        print("(This always runs — useful for cleanup)")

read_number()

print()
print("=" * 50)
print("4. CATCHING THE EXCEPTION OBJECT (as e)")
print("=" * 50)

try:
    my_list = [1, 2, 3]
    print(my_list[10])   # Index doesn't exist
except IndexError as e:
    print(f"❌ IndexError caught: {e}")

try:
    result = int("not_a_number")
except ValueError as e:
    print(f"❌ ValueError caught: {e}")

print()
print("=" * 50)
print("5. COMMON PYTHON EXCEPTIONS")
print("=" * 50)

exceptions_demo = [
    # (description, callable that raises the exception at runtime)
    ("ZeroDivisionError",  lambda: 1 / int("0")),         # int("0") = 0, avoids static analysis warning
    ("TypeError",          lambda: "2" + 2),
    ("ValueError",         lambda: int("abc")),
    ("IndexError",         lambda: [1, 2, 3][99]),
    ("KeyError",           lambda: {"a": 1}["z"]),
    ("AttributeError",     lambda: (42).upper()),
    ("NameError",          lambda: exec("raise NameError('undefined_variable')")),
]

for name, fn in exceptions_demo:
    try:
        fn()
    except Exception as e:
        print(f"  {name}: {e}")

print()
print("=" * 50)
print("6. RAISING EXCEPTIONS with 'raise'")
print("=" * 50)

def set_age(age):
    """Set a person's age — must be between 0 and 120."""
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0 or age > 120:
        raise ValueError(f"Age must be between 0 and 120, got {age}")
    print(f"✅ Age set to {age}")

try:
    set_age(25)
    set_age(-5)
except ValueError as e:
    print(f"❌ {e}")

try:
    set_age("twenty")
except TypeError as e:
    print(f"❌ {e}")

print()
print("=" * 50)
print("7. CUSTOM EXCEPTION CLASSES")
print("=" * 50)

class InsufficientFundsError(Exception):
    """Raised when a bank account has insufficient funds."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw Ksh {amount:.2f}. Balance is only Ksh {balance:.2f}."
        )

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"✅ Deposited Ksh {amount:.2f}. New balance: Ksh {self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"✅ Withdrew Ksh {amount:.2f}. Remaining: Ksh {self.balance:.2f}")

account = BankAccount("Musa", balance=1000)

try:
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)   # This will fail
except InsufficientFundsError as e:
    print(f"❌ {e}")
except ValueError as e:
    print(f"❌ {e}")

print()
print("=" * 50)
print("8. REAL-WORLD EXAMPLE: Safe file reading")
print("=" * 50)

def read_file(filepath):
    """Safely read a file and return its contents."""
    try:
        with open(filepath, "r") as f:
            content = f.read()
            print(f"✅ File read successfully ({len(content)} chars).")
            return content
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
    except PermissionError:
        print(f"❌ Permission denied: {filepath}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    return None

read_file("hello.py")                  # This file exists
read_file("non_existent_file.txt")     # This will trigger FileNotFoundError

print()
print("=" * 50)
print("SUMMARY — Exception Handling Best Practices")
print("=" * 50)
print("""
  ✅ Always catch SPECIFIC exceptions, not bare 'except:'
  ✅ Use 'finally' for cleanup (closing files, DB connections)
  ✅ Create custom exceptions for your own errors
  ✅ Never silence errors silently — always log or inform the user
  ✅ Use 'raise' to re-raise or create meaningful error messages
""")
