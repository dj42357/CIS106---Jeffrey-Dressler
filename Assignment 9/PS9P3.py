def compMPG(miles, gallons):
  MPG = miles / gallons
  return MPG

sumTrips = 0
r = input("Do you want to compute your miles per gallon? (y/n): ")
while r == "y":
  city = str(input("Input the destination city: "))
  miles = int(input("Input your miles travelled: "))
  gallons = int(input("Input gallons used: "))
  MPG = compMPG(miles, gallons)
  sumTrips += 1
  print("Destination: ", city)
  print("Miles travelled: ", miles)
  print("Miles per gallon: ", MPG)
  r = input("Do you want to compute another trip? (y/n): ")

print("Total trips: ", sumTrips)