# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("you are not eligible to vote.")


# marks = int(input("Enter your marks: "))
# if marks >=90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 65:
#     print("Grade C")
# else:
#     print("Grade D") 

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("username not found")   
    
    
    