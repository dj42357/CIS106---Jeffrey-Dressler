#inputs
run = str(input("Would you like to run the program? (yes/no): "))
sumdiscount = 0
#processes & outputs
while run == "yes":
  print("")
  qty = int(input("Enter the amount of items: "))
  price = float(input("Enter the price of the item: "))
  extprice = price * qty
  discountamt = extprice * 0.25 if extprice > 10000 else extprice * 0.1
  total = extprice - discountamt
  print("")
  print("Extended price: ${}".format(extprice))
  print("Discount amount: ${}".format(round(discountamt,2)))
  print("Total: ${}".format(total))
  sumdiscount += discountamt
  print("")
  print("The sum of all discounts is: ${}".format(sumdiscount))
  print("")
  run = str(input("Calculate another order? (yes/no): "))