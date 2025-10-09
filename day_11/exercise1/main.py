# Exercise 1: Create a Package
# Create a folder called math_tools
# Inside it, create:
# basic.py with add() and subtract() functions
# advanced.py with power() and factorial() functions
# __init__.py to expose all functions
# In a separate file, import and use all functions.
from math_tools import basic,advance
print(basic.add(2,5))
print(basic.subtract(2,5))

print(advance.power(5))
print(advance.factorial(4))