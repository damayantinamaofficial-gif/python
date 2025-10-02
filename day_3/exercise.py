# Create a script that:
# Asks the user for their age
# If age < 13 → print "Child"
# If age between 13–19 → print "Teenager"
# If age between 20–59 → print "Adult"
# If age 60+ → print "Senior"

age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior")