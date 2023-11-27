def compTicket(miles):
  if miles >= 30:
    ticket = 12
  elif miles > 20:
    ticket = 10
  elif miles > 10:
    ticket = 8
  else:
    ticket = 5

  return ticket

sumTicket = 0

r = input("Do you want to compute your ticket price? (y/n): ")
while r == "y":
  name = str(input("Input your last name: "))
  miles = float(input("Input how far you are from Chicago in miles: "))
  ticket = compTicket(miles)

  print("")
  print("Name:",name)
  print("Ticket price: $",ticket)

  sumTicket += ticket
  r = input("Would you like to run the program again? (y/n): ")

print("")
print("Sum of all tickets: $",sumTicket)