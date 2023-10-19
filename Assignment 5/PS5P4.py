#inputs
name = str(input("Input the name of the appliance: "))
cost = float(input("Input the cost of the appliance: "))

#processes
warrantee = cost * 0.05 if cost <= 1000 else cost * 0.1
total = cost + warrantee

#outputs
print("")
print("Appliance:",name)
print("Cost: ${}".format(cost))
print("Warrantee: ${}".format(round(warrantee,2)))
print("Total: ${}".format(round(total,2)))