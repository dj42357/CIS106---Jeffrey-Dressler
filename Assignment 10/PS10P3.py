def compTotal(make, model, code, msrp):
  if make == 'Honda' and model == 'Accord':
    discount = 0.10
  elif make == 'Toyota' and model == 'Rav4':
    discount = 0.15
  elif code == 'y':
    discount = 0.30
  else:
    discount = 0.05

  total = (msrp * (1 - discount)) * 1.07

  return total

sumMSRP = 0
sumTotal = 0

r = input("Do you want to compute the price for a car? (y/n): ")
while r == "y":
  make = str(input("Input the make of the car: "))
  model = str(input("Input the model of the car: "))
  code = str(input("Is the vehicle electric? (y/n): "))
  msrp = float(input("Input the MSRP of the car: "))
  total = compTotal(make, model, code, msrp)

  print("")
  print("Final price: $",total)

  sumMSRP += msrp
  sumTotal += total
  r = input("Would you like to run the program again? (y/n): ")

print("")
print("Sum of MSRPs: $",sumMSRP)
print("Sum of final prices: $",sumTotal)