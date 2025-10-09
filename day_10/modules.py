import math
import random
import requests

#Built-in Modules
print(math.sqrt(16))
print(random.randint(1,20))

#User-defined Modules
def discount_price(price,discount):
    return price*(1-discount)

def format_product(name,price):
    return f"{name} - {price}"

#Third-party Modules
res = requests.get("https://api.github.com")
print(res.status_code)