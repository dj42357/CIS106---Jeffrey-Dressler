#inputs
qty = int(input("Input the number of tickets: "))

#processes
if qty >= 25:
  price = 50
elif qty <= 24 and qty >= 10:
  price = 60
elif qty <= 9 and qty >= 5:
  price = 70
else:
  price = 75
total = qty * price

#outputs
print("")
print("Number of tickets: {}".format(qty))
print("Price per ticket: ${}".format(price))
print("Total: ${}".format(total))