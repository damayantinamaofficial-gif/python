# Check if a number is positive
isPosNumber = lambda x: x>0
print(isPosNumber(23))
print(isPosNumber(-3))

# Find max of two numbers
maxNum = lambda a,b: a if a>b else b
print(maxNum(10,12))


# Sort Products by Price
products = [
    {"name": "Shoes", "price": 2999},
    {"name": "Bags", "price": 1999},
    {"name": "Watches", "price": 4999}
]

sorted = sorted(products,key=lambda x: x['price'])
print(sorted)