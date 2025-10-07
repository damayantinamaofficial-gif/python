# Write a program that counts the frequency of each character in a string.
text = "hello world"
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

out = {}
# string convert into list
arr = list(text)
for val in arr:
    out[val] = out.get(val,0)+1

print(out)
