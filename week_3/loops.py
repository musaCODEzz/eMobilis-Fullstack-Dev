# ============================================================
# Week 3 - Python Basics: Loops
# ============================================================
# Loops let you REPEAT a block of code multiple times.
# Python has two types: while loop and for loop.

print("=" * 50)
print("1. WHILE LOOP — repeats WHILE a condition is True")
print("=" * 50)
# Syntax:
#   while condition:
#       body

number = 10
while number > 0:
    print(f"Countdown: {number}")
    number -= 1
print("🚀 Liftoff!")

print()
# Classic while loop — ask until valid input
print("--- Guessing game (while loop) ---")
secret = 7
guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")

print(f"✅ Correct! You got it in {attempts} attempt(s).")

print()
print("=" * 50)
print("2. FOR LOOP — iterates over a sequence")
print("=" * 50)
# Syntax:
#   for variable in sequence:
#       body

# Loop over a range of numbers
print("--- range(5) ---")
for i in range(5):
    print(i, end=" ")
print()  # new line

# range(start, stop, step)
print("--- range(1, 11) →  1 to 10 ---")
for i in range(1, 11):
    print(i, end=" ")
print()

print("--- range(0, 21, 2) → even numbers ---")
for i in range(0, 21, 2):
    print(i, end=" ")
print()

print("--- range(10, 0, -1) → countdown ---")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

print()
print("--- Looping over a LIST ---")
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(f"  🍓 {fruit}")

print()
print("--- Looping over a STRING ---")
for char in "Python":
    print(char, end="-")
print()

print()
print("--- Looping over a DICTIONARY ---")
student = {"name": "Musa", "age": 20, "course": "Fullstack"}
for key, value in student.items():
    print(f"  {key}: {value}")

print()
print("--- enumerate() — get index AND value ---")
colours = ["red", "green", "blue"]
for index, colour in enumerate(colours):
    print(f"  [{index}] {colour}")

print()
print("--- zip() — loop over two lists together ---")
names  = ["Alice", "Bob", "Carol"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"  {name} scored {score}")

print()
print("=" * 50)
print("3. NESTED LOOPS — a loop inside a loop")
print("=" * 50)

print("--- Multiplication table (3x3) ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="   ")
    print()

print()
print("--- Printing a triangle pattern ---")
for row in range(1, 6):
    print("*" * row)

print()
print("=" * 50)
print("4. LOOP CONTROL STATEMENTS")
print("=" * 50)

# break — exit the loop early
print("--- break: stop when 5 is found ---")
for num in range(1, 11):
    if num == 5:
        print(f"Found 5! Breaking out.")
        break
    print(num, end=" ")
print()

# continue — skip current iteration
print("--- continue: skip even numbers ---")
for num in range(1, 11):
    if num % 2 == 0:
        continue        # jump to next iteration
    print(num, end=" ")
print()

# pass — placeholder (do nothing)
print("--- pass: placeholder for future code ---")
for num in range(5):
    if num == 3:
        pass            # TODO: handle this case later
    else:
        print(num, end=" ")
print()

print()
print("=" * 50)
print("5. for-else / while-else")
print("=" * 50)
# The else block runs if the loop COMPLETES without hitting break.

numbers = [1, 3, 5, 7, 9]
target = 6

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} was NOT found in the list.")

print()
print("=" * 50)
print("6. LIST COMPREHENSION (compact for loop)")
print("=" * 50)
# A concise way to build a list using a for loop in one line.

# Without comprehension:
squares_normal = []
for n in range(1, 6):
    squares_normal.append(n ** 2)
print("Normal:", squares_normal)

# With comprehension:
squares_comp = [n ** 2 for n in range(1, 6)]
print("Comprehension:", squares_comp)

# With a condition:
even_squares = [n ** 2 for n in range(1, 11) if n % 2 == 0]
print("Even squares:", even_squares)

# Convert all strings to uppercase in one line:
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print("Uppercase:", upper_words)
