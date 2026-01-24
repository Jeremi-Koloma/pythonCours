# Fundamental Data Types

# int
print(6)
print(type(6))

# float
print(10.50)
print(type(10.50))

# Math function
print(round(3.2))
print(abs(-20))

# Operator precedente
print(20 - 3 * 2)

# Optional bin
print(bin(5))
print(int("0b101", 2))

# Variable
user_age = 1990
first_job = "Designer"
print(user_age)

# Constants
PI = 13.14

# augmented assignment operator
some_value = 5
some_value = some_value + 2
print(some_value)

# string
print(type("Hi hi !"))
username = "supercoder"
password = "supersecret"
print(username)

multi_line = """
first line
second line
third line
"""
print(multi_line)

# string concatenation
print("Hello " + "Jeremi")

# Type conversion
print(str(100))

# Escape sequence
water = "It 's sunny !"
print(water)

# formatted strings
name = "Jeremi"
print(f"Hi {name}, you are {user_age} years old")

# string indexes
selfish = "01234567"
print(selfish[0])
# [start : stop : stepover]
print(selfish[1:6:2])

# Boolean
is_cool = True
print(is_cool)
print(bool(0))

# List
li = [1, 2, 3, 4, 5]
li2 = ["A", "B", "C", "D"]
li3 = [1, 2, "A", "B", True, 20.0]

# List slicing
amazon_cart = ["notebooks", "sunglasses", "toys", "grapes"]
print(amazon_cart[2:4])

new_cart = amazon_cart[:]  # Copy a list
new_cart[0] = "latop"
print(new_cart)
print(amazon_cart)

# Matrix
matrix = [[1, 5, 1], [0, 1, 0], [1, 0, 1]]
print(matrix[0][1])
