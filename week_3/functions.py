# Lets learn about functions in Python. Functions are blocks of code that perform a specific task and can be reused throughout your program. They help make your code more organized and manageable.


def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
greet("Bob")


def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"The sum is: {result}")


def multiply_numbers(a, b):
    return a * b    

result = multiply_numbers(5, 3)
print(f"The product is: {result}")


def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True

print(is_even(5))  # False


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_number)
        return fib_sequence

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(7))  # True
print(is_prime(10))  # False

def reverse_string(s):
    return s[::-1]

print(reverse_string("Hello, World!"))  # !dlroW ,olleH