# Use the math module to:
# - Calculate square root of 49
# - Find the value of pi
# - Round 3.14159 to 2 decimal places
import math

print(math.sqrt(49))
print(math.pi)
print(round(3.14159,2))

#Create and Use a Custom Module for add two digit
def add(a,b):
    return a+b


# Install and use the 'datetime' module to:
# - Print current date and time
# - Format it as "DD-MM-YYYY HH:MM"
from datetime import datetime
currentDate = datetime.now()
print(currentDate)
print(currentDate.strftime("%d-%m-%Y %H:%M"))
