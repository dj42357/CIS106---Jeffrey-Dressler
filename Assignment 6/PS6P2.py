#inputs
part = int(input("Input the part number: "))
qty = int(input("Input the quantity of parts: "))

#processes
if part == 10 or part == 55:
  cost = 1
elif part == 99:
  cost = 2
elif part == 80 or part == 70:
  cost = 3
else:
  cost = 5
total = cost * qty

#outputs
print("")
print("Part number: {}".format(part))
print("Cost per unit: ${}".format(cost))
print("Total: ${}".format(total))