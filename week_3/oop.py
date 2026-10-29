# ============================================================
# Week 3 - Python Basics: Object-Oriented Programming (OOP)
# ============================================================
# OOP is a way of organising code around OBJECTS and CLASSES
# instead of just functions and logic.
#
# Think of it like this:
#   📐 A CLASS is a BLUEPRINT (e.g. a car design)
#   🚗 An OBJECT is a real thing built from that blueprint (e.g. your car)
#
# The 5 main OOP concepts are:
#   1. Classes & Objects  — blueprints and instances
#   2. Encapsulation      — protecting internal data
#   3. Inheritance        — child classes reuse parent code
#   4. Polymorphism       — same method name, different behaviour
#   5. Abstraction        — hide complexity, show essentials
# ============================================================


# ══════════════════════════════════════════════════════════════
# 1. CLASSES & OBJECTS
# ══════════════════════════════════════════════════════════════

print("=" * 55)
print("1. CLASSES & OBJECTS")
print("=" * 55)

# A class groups DATA (attributes) and BEHAVIOUR (methods) together.
# __init__ is the CONSTRUCTOR — it runs automatically when you
# create a new object. 'self' refers to the current object.

class Employee:
    """Represents an employee in a company."""

    def __init__(self, name, position, salary):
        # These are INSTANCE ATTRIBUTES — unique to each object
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        """Print the employee's details."""
        print(f"  👤 {self.name} | {self.position} | Ksh {self.salary:,.2f}")

    def give_raise(self, amount):
        """Increase the employee's salary."""
        self.salary += amount
        print(f"  💰 {self.name} got a raise! New salary: Ksh {self.salary:,.2f}")

# Create objects (instances) of the Employee class
emp1 = Employee("Alice", "Software Engineer", 120000)
emp2 = Employee("Bob", "Designer", 95000)
emp3 = Employee("Musa", "Fullstack Developer", 110000)

emp1.display_info()
emp2.display_info()
emp3.display_info()
emp3.give_raise(15000)

# You can access attributes directly too
print(f"  emp1.name = {emp1.name}")
print(f"  emp1.salary = {emp1.salary}")

# Modify an attribute directly
emp1.position = "Senior Software Engineer"
emp1.display_info()


# ══════════════════════════════════════════════════════════════
# 1b. CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES
# ══════════════════════════════════════════════════════════════

print()
print("=" * 55)
print("1b. CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES")
print("=" * 55)

class Student:
    """Represents a student at eMobilis."""

    # CLASS ATTRIBUTE — shared by ALL students
    school = "eMobilis Academy"
    student_count = 0

    def __init__(self, name, course):
        # INSTANCE ATTRIBUTES — unique to each student
        self.name = name
        self.course = course
        Student.student_count += 1   # Increment shared counter

    def display(self):
        print(f"  🎓 {self.name} studying {self.course} at {Student.school}")

s1 = Student("Musa", "Fullstack Development")
s2 = Student("Alice", "Data Science")
s3 = Student("Bob", "Cyber Security")

s1.display()
s2.display()
s3.display()

# The class attribute is shared — access it via the class name
print(f"  Total students enrolled: {Student.student_count}")
print(f"  School name: {Student.school}")


# ══════════════════════════════════════════════════════════════
# 2. ENCAPSULATION (Data Protection)
# ══════════════════════════════════════════════════════════════

print()
print("=" * 55)
print("2. ENCAPSULATION — Protecting Data")
print("=" * 55)

# Encapsulation means HIDING internal data so it can't be
# changed carelessly from outside. In Python:
#   self.name       → public    (accessible anywhere)
#   self._name      → protected (convention: "don't touch")
#   self.__name     → private   (name-mangled, harder to access)

class BankAccount:
    """A bank account with protected balance."""

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance   # PRIVATE — cannot be accessed directly

    def deposit(self, amount):
        """Add money to the account."""
        if amount <= 0:
            print("  ❌ Deposit amount must be positive!")
            return
        self.__balance += amount
        print(f"  ✅ Deposited Ksh {amount:,.2f}. Balance: Ksh {self.__balance:,.2f}")

    def withdraw(self, amount):
        """Remove money from the account (with checks)."""
        if amount <= 0:
            print("  ❌ Withdrawal amount must be positive!")
            return
        if amount > self.__balance:
            print(f"  ❌ Insufficient funds! Balance: Ksh {self.__balance:,.2f}")
            return
        self.__balance -= amount
        print(f"  ✅ Withdrew Ksh {amount:,.2f}. Balance: Ksh {self.__balance:,.2f}")

    def get_balance(self):
        """Getter — the SAFE way to read the balance."""
        return self.__balance

    def __str__(self):
        """String representation of the account."""
        return f"Account({self.owner}, #{self.account_number}, Ksh {self.__balance:,.2f})"

# Using the BankAccount
print("  --- Musa's Bank Account ---")
account = BankAccount("Musa", "001-234-567", 5000)
account.deposit(3000)           # +3000 → 8000
account.withdraw(2000)          # -2000 → 6000
account.deposit(500)            # +500  → 6500
account.withdraw(10000)         # ❌ Insufficient
print(f"  Current balance: Ksh {account.get_balance():,.2f}")
print(f"  Account: {account}")  # Uses __str__

# Trying to access __balance directly FAILS:
# print(account.__balance)  # ❌ AttributeError!
# You CAN bypass it with name mangling, but you SHOULDN'T:
# print(account._BankAccount__balance)  # Works but is bad practice


# ══════════════════════════════════════════════════════════════
# 3. INHERITANCE (Parent → Child)
# ══════════════════════════════════════════════════════════════

print()
print("=" * 55)
print("3. INHERITANCE — Reusing Code from Parent Classes")
print("=" * 55)

# Inheritance lets a CHILD class get all the attributes and
# methods of a PARENT class, then ADD or OVERRIDE them.
#
# Real-world analogy:
#   Person → Student (a student IS a person with extra features)

class Person:
    """Base class for all people."""

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        """Show person details."""
        print(f"  👤 {self.name} | Age: {self.age} | Gender: {self.gender}")

    def greet(self):
        print(f"  Hi, I'm {self.name}! 👋")


class StudentPerson(Person):
    """A student inherits from Person and adds student-specific features."""

    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)  # Call parent's __init__
        self.student_id = student_id
        self.course = course
        self.grades = []

    def display_info(self):
        """OVERRIDE parent's method to include student details."""
        super().display_info()   # Call parent's version first
        print(f"       Student ID: {self.student_id} | Course: {self.course}")
        if self.grades:
            avg = sum(self.grades) / len(self.grades)
            print(f"       Grades: {self.grades} | Average: {avg:.1f}")

    def add_grade(self, grade):
        """Add a grade to the student's record."""
        self.grades.append(grade)
        print(f"  📝 Added grade {grade} for {self.name}")


class Teacher(Person):
    """A teacher inherits from Person and adds teacher-specific features."""

    def __init__(self, name, age, gender, subject, years_experience):
        super().__init__(name, age, gender)
        self.subject = subject
        self.years_experience = years_experience

    def display_info(self):
        super().display_info()
        print(f"       Teaches: {self.subject} | Experience: {self.years_experience} years")


# Create instances
print("  --- Student ---")
student = StudentPerson("Musa", 20, "Male", "EM-2024-001", "Fullstack")
student.greet()                  # Inherited from Person
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
student.display_info()           # Overridden to show student extras

print()
print("  --- Teacher ---")
teacher = Teacher("Dr. Amina", 35, "Female", "Python", 8)
teacher.greet()                  # Inherited from Person
teacher.display_info()

# Check inheritance
print(f"\n  Is student a Person? {isinstance(student, Person)}")        # True
print(f"  Is teacher a Person? {isinstance(teacher, Person)}")          # True
print(f"  Is student a Teacher? {isinstance(student, Teacher)}")        # False


# ══════════════════════════════════════════════════════════════
# 4. POLYMORPHISM (Same Name, Different Behaviour)
# ══════════════════════════════════════════════════════════════

print()
print("=" * 55)
print("4. POLYMORPHISM — Same Method, Different Behaviour")
print("=" * 55)

# "Poly" = many, "morph" = forms.
# Different classes can have the SAME method name but behave
# DIFFERENTLY. This lets you write flexible code.

class Animal:
    """Base class for all animals."""
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Each animal speaks differently — to be overridden."""
        return "..."

    def info(self):
        return f"{self.name} says: {self.speak()}"

class Dog(Animal):
    def speak(self):
        return "Woof! 🐕"

class Cat(Animal):
    def speak(self):
        return "Meow! 🐱"

class Cow(Animal):
    def speak(self):
        return "Moo! 🐄"

class Duck(Animal):
    def speak(self):
        return "Quack! 🦆"

# Create a list of different animals
animals = [Dog("Rex"), Cat("Whiskers"), Cow("Bessie"), Duck("Donald")]

# The SAME code works for ALL of them — that's polymorphism!
for animal in animals:
    print(f"  {animal.info()}")

# This is powerful because you can add new animals (e.g. Parrot)
# WITHOUT changing the loop above.


# ══════════════════════════════════════════════════════════════
# 5. ABSTRACTION (Hide Complexity, Show Essentials)
# ══════════════════════════════════════════════════════════════

print()
print("=" * 55)
print("5. ABSTRACTION — Hide the Details")
print("=" * 55)

# Abstraction means showing WHAT an object does, not HOW.
# Like driving a car: you use the steering wheel and pedals,
# but you don't need to understand the engine internals.
#
# In Python, we use the abc module for abstract classes.

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class for shapes.
    You CANNOT create a Shape() directly — you must create
    a specific shape like Circle or Rectangle.
    """

    @abstractmethod
    def area(self):
        """Calculate the area (must be implemented by subclasses)."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter (must be implemented by subclasses)."""
        pass

    def describe(self):
        """Non-abstract method — inherited by all shapes."""
        print(f"  📐 {self.__class__.__name__}: "
              f"Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, base, height, side_a, side_b, side_c):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


# Create shapes and use polymorphism + abstraction together
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 3, 4, 5),
]

for shape in shapes:
    shape.describe()

# Trying to create Shape() directly would fail:
# shape = Shape()  # ❌ TypeError: Can't instantiate abstract class


# ══════════════════════════════════════════════════════════════
# 6. SPECIAL (DUNDER) METHODS
# ══════════════════════════════════════════════════════════════

print()
print("=" * 55)
print("6. SPECIAL METHODS (Dunder Methods)")
print("=" * 55)

# "Dunder" = Double UNDERscore. These methods let your objects
# work with Python's built-in operations (+, -, print, len, ==, etc.)

class Product:
    """Represents a product in an online shop."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """What print() shows — human-readable."""
        return f"{self.name}: Ksh {self.price:,.2f} × {self.quantity}"

    def __repr__(self):
        """What the developer sees — for debugging."""
        return f"Product('{self.name}', {self.price}, {self.quantity})"

    def __len__(self):
        """Let len() work on our object."""
        return self.quantity

    def __eq__(self, other):
        """Let == compare two products by name."""
        return self.name == other.name

    def __add__(self, other):
        """Let + combine quantities of the same product."""
        if self.name != other.name:
            raise ValueError("Cannot add different products!")
        return Product(self.name, self.price, self.quantity + other.quantity)

    def total_value(self):
        return self.price * self.quantity

# Demo
p1 = Product("Laptop", 85000, 3)
p2 = Product("Laptop", 85000, 2)
p3 = Product("Phone", 45000, 5)

print(f"  {p1}")                     # Uses __str__
print(f"  repr: {repr(p1)}")         # Uses __repr__
print(f"  len(p1) = {len(p1)}")      # Uses __len__  → 3
print(f"  p1 == p2? {p1 == p2}")     # Uses __eq__   → True  (same name)
print(f"  p1 == p3? {p1 == p3}")     # Uses __eq__   → False

combined = p1 + p2                   # Uses __add__
print(f"  p1 + p2 = {combined}")     # Laptop: Ksh 85,000 × 5
print(f"  Total value: Ksh {combined.total_value():,.2f}")


# ══════════════════════════════════════════════════════════════
# 7. REAL-WORLD EXAMPLE: Library Management System
# ══════════════════════════════════════════════════════════════

print()
print("=" * 55)
print("7. REAL-WORLD EXAMPLE — Library System")
print("=" * 55)

class Book:
    """Represents a book in the library."""

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrower = None

    def __str__(self):
        status = "📖 Available" if not self.is_borrowed else f"🔒 Borrowed by {self.borrower}"
        return f"  '{self.title}' by {self.author} [{status}]"


class Library:
    """Manages a collection of books."""

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        print(f"  📚 Added: '{book.title}' by {book.author}")

    def display_books(self):
        """Show all books in the library."""
        print(f"\n  ══ {self.name} — Catalogue ({len(self.books)} books) ══")
        for book in self.books:
            print(book)

    def borrow_book(self, title, borrower):
        """Borrow a book by title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print(f"  ❌ '{title}' is already borrowed by {book.borrower}")
                    return
                book.is_borrowed = True
                book.borrower = borrower
                print(f"  ✅ {borrower} borrowed '{title}'")
                return
        print(f"  ❌ Book '{title}' not found in library")

    def return_book(self, title):
        """Return a borrowed book."""
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    print(f"  ⚠️  '{title}' was not borrowed")
                    return
                borrower = book.borrower
                book.is_borrowed = False
                book.borrower = None
                print(f"  ✅ '{title}' returned by {borrower}")
                return
        print(f"  ❌ Book '{title}' not found")


# Build our library
lib = Library("eMobilis Library")

lib.add_book(Book("Python Crash Course", "Eric Matthes", "978-1593279"))
lib.add_book(Book("Clean Code", "Robert C. Martin", "978-0132350"))
lib.add_book(Book("The Pragmatic Programmer", "Hunt & Thomas", "978-0135957"))

lib.display_books()

lib.borrow_book("Clean Code", "Musa")
lib.borrow_book("Clean Code", "Alice")     # Already borrowed
lib.return_book("Clean Code")
lib.borrow_book("Clean Code", "Alice")     # Now available

lib.display_books()


# ══════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════

print()
print("=" * 55)
print("         OOP — KEY TAKEAWAYS")
print("=" * 55)
print("""
  ✅ CLASS = blueprint        OBJECT = instance of a class
  ✅ __init__()               — constructor, runs on creation
  ✅ self                     — refers to the current object
  ✅ Encapsulation            — protect data with __private
  ✅ Inheritance              — child reuses parent's code
  ✅ super()                  — call the parent's methods
  ✅ Polymorphism             — same method name, different behaviour
  ✅ Abstraction (ABC)        — force subclasses to implement methods
  ✅ Dunder methods           — __str__, __add__, __eq__, __len__
  ✅ isinstance(obj, Class)   — check if an object is of a type
""")
