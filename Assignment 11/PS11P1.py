def compDiscount(quantity, price, discountPerc):
  extPrice = quantity * price
  discountAmt = extPrice * discountPerc
  Total = extPrice - discountAmt

  return discountAmt, Total

qty = int(input("Input the quantity of items: "))
price = float(input("Input the price of the item: "))
discountPerc = float(input("Input the discount percentage: "))
discountAmt, Total = compDiscount(qty, price, discountPerc)

print("")
print("The quantity of items is:",qty)
print("The price of the item is ${}".format(price))
print("The discount amount is: ${}".format(discountAmt))
print("The discounted price is: ${}".format(Total))
