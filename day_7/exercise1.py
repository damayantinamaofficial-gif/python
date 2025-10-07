person = {
    "name": "Rahul",
    "age": 25,
    "profession": "Engineer"
}

# Print all keys
# Print all values
# Add a new key "city" with value "Mumbai"
# Update age to 26
# Remove profession

print(person.keys())
print(person.values())
print(list(person.values()))
person["city"] = "Mumbai"
person.update({"age":26})
del person["profession"]
print(person)