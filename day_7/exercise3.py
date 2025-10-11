dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Merge dict2 into dict1
# Final dict1 should be: {'a': 1, 'b': 3, 'c': 4}


dict1.update(dict2)
print(dict1)


students = {
    "101": {"name": "Amit", "marks": 85},
    "102": {"name": "Sara", "marks": 90}
}

# Print all student names
# Add a new student
# Update marks for student 101

## Method-1
names = []
for keys,stds in students.items():    
    if '101' in keys:
        stds.update({"marks":95}) 
    for keys,std in stds.items():
        if 'name' in keys:
            names.append(std)
           

print(names) 
students.update({"103":{"name":"Pari","marks":40}})
print(students)

## Method-2 
names = [std["name"] for std in students.values()] #List Comprehensions
students["104"] = {"name":"Pari 2","marks":45}
students["101"]["marks"] = 100
print(names,students)
