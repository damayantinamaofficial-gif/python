# Create a script that:
# Asks the user for price and quantity
# Calculates total cost
# Handles invalid inputs (non-numeric, zero quantity)

try:
    price = float(input("enter a price:"))
    quantity = int(input("enter quantity:"))
    if quantity <=0:
        raise ValueError("Quantity must be greater than zero.")
except ValueError as e:
    print(f"Error {e}")
finally:
    print("Transaction complete.")