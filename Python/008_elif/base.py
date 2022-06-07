x = int(input("Please enter a number."))
y = int(input("Please enter a second number"))
z = input("Please enter an operation")

minus = "-"
plus = "+"
divide = "/"
multiply = "*"


if z == minus:
    print(x-y)
elif z == plus:
    print(x+y)
elif z == divide:
    print(x/y)
elif z == multiply:
    print(x*y)
    