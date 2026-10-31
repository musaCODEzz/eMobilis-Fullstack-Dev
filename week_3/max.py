# ============================================================
# Week 3 - Python Built-in Functions: min(), max() & Friends
# ============================================================
# Python has powerful built-in functions that work on
# collections (lists, tuples, sets) without importing anything.
# This file covers min(), max(), sum(), sorted(), and more.
# ============================================================


# ──────────────────────────────────────────────────────────────
# SECTION 1: max() — Find the LARGEST Value
# ──────────────────────────────────────────────────────────────

print("=" * 55)
print("1. max() — Find the Largest Value")
print("=" * 55)

# max() with a list of numbers
numberArray = [-1.3, -1.4, -10]
print(f"  List:    {numberArray}")
print(f"  max() =  {max(numberArray)}")   # -1.3 (closest to zero)

# max() with positive numbers
scores = [85, 92, 78, 95, 88]
print(f"\n  Scores:  {scores}")
print(f"  Highest: {max(scores)}")        # 95

# max() with individual arguments (no list needed)
print(f"\n  max(10, 20, 30) = {max(10, 20, 30)}")    # 30
print(f"  max(5, -3, 8, 1) = {max(5, -3, 8, 1)}")   # 8

# max() with strings (compares alphabetically / by Unicode)
names = ["Musa", "Alice", "Zara", "Bob"]
print(f"\n  Names: {names}")
print(f"  max()  = {max(names)}")        # Zara (Z comes last)

# max() with a key function — find longest string
print(f"  Longest name: {max(names, key=len)}")   # Alice (5 chars)

# PRACTICAL: Find the student with the highest score
students = [
    {"name": "Musa",  "score": 92},
    {"name": "Alice", "score": 88},
    {"name": "Bob",   "score": 95},
    {"name": "Carol", "score": 91},
]
top_student = max(students, key=lambda s: s["score"])
print(f"\n  🏆 Top student: {top_student['name']} with {top_student['score']}%")


# ──────────────────────────────────────────────────────────────
# SECTION 2: min() — Find the SMALLEST Value
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("2. min() — Find the Smallest Value")
print("=" * 55)

temperatures = [32.5, 28.1, 35.7, 22.3, 30.0]
print(f"  Temperatures: {temperatures}")
print(f"  Coldest:      {min(temperatures)}°C")    # 22.3

prices = [1500, 2300, 850, 4200, 1100]
print(f"\n  Prices: {prices}")
print(f"  Cheapest: Ksh {min(prices):,}")          # 850

# min() with individual arguments
print(f"\n  min(10, 20, 30) = {min(10, 20, 30)}")  # 10

# min() with strings
print(f"  min('z', 'a', 'm') = {min('z', 'a', 'm')}")  # a

# PRACTICAL: Find the youngest person
people = [
    {"name": "Musa", "age": 20},
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 18},
    {"name": "Diana", "age": 25},
]
youngest = min(people, key=lambda p: p["age"])
print(f"\n  👶 Youngest: {youngest['name']} (age {youngest['age']})")


# ──────────────────────────────────────────────────────────────
# SECTION 3: sum() — Add Up All Values
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("3. sum() — Total of All Values")
print("=" * 55)

numbers = [10, 20, 30, 40, 50]
print(f"  Numbers: {numbers}")
print(f"  sum()  = {sum(numbers)}")           # 150

# sum() with a start value (adds to the total)
print(f"  sum() + 100 bonus = {sum(numbers, 100)}")  # 250

# PRACTICAL: Calculate average
grades = [85, 92, 78, 95, 88, 91]
average = sum(grades) / len(grades)
print(f"\n  Grades:  {grades}")
print(f"  Total:   {sum(grades)}")
print(f"  Count:   {len(grades)}")
print(f"  Average: {average:.1f}")

# PRACTICAL: Shopping cart total
cart = [
    {"item": "Laptop",    "price": 85000},
    {"item": "Mouse",     "price": 1500},
    {"item": "Keyboard",  "price": 3500},
    {"item": "Monitor",   "price": 35000},
]
total = sum(item["price"] for item in cart)
print(f"\n  🛒 Shopping Cart Total: Ksh {total:,}")


# ──────────────────────────────────────────────────────────────
# SECTION 4: sorted() — Sort Without Changing the Original
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("4. sorted() — Sort Values")
print("=" * 55)

ages = [25, 18, 32, 21, 28, 19]
print(f"  Original: {ages}")
print(f"  Sorted (asc):  {sorted(ages)}")               # [18, 19, 21, ...]
print(f"  Sorted (desc): {sorted(ages, reverse=True)}")  # [32, 28, 25, ...]
print(f"  Original unchanged: {ages}")  # sorted() does NOT modify the original

# Sort strings
fruits = ["banana", "apple", "cherry", "mango", "elderberry"]
print(f"\n  Fruits: {fruits}")
print(f"  Alphabetical: {sorted(fruits)}")
print(f"  By length:    {sorted(fruits, key=len)}")

# PRACTICAL: Sort students by score (highest first)
students = [("Musa", 92), ("Alice", 88), ("Bob", 95), ("Carol", 80)]
ranked = sorted(students, key=lambda s: s[1], reverse=True)
print(f"\n  🏆 Rankings:")
for rank, (name, score) in enumerate(ranked, start=1):
    medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "  "
    print(f"     {medal} #{rank} {name}: {score}%")


# ──────────────────────────────────────────────────────────────
# SECTION 5: len() — Count Items
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("5. len() — Count Items")
print("=" * 55)

# Works on strings, lists, tuples, dicts, sets
print(f"  len('Hello')           = {len('Hello')}")          # 5
print(f"  len([1, 2, 3])         = {len([1, 2, 3])}")        # 3
print(f"  len((10, 20))          = {len((10, 20))}")          # 2
print(f"  len({{'a':1, 'b':2}})   = {len({'a':1, 'b':2})}")  # 2

# PRACTICAL: Check password length
password = "Musa@2024"
if len(password) >= 8:
    print(f"\n  ✅ Password '{password}' is long enough ({len(password)} chars)")
else:
    print(f"\n  ❌ Password too short ({len(password)} chars, need 8+)")


# ──────────────────────────────────────────────────────────────
# SECTION 6: abs() — Absolute Value (Always Positive)
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("6. abs() — Absolute Value")
print("=" * 55)

print(f"  abs(-10)   = {abs(-10)}")     # 10
print(f"  abs(10)    = {abs(10)}")       # 10
print(f"  abs(-3.14) = {abs(-3.14)}")   # 3.14

# PRACTICAL: Distance between two points (always positive)
point_a = 15
point_b = 42
distance = abs(point_a - point_b)
print(f"\n  Distance between {point_a} and {point_b} = {distance}")

# PRACTICAL: Check if a temperature change is significant
yesterday = 28.5
today = 22.1
change = abs(today - yesterday)
print(f"  Temperature change: {change:.1f}°C", end="")
print(" ⚠️  (big swing!)" if change > 5 else " (normal)")


# ──────────────────────────────────────────────────────────────
# SECTION 7: round() — Round a Number
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("7. round() — Round Numbers")
print("=" * 55)

pi = 3.14159265

print(f"  round(π)       = {round(pi)}")       # 3   (no decimal)
print(f"  round(π, 1)    = {round(pi, 1)}")    # 3.1
print(f"  round(π, 2)    = {round(pi, 2)}")    # 3.14
print(f"  round(π, 4)    = {round(pi, 4)}")    # 3.1416

# Round to nearest 10, 100 using negative digits
print(f"  round(1234, -1) = {round(1234, -1)}")  # 1230
print(f"  round(1234, -2) = {round(1234, -2)}")  # 1200

# PRACTICAL: Formatting prices
price = 49.997
print(f"\n  Raw price: {price}")
print(f"  Rounded:   Ksh {round(price, 2):,.2f}")


# ──────────────────────────────────────────────────────────────
# SECTION 8: enumerate() — Loop with Index
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("8. enumerate() — Loop with Index Numbers")
print("=" * 55)

# Instead of tracking an index manually, use enumerate()
languages = ["Python", "JavaScript", "Java", "C++", "Go"]

# Without enumerate (the old way):
print("  Without enumerate:")
index = 0
for lang in languages:
    print(f"    {index}: {lang}")
    index += 1

# With enumerate (the Python way):
print("\n  With enumerate:")
for index, lang in enumerate(languages):
    print(f"    {index}: {lang}")

# Start counting from 1 instead of 0
print("\n  Starting from 1:")
for i, lang in enumerate(languages, start=1):
    print(f"    {i}. {lang}")


# ──────────────────────────────────────────────────────────────
# SECTION 9: zip() — Combine Two Lists Together
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("9. zip() — Combine Lists Side by Side")
print("=" * 55)

names  = ["Musa", "Alice", "Bob", "Carol"]
scores = [92, 88, 95, 80]
cities = ["Nairobi", "Mombasa", "Kisumu", "Nakuru"]

# Pair names with scores
print("  Names + Scores:")
for name, score in zip(names, scores):
    print(f"    {name}: {score}%")

# Combine three lists
print("\n  Names + Scores + Cities:")
for name, score, city in zip(names, scores, cities):
    print(f"    {name} from {city} scored {score}%")

# Create a dictionary from two lists using zip
student_dict = dict(zip(names, scores))
print(f"\n  As dictionary: {student_dict}")


# ──────────────────────────────────────────────────────────────
# SECTION 10: map() and filter() — Transform & Filter Data
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("10. map() & filter() — Transform and Filter")
print("=" * 55)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() applies a function to EVERY item
squared = list(map(lambda x: x ** 2, numbers))
print(f"  Original: {numbers}")
print(f"  Squared:  {squared}")

doubled = list(map(lambda x: x * 2, numbers))
print(f"  Doubled:  {doubled}")

# filter() keeps items that match a condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\n  Even numbers: {evens}")

odds = list(filter(lambda x: x % 2 != 0, numbers))
print(f"  Odd numbers:  {odds}")

# PRACTICAL: Filter passing grades
all_grades = [45, 82, 33, 91, 67, 55, 78, 40, 95]
passing = list(filter(lambda g: g >= 50, all_grades))
failing = list(filter(lambda g: g < 50, all_grades))
print(f"\n  All grades:   {all_grades}")
print(f"  ✅ Passing:    {passing}")
print(f"  ❌ Failing:    {failing}")


# ──────────────────────────────────────────────────────────────
# SECTION 11: any() and all() — Quick True/False Checks
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("11. any() & all() — Quick True/False Checks")
print("=" * 55)

ages = [25, 17, 30, 15, 22]

# any() — is at least ONE item True?
any_adult = any(age >= 18 for age in ages)
print(f"  Ages: {ages}")
print(f"  Any adult (≥18)?  {any_adult}")    # True

# all() — are ALL items True?
all_adults = all(age >= 18 for age in ages)
print(f"  All adults (≥18)? {all_adults}")   # False

# PRACTICAL: Validate form fields are not empty
form = {"name": "Musa", "email": "musa@email.com", "phone": ""}
all_filled = all(value != "" for value in form.values())
print(f"\n  Form: {form}")
print(f"  All fields filled? {all_filled}")  # False (phone is empty)

empty_fields = [k for k, v in form.items() if v == ""]
if empty_fields:
    print(f"  ⚠️  Missing: {', '.join(empty_fields)}")


# ──────────────────────────────────────────────────────────────
# SECTION 12: Putting It All Together — Data Analysis Example
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("12. PRACTICAL EXAMPLE — Student Report Card")
print("=" * 55)

exam_results = {
    "Musa":  [85, 92, 78, 90, 88],
    "Alice": [91, 87, 95, 82, 89],
    "Bob":   [72, 68, 75, 80, 65],
    "Carol": [55, 48, 62, 40, 58],
}

print(f"\n  {'Student':<10} {'Min':>5} {'Max':>5} {'Avg':>6} {'Total':>6}  Status")
print("  " + "─" * 52)

for student, grades in exam_results.items():
    low    = min(grades)
    high   = max(grades)
    total  = sum(grades)
    avg    = total / len(grades)
    status = "✅ Pass" if avg >= 60 else "❌ Fail"

    print(f"  {student:<10} {low:>5} {high:>5} {avg:>6.1f} {total:>6}  {status}")

# Overall class statistics
all_scores = [s for grades in exam_results.values() for s in grades]
print("  " + "─" * 52)
print(f"  {'CLASS':<10} {min(all_scores):>5} {max(all_scores):>5} "
      f"{sum(all_scores)/len(all_scores):>6.1f} {sum(all_scores):>6}")

pass_count = sum(1 for grades in exam_results.values()
                 if sum(grades)/len(grades) >= 60)
print(f"\n  📊 {pass_count}/{len(exam_results)} students passed "
      f"({pass_count/len(exam_results)*100:.0f}% pass rate)")


# ──────────────────────────────────────────────────────────────
# SUMMARY
# ──────────────────────────────────────────────────────────────

print()
print("=" * 55)
print("    BUILT-IN FUNCTIONS — CHEAT SHEET")
print("=" * 55)
print("""
  max(list)        → largest value
  min(list)        → smallest value
  sum(list)        → total of all values
  len(list)        → number of items
  abs(x)           → positive version of x
  round(x, n)      → round to n decimal places
  sorted(list)     → new sorted list (original unchanged)
  enumerate(list)  → pairs of (index, value)
  zip(a, b)        → pairs of (a[i], b[i])
  map(fn, list)    → apply fn to every item
  filter(fn, list) → keep items where fn returns True
  any(iterable)    → True if at least one item is truthy
  all(iterable)    → True only if ALL items are truthy
""")
