# lambda arguments: expression
square = lambda x: x**2
print(square(5))


add = lambda a,b: a+b
print(add(2,5))

checkNumber = lambda x: "Even" if x%2==0 else "Odd"
print(checkNumber(5))
print(checkNumber(12))


def multiple(a):
    return lambda b:a*b

func = multiple(5)
print(func(4))

nums = [2,3,5,2,4]
out1 = list(map(lambda x: x*2,nums))
print(out1)

out2 = list(filter(lambda x: x%2==0,nums))
print(out2)

from functools import reduce
out3 = reduce(lambda a,b:a+b,nums)
print(out3)