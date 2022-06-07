x =int(input("How many items would you like to purchase?"))

total = 0
for i in range(0,x):
  y = input("What you like to buy?")
  z = float(input("How much does this cost?"))
  print("Thanks for purchasing" + " " + y)
  total = total + z
  
print("Your total is plus the $100 tax is:" + str(total+100))
print("Blame inflation not me.")