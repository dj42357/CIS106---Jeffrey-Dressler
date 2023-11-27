def compValue(county, marketValue):
  if county == 'Cook':
    AVP = 0.90
  elif county == 'DuPage':
    AVP = 0.80
  elif county == 'McHenry':
    AVP = 0.75
  elif county == 'Kane':
    AVP = 0.60
  else:
    AVP = 0.70

  value = marketValue * AVP

  return value

sumMarketValue = 0
sumValue = 0

r = input("Do you want to compute your housing value? (y/n): ")
while r == "y":
  county = str(input("Input your county: "))
  marketValue = float(input("Input your houses' market value: "))
  value = compValue(county, marketValue)

  print("")
  print("Market value: $",marketValue)
  print("Assessed value: $",value)

  sumMarketValue += marketValue
  sumValue += value
  r = input("Would you like to run the program again? (y/n): ")

print("")
print("Sum of market values: $",sumMarketValue)
print("Sum of assessed values: $",sumValue)