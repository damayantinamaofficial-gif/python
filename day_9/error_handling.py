try:
    stock = int(input("enter stock quantity:"))
    print(f"stock quantity {stock}")
except ValueError:
    print("Invaild stock")
else:
    print(f"stock quantity- {stock}")    
finally:
    print("Thanks!")    