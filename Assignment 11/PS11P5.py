def compTotal(qty, unitPrice):
  global total
  total = qty * unitPrice
  global tax
  tax = total * 0.07

  return

qty = float(input("Input quantity: "))
unitPrice = float(input("Input unit price: "))
compTotal(qty, unitPrice)

final = total + tax

print("")
print("Total (without tax): ${}".format(round(total,2)))
print("Tax: ${}".format(round(tax,2)))
print("")
print("Total (with tax): ${}".format(round(final,2)))