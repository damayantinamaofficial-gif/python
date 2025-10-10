#find even no. of Numbers 1–10 using list comprehension
numbers = [num for num in range(11) if (num%2==0)]
print(numbers)

#print even and odd if number is even/odd of Numbers 1–10 using list comprehension
nums = [f"{num} Even" if num%2==0 else f"{num} Odd" for num in range(11)]
print(nums)

#Squares of Numbers 1–10
sqr = [num**2 for num in range(1,11)]
print(sqr)

#Reverse Strings in List
words = ["apple", "banana", "cherry"]
reversed_words = [word[::-1] for word in words]
print(reversed_words)
