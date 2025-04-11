# Note: In the program below, the print() function is used to display the output in the console.
# In the print() function, the end='\n'  is used to print each output on a new line
# In the print() function, the (exampl: "a + b =") is used to explain the syntax of the output
# Don't get confused just run the program it will help you to understand the output

# 🧮 ARITHMETIC OPERATORS
print("🧮 ARITHMETIC OPERATORS")
a = 10
b = 3
print("a + b =", a + b)       # Addition → 13
print("a - b =", a - b)       # Subtraction → 7
print("a * b =", a * b)       # Multiplication → 30
print("a / b =", a / b)       # Division → 3.333... (float result)
print("a // b =", a // b)     # Floor division → 3 (drops decimals)
print("a % b =", a % b)       # Modulus → 1 (remainder of division)
print("a ** b =", a ** b)     # Exponentiation → 1000 (10^3)

# 📝 ASSIGNMENT OPERATORS
print("\n📝 ASSIGNMENT OPERATORS")
x = 5                        # Initial value of x
print("Initial x =", x)

x += 3                       # Add 3 to x → x = x + 3
print("x += 3 →", x)         # x becomes 8

x *= 2                       # Multiply x by 2 → x = x * 2
print("x *= 2 →", x)         # x becomes 16

x -= 1                       # Subtract 1 from x
print("x -= 1 →", x)         # x becomes 15

x /= 2                       # Divide x by 2 → float result
print("x /= 2 →", x)         # x becomes 7.5

x **= 2                      # Square x → x = x ** 2
print("x **= 2 →", x)        # x becomes 56.25

# 🧐 COMPARISON OPERATORS
print("\n🧐 COMPARISON OPERATORS")
print("a == b:", a == b)     # False → 10 is not equal to 3
print("a != b:", a != b)     # True → 10 is not equal to 3
print("a > b:", a > b)       # True → 10 is greater than 3
print("a < b:", a < b)       # False → 10 is not less than 3
print("a >= b:", a >= b)     # True → 10 is greater or equal to 3
print("a <= b:", a <= b)     # False → 10 is not less or equal to 3

# 🧠 LOGICAL OPERATORS
print("\n🧠 LOGICAL OPERATORS")
age = 20
country = "India"

# 'and' checks if both conditions are True
print("age > 18 and country == 'India':", age > 18 and country == "India")

# 'or' checks if at least one condition is True
print("age > 18 or country == 'USA':", age > 18 or country == "USA")

# 'not' reverses the result
print("not age < 18:", not age < 18)

# 📦 MEMBERSHIP OPERATORS
print("\n📦 MEMBERSHIP OPERATORS")
colors = ["red", "green", "blue"]    # A list of colors

# 'in' checks if a value is inside the list
print("'red' in colors:", "red" in colors)

# 'not in' checks if a value is NOT in the list
print("'yellow' not in colors:", "yellow" not in colors)

# 🧱 IDENTITY OPERATORS
print("\n🧱 IDENTITY OPERATORS")
x = [1, 2]
y = x         # y points to the same object as x
z = [1, 2]     # z is a different object with the same values

# 'is' checks if two variables refer to the same object in memory
print("x is y:", x is y)     # True (same memory reference)
print("x is z:", x is z)     # False (different objects)

# '==' checks if values are equal (even if objects are different)
print("x == z:", x == z)     # True (same content)