import random 
numbers = [3,6,2,5,9,10,1,7,4,8]
x = int(input("How many random numbers would you like? (10 numbers max)"))

for i in range(0,x):
    import random
    i = int(random.randrange(0,10))
    print(numbers[i], end=". ")