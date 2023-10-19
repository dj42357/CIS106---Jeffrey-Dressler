#inputs
qty = int(input("Input the quantity of an item: "))

#processes
unit = 3 if qty >= 1000 else 5
extprice = unit * qty
tax = extprice * 0.07
total = extprice + tax

#outputs
print("")
print("Quantity:",qty)
print("Unit price: ${}".format(unit))
print("Extended price: ${}".format(extprice))
print("Tax: ${}".format(round(tax,2)))
print("Total: ${}".format(round(total,2)))