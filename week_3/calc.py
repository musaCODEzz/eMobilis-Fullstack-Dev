# ============================================================
# Week 3 - Python Project: Arithmetic Calculator
# ============================================================
# This is a fully-featured calculator that demonstrates:
#   ✅ Functions with return values
#   ✅ User input handling
#   ✅ Error handling (try/except)
#   ✅ Loops (run multiple calculations)
#   ✅ match/if-elif for branching logic
#   ✅ Formatted output
#
# Run it:  python calc.py
# ============================================================


# ──────────────────────────────────────────────────────────────
# SECTION 1: Core Arithmetic Functions
# ──────────────────────────────────────────────────────────────
# Each function takes two numbers and returns a result
# rounded to 2 decimal places. Keeping logic in functions
# makes the code reusable and easy to test.

def add(x, y):
    """Return the sum of x and y, rounded to 2 decimal places."""
    return round(x + y, 2)

def subtract(x, y):
    """Return the difference of x and y."""
    return round(x - y, 2)

def multiply(x, y):
    """Return the product of x and y."""
    return round(x * y, 2)

def divide(x, y):
    """
    Return x divided by y.
    Returns None and prints an error if y is zero.
    """
    if y == 0:
        print("  ❌ Error: Division by zero is not allowed.")
        return None
    return round(x / y, 2)


# ──────────────────────────────────────────────────────────────
# SECTION 2: Advanced Arithmetic Functions
# ──────────────────────────────────────────────────────────────
# Let's add more operations to make this a complete calculator.

def power(x, y):
    """Return x raised to the power of y (x^y)."""
    return round(x ** y, 2)

def modulus(x, y):
    """
    Return the remainder of x divided by y.
    Example: 10 % 3 = 1 (because 10 = 3×3 + 1)
    """
    if y == 0:
        print("  ❌ Error: Modulus by zero is not allowed.")
        return None
    return round(x % y, 2)

def floor_divide(x, y):
    """
    Return x divided by y, rounded DOWN to the nearest integer.
    Example: 7 // 2 = 3 (not 3.5)
    """
    if y == 0:
        print("  ❌ Error: Division by zero is not allowed.")
        return None
    return x // y

def percentage(x, y):
    """
    Return what percentage x is of y.
    Example: percentage(25, 200) → 12.5%  (25 is 12.5% of 200)
    """
    if y == 0:
        print("  ❌ Error: Cannot calculate percentage of zero.")
        return None
    return round((x / y) * 100, 2)

def square_root(x):
    """
    Return the square root of x.
    Example: √16 = 4.0
    """
    if x < 0:
        print("  ❌ Error: Cannot calculate square root of a negative number.")
        return None
    return round(x ** 0.5, 2)


# ──────────────────────────────────────────────────────────────
# SECTION 3: Calculation History
# ──────────────────────────────────────────────────────────────
# We store every calculation so the user can review them later.
# This demonstrates using a LIST to accumulate data.

history = []   # Each entry is a string like "10 + 5 = 15"

def add_to_history(entry):
    """Store a calculation result in history."""
    history.append(entry)

def show_history():
    """Display all past calculations."""
    if not history:
        print("\n  📋 No calculations yet.")
        return
    print(f"\n  📋 Calculation History ({len(history)} entries):")
    print("  " + "─" * 40)
    for i, entry in enumerate(history, start=1):
        print(f"  {i:3}. {entry}")
    print("  " + "─" * 40)

def clear_history():
    """Clear all stored calculations."""
    history.clear()
    print("  🗑️  History cleared.")


# ──────────────────────────────────────────────────────────────
# SECTION 4: Helper Functions
# ──────────────────────────────────────────────────────────────

def get_number(prompt):
    """
    Safely get a number from the user.
    Keeps asking until a valid number is entered.
    This prevents the program from crashing on bad input.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠️  That's not a valid number. Try again.")

def display_menu():
    """Show the calculator menu."""
    print()
    print("  ╔══════════════════════════════════════╗")
    print("  ║      🧮  PYTHON CALCULATOR  🧮       ║")
    print("  ╠══════════════════════════════════════╣")
    print("  ║  +   Addition                       ║")
    print("  ║  -   Subtraction                    ║")
    print("  ║  *   Multiplication                 ║")
    print("  ║  /   Division                       ║")
    print("  ║  **  Power (x^y)                    ║")
    print("  ║  %   Modulus (remainder)            ║")
    print("  ║  //  Floor Division                 ║")
    print("  ║  %%  Percentage (x is what % of y)  ║")
    print("  ║  √   Square Root                    ║")
    print("  ║  h   Show History                   ║")
    print("  ║  c   Clear History                  ║")
    print("  ║  q   Quit                           ║")
    print("  ╚══════════════════════════════════════╝")


# ──────────────────────────────────────────────────────────────
# SECTION 5: Main Calculator Loop
# ──────────────────────────────────────────────────────────────
# The calculator runs in a loop so the user can perform
# multiple calculations without restarting the program.

def run_calculator():
    """Main function that drives the calculator."""

    print()
    print("  " + "=" * 40)
    print("  Welcome to the Python Calculator! 🧮")
    print("  Type 'q' to quit at any time.")
    print("  " + "=" * 40)

    while True:
        display_menu()
        operator = input("\n  Enter operator: ").strip()

        # ── Quit ──
        if operator.lower() == "q":
            print(f"\n  👋 Goodbye! You made {len(history)} calculation(s).")
            if history:
                show_history()
            break

        # ── History ──
        if operator.lower() == "h":
            show_history()
            continue

        # ── Clear History ──
        if operator.lower() == "c":
            clear_history()
            continue

        # ── Square Root (only needs one number) ──
        if operator == "√" or operator.lower() == "sqrt":
            x = get_number("  Enter the number: ")
            result = square_root(x)
            if result is not None:
                entry = f"√{x} = {result}"
                print(f"\n  ✅ {entry}")
                add_to_history(entry)
            continue

        # ── Two-number operations ──
        valid_operators = ["+", "-", "*", "/", "**", "%", "//", "%%"]
        if operator not in valid_operators:
            print("  ❌ Invalid operator. Please pick from the menu.")
            continue

        x = get_number("  Enter first number: ")
        y = get_number("  Enter second number: ")

        # Perform the calculation
        result = None
        display_op = operator   # What we show in the output

        if operator == "+":
            result = add(x, y)
        elif operator == "-":
            result = subtract(x, y)
        elif operator == "*":
            result = multiply(x, y)
        elif operator == "/":
            result = divide(x, y)
        elif operator == "**":
            result = power(x, y)
            display_op = "^"
        elif operator == "%":
            result = modulus(x, y)
        elif operator == "//":
            result = floor_divide(x, y)
        elif operator == "%%":
            result = percentage(x, y)
            if result is not None:
                entry = f"{x} is {result}% of {y}"
                print(f"\n  ✅ {entry}")
                add_to_history(entry)
                continue

        # Display and store the result
        if result is not None:
            entry = f"{x} {display_op} {y} = {result}"
            print(f"\n  ✅ {entry}")
            add_to_history(entry)


# ──────────────────────────────────────────────────────────────
# SECTION 6: Run the Program
# ──────────────────────────────────────────────────────────────
# The __name__ guard ensures this code runs ONLY when you
# execute this file directly (python calc.py), NOT when you
# import it as a module.

if __name__ == "__main__":
    run_calculator()


# ──────────────────────────────────────────────────────────────
# QUICK TEST EXAMPLES (for learning / reference)
# ──────────────────────────────────────────────────────────────
# You can also use these functions directly in another file:
#
#   from calc import add, subtract, multiply, divide
#
#   print(add(10, 5))           # 15
#   print(subtract(10, 5))      # 5
#   print(multiply(10, 5))      # 50
#   print(divide(10, 5))        # 2.0
#   print(divide(10, 0))        # Error + None
#   print(power(2, 10))         # 1024
#   print(modulus(10, 3))       # 1
#   print(floor_divide(7, 2))   # 3
#   print(percentage(25, 200))  # 12.5
#   print(square_root(144))     # 12.0
