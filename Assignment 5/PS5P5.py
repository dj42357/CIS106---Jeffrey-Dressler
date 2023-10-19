#inputs
name = str(input("Input your last name: "))
dependents = int(input("Input the number of dependents: "))
gross = float(input("Input your gross income: "))

#processes
Agross = gross - dependents * 12000
rate = 0.1 if Agross <= 50000 else 0.2
tax = Agross * rate
tax = 100 if tax < 0 else tax

#outputs
print("")
print("Last name:",name)
print("Gross income: ${}".format(gross))
print("Number of dependents:",dependents)
print("Adjusted gross income: ${}".format(Agross))
print("Income tax: ${}".format(tax))