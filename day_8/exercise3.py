set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Find union
# Find intersection
# Find difference (set1 - set2)
# Find symmetric difference

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1 | set2)  # Combines all unique elements

# Intersection
print(set1 & set2)  # Common elements

# Difference
print(set1 - set2)  # Elements in set1 but not in set2

# Symmetric Difference
print(set1 ^ set2)  # Elements in either set, but not both


a = {1, 2}
b = {1, 2, 3, 4}

# Check if a is subset of b
# Check if b is superset of a

print(a.issubset(b))
print(b.issuperset(a))