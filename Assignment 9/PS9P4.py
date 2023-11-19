def compPayRate(jobCode):
  if jobCode == "J":
    payRate = 50
  elif jobCode == "A":
    payRate = 30
  else:
    payRate = 25
  return payRate

totalGrossPay = 0
r = input("Do you want to compute an employee's gross pay? (y/n): ")
while r == "y":
  name = str(input("Input your last name: "))
  jobCode = str(input("Input your job code (J/A/L): "))
  hours = float(input("Input hours worked: "))
  payRate = compPayRate(jobCode)
  if hours <= 40:
    grossPay = hours * payRate
  else:
    grossPay = (hours * payRate) + (hours - 40)*(payRate * 0.5)
  totalGrossPay += grossPay
  print("Last name: ", name)
  print("Gross pay: ", grossPay)
  r = input("Do you want to compute another employee's gross pay? (y/n): ")

print("Total gross pay: ", totalGrossPay)