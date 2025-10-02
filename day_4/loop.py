for i in range(5):
    print("i value is: ",i)
    
    
fruits = ["apple", "banana", "orange", "grapes"]
for fruit in fruits:
    print("Fruit: ",fruit)    
    
    
count = 0
while count < 5:
    print("count is: ",count)
    count +=1    
    

for i in range(7):
    if i==5:
        break
    print(i)    
    
    
for i in range(9):
    if (i%2!=0):
        continue
    print(i)    
    
    
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"num x {i} = {num*i}")    