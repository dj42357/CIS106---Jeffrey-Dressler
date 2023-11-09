f = open("PS8P4.txt", "r")

#initialize counters and sums to 0
count = 0
totp_ex = 0

#get first data line
item = str(f.readline().rstrip('\n'))

while item !="":
  qty = int(f.readline())
  price = float(f.readline())
  extprice = qty * price
  #sum and count
  totp_ex += extprice
  count += 1
  #display data
  print("Item: {}".format(item))
  print("Quantity: {}".format(qty))
  print("Price: ${}".format(price))
  print("Extended price: ${}".format(extprice))
  print("")
  #get next data
  item = str(f.readline().rstrip('\n'))
#after loop
print("Total extended price: ${}".format(totp_ex))
print("Number of orders: {}".format(int(count)))
avg = totp_ex / count
print("Average order price: ${}".format(round(avg,2)))