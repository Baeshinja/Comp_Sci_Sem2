x = int(input("Please enter a line length." + " "))
y = input("Do you want a horizontal or vertical line? (h or v)" + " ")
q = input("Enter a symbol" + " ")

a = "h"
b = "v"

if y == b:
    for z in range(0,x):
      print(q)
elif y == a:
    for z in range(0,x):
      print(q, end=" ")
