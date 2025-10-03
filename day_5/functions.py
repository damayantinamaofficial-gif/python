def greet():
    print("Hello, World!")
    
greet()    


# with parameters

def fullName(firstName, lastName):
    print(f"full name is: {firstName} {lastName}")
    
fullName("damayanti","name")    


# return statment

def add(a,b):
    return a+b

result = add(5,6)
print("a + b =", result)


#defult statment

def greeting(name="Guest"):
    print(f"Hello, {name}")
    
greeting()  
greeting("Dammu")  
    