#inputs
meal = float(input("Input the price of the meal: "))

#processes
tip15 = meal * 0.15
total15 = meal + tip15
tip18 = meal * 0.18
total18 = meal + tip18
tip20 = meal * 0.2
total20 = meal + tip20

#outputs
print("")
print("With 15% tip:")
print("Total: ${}".format(meal))
print("Tip: ${}".format(round(tip15,2)))
print("Total with tip: ${}".format(round(total15,2)))
print("")
print("With 18% tip:")
print("Total: ${}".format(meal))
print("Tip: ${}".format(round(tip18,2)))
print("Total with tip: ${}".format(round(total18,2)))
print("")
print("With 20% tip:")
print("Total: ${}".format(meal))
print("Tip: ${}".format(round(tip20,2)))
print("Total with tip: ${}".format(round(total20,2)))