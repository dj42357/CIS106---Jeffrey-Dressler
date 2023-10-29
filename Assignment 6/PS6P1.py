#inputs
qty = int(input("Input the quantity of widgets: "))

#processes
if qty > 10000:
  price = 10
elif qty > 5000:
  price = 20
else:
  price = 30
extprice = qty * price
tax = extprice * 0.07
total = extprice + tax

#outputs
print("")
print("Extended price: ${}".format(extprice))
print("Tax amount: ${}".format(round(tax,2)))
print("Total: ${}".format(round(total,2)))