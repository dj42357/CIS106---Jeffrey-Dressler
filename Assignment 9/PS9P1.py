def compExtPrice(qty, unitPrice):
  extPrice = qty * unitPrice
  discountAmt = extPrice * 0.1 if extPrice > 10000 else 0
  newExtPrice = extPrice - discountAmt
  return newExtPrice

totalExtPrice = 0
r = input("Do you want to compute extended price? (y/n): ")
while r == "y":
  qty = int(input("Enter quantity: "))
  unitPrice = float(input("Enter unit price: "))
  extPrice = compExtPrice(qty, unitPrice)
  totalExtPrice += extPrice
  print("Extended price: ${}".format(extPrice))
  r = input("Do you want to run the program again? (y/n): ")

print("Total extended price: ${}".format(totalExtPrice))
