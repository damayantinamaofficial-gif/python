person = {
    "name": "Dammu",
    "class": "1st year",
    "year": 2025
}

print(person)
print(person.clear())
print(person)

std = {
  "name": "Damayanti",
  "age": 20,
  "grade": "A",
  "course": ["PHP","JAVASCRIPT","MYSQL","JAVA"]
}

print(std)
print(std.items())

for key,value in std.items():
    print(key,": ",value)


print(std.get("name"))
print(std.keys())
print(std.values())
std["age"] = 32
std.update({"name":"Damayanti Nama"})
del std["grade"]

if "name" in std:
    print("name key exist")

if "grade" in std:
    print("grade key exist")
else:
    print("not exist")    

print(std)



