# ============================================================
# Week 3 - Python Basics: Control Statements (if/elif/else)
# ============================================================
# Control statements let your program make DECISIONS.
# They control which block of code runs based on conditions.

# ----------------------------------------------------------
# SYNTAX:
#   if condition:
#       # runs when condition is True
#   elif another_condition:
#       # runs when first is False but this is True
#   else:
#       # runs when ALL conditions above are False
# ----------------------------------------------------------

print("=" * 50)
print("1. SIMPLE if STATEMENT")
print("=" * 50)

temperature = 35
if temperature > 30:
    print("It's a hot day! Stay hydrated.")

print()
print("=" * 50)
print("2. if-else STATEMENT")
print("=" * 50)

# User input — vote eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote. ✅")
else:
    print("You are NOT eligible to vote yet. ❌")

print()
print("=" * 50)
print("3. if-elif-else (Multiple conditions)")
print("=" * 50)

temperature = float(input("Enter the temperature in Celsius: "))
if temperature > 35:
    print("🔥 It's a very hot day!")
elif temperature > 30:
    print("☀️ It's a hot day.")
elif temperature > 20:
    print("🌤 It's a warm day.")
elif temperature > 10:
    print("🌥 It's a cool day.")
else:
    print("🥶 It's a cold day!")

print()
print("=" * 50)
print("4. NESTED if STATEMENTS")
print("=" * 50)

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("✅ Login successful! Welcome, Admin.")
    else:
        print("❌ Wrong password.")
else:
    print("❌ Username not found.")

print()
print("=" * 50)
print("5. GRADES EXAMPLE (Classic classroom exercise)")
print("=" * 50)

score = int(input("Enter your exam score (0-100): "))

if score >= 90:
    grade = "A"
    remark = "Excellent! 🏆"
elif score >= 80:
    grade = "B"
    remark = "Very Good! 👏"
elif score >= 70:
    grade = "C"
    remark = "Good. Keep improving."
elif score >= 60:
    grade = "D"
    remark = "Average. You can do better!"
elif score >= 0:
    grade = "F"
    remark = "Failed. Please revise and retry."
else:
    grade = "?"
    remark = "Invalid score entered."

print(f"Score: {score} → Grade: {grade} — {remark}")

print()
print("=" * 50)
print("6. ONE-LINE if (Ternary / Conditional Expression)")
print("=" * 50)

number = 8
result = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {result}")

# Ternary with input
x = int(input("Enter a number: "))
print("Positive" if x > 0 else "Negative" if x < 0 else "Zero")

print()
print("=" * 50)
print("7. USING 'in' with if")
print("=" * 50)

day = input("Enter a day of the week: ").capitalize()
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend  = ["Saturday", "Sunday"]

if day in weekdays:
    print(f"{day} is a weekday. Time to work! 💼")
elif day in weekend:
    print(f"{day} is a weekend. Time to relax! 🎉")
else:
    print(f"'{day}' is not a valid day name.")

print()
print("=" * 50)
print("8. if-elif ACTING AS switch/case  (works on ALL Python versions)")
print("=" * 50)
# Python 3.10+ has 'match/case' (like switch in JS/Java).
# Here we achieve the same logic using if-elif so it works on Python 3.9+.

direction = input("Enter direction (north/south/east/west): ").lower()

if direction == "north":
    print("🧭 Going North!")
elif direction == "south":
    print("🧭 Going South!")
elif direction == "east":
    print("🧭 Going East!")
elif direction == "west":
    print("🧭 Going West!")
else:
    print("❌ Unknown direction.")

# NOTE: Python 3.10+ syntax (match/case) — equivalent of the above:
# match direction:
#     case "north": print("Going North!")
#     case "south": print("Going South!")
#     case "east":  print("Going East!")
#     case "west":  print("Going West!")
#     case _:       print("Unknown direction.")
