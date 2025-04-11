# A variable stores a value — like a name or a number
name = "Zayed"
age = 24
city = "Mumbai"

# Print the values stored in the variables
print("Name:", name)
print("Age:", age)
print("City:", city)

# You can change the value of a variable
city = "Bangalore"
print("Updated City:", city)
#
#
#
# ✅ VALID variable names — these will work in Python:

my_name = "Zayed"               # uses letters + underscore
age1 = 24                       # can end with a number
_height = 175                  # can start with underscore
user_country = "India"         # underscores are commonly used
fullName = "Zayed Bin Jad"     # camelCase style (also okay)

# Print them to confirm
print("My name is:", my_name)
print("Age is:", age1)
print("Height:", _height)
print("Country:", user_country)
print("Full Name:", fullName)

# ❌ INVALID variable names — these will give errors if you try to use them:

# 1name = "Ali"        ❌ Starts with a number
# user-name = "Sarah"  ❌ Hyphens are not allowed
# my name = "Zara"     ❌ Spaces are not allowed
# class = "Math"       ❌ 'class' is a reserved keyword in Python
# def = "Function"     ❌ 'def' is also a keyword (used to define functions)

# Python has a list of **reserved words** (like `class`, `if`, `else`, `def`, `for`) which you can't use as variable names.
# Full list of reserved keywords: https://docs.python.org/3/reference/lexical_analysis.html#keywords

# 🧠 Tips:
# - Use clear names that describe what the variable stores (like 'user_age' or 'city_name')
# - Avoid using single letters like x, y, z unless it's for math or short loops
#
#
#
#
# Identifiers
# ===========
# Every variable is an identifier but not every identifier is a variable.
# Identifers can also be functions, classes, modules, etc
# Every identifier in Python has a **name** and a **value** and that Values have a **type**.(next topic)
# Note :
# - python is a case-sensitive language
# - Rules for identifier's names is same as variable names