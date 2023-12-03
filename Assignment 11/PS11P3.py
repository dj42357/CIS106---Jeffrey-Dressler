def compCommission(sale):
  commissionPerc = 0.10 if sale > 100000 else 0.05

  commission = sale * commissionPerc
  target = sale * 1.05

  return commission, target

name = str(input("Input your last name: "))
sale = float(input("Input sale amount: "))
commission, target = compCommission(sale)

print("")
print("Last name:",name)
print("Commission earned: ${}".format(commission))
print("Next years' target sales: ${}".format(target))