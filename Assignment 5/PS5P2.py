#inputs
item = str(input("Input the item's letter (A or B): "))
qty = int(input("Input the quantity: "))

#processes
unit = 10 if item == "A" else 20
ext = unit * qty

#outputs
print("")
print("Item:",item)
print("Unit price: ${}".format(unit))
print("Extended price: ${}".format(ext))