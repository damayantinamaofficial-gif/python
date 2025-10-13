# Functions (to organize logic)
# Lists & Dictionaries (to store product data)
# File Handling (to save/load inventory)
# Error Handling (to manage bad input)
import json

def add_product(inventory):
    try:
        name = input("enter product name: ")
        price = float(input("enter product price: "))
        stock = int(input("enter stock: "))
        inventory.append({'name':name,'price':price,'stock':stock})
        print(f"{name} added successfully.")
    except ValueError:
        print("Input Error, Price and stock must be number.")

def view_product(inventory):
    if not inventory:
        print("Inventory empty!")
    else:
        for prod in inventory:
            print(f"{prod['name']} - ₹{prod['price']} - stock {prod['stock']}")   

def save_inventory(inventory,filename="products.json"):
    with open(filename,"w") as file:
        json.dump(inventory,file)
    print("Inventory saved.")

def load_inventory(filename="products.json"):
    try:
        with open(filename,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File Not Found",{FileNotFoundError}) 
        return []   

def remove_inventory(inventory):
    name = input("enter product name for delete")
    for item in inventory:
        if item['name'].lower() == name.lower():
            inventory.remove(item)
            print(f"{name} removed")
            return
    print("Product not found")



# add_product() 
# view_product()  
# save_inventory({'name':'Item 1','price':200,'stock':5})
# print(load_inventory())       

def main():
    inventory = load_inventory()
    while True:
        print("\n1. Add Product \n2. View Product \n3. Save \n4. remove product")
        choice = int(input("Choose an option: "))
        if choice == 1:
            add_product(inventory)
        elif choice == 2:
            view_product(inventory)
        elif choice == 3:
            save_inventory(inventory)
        elif choice == 4:
            remove_inventory(inventory)   
        else:
            print("Invalid Choice") 

main()       
