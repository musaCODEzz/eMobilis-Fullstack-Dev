# we want to talk about operators in python
# arithmetic operators
x = 10
y = 5
z = x + y
print(z)

# subtraction
z = x - y
print(z)    

# multiplication
z = x * y
print(z)

# division
z = x / y
print(z)

# modulus
z = x % y
print(z)

# exponentiation
z = x ** y
print(z)    

# floor division
z = x // y
print(z)

# comparison operators
x = 10
y = 5
print(x > y)  # True
print(x < y)  # False
print(x == y)  # False

# not equal
print(x != y)  # True   

# greater than or equal to
print(x >= y)  # True

# less than or equal to
print(x <= y)  # False

# logical operators
x = True
y = False
print(x and y)  # False
print(x or y)  # True
print(not x)  # False   

# bitwise operators
x = 10  # 1010 in binary
y = 4   # 0100 in binary
print(x & y)  # 0000 in binary, which is 0
print(x | y)  # 1110 in binary, which is 14
print(x ^ y)  # 1110 in binary, which is 14
print(~x)     # 11111111111111111111111111110101 in binary, which is -11
print(x << 1)  # 10100 in binary, which is 20
print(x >> 1)  # 0101 in binary, which is 5

# assignment operators
x = 10
x += 5  # equivalent to x = x + 5
print(x)  # 15


# identity operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)  # False
print(x is z)  # True
print(x is not y)  # True

# membership operators
x = [1, 2, 3]
print(1 in x)  # True
print(4 not in x)  # True

#