#inputs
make = input("Input the make of the car: ")
model = input("Input the model of the car: ")
msrp = float(input("Input the MSRP: "))
discount = float(input("Input the discount percentage as a decimal: "))

#processes
discountamt = msrp * discount
price = msrp - discountamt

#outputs
print("")
print("Make:",make)
print("Model:",model)
print("MSRP:",msrp)
print("Discount %:",discount)
print("Discount Amount:",discountamt)
print("Final Price:",price)