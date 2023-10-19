#inputs
qty = int(input("Input the number of books to order: "))
cost = float(input("Input the cost per book: "))

#processes
order = qty * cost
shipping = 25 if order <= 50 else 0
total = order + shipping

#outputs
print("")
print("Total: ${}".format(round(total,2)))
print("Shipping: ${}".format(shipping))