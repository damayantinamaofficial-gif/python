fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(2,"kiwi")
fruits.remove("apple")
fruits.pop()
fruits.sort()
ind = fruits.index("cherry")

print(fruits[0])
print(fruits[-1])

print(f"fruits: {fruits}",ind)