#inputs
run = str(input("Would you like to run the program? (yes/no): "))
totalgross = 0
employees = 0
#processes & outputs
while run == "yes":
  print("")
  name = str(input("Enter the employees' last name: "))
  hours = float(input("Enter the amount of hours worked: "))
  pay = float(input("Enter the rate of pay: "))
  gross = hours * pay + (hours - 40) * (pay * 0.5) if hours > 40 else hours * pay
  print("")
  print("Last name: {}".format(name))
  print("Gross pay: {}".format(gross))
  totalgross += gross
  employees += 1
  print("")
  print("The sum of all gross pays' is: ${}".format(totalgross))
  print("Number of employees: {}".format(employees))
  average = totalgross / employees
  print("Average gross pay: ${}".format(average))
  print("")
  run = str(input("Calculate another employees' gross pay? (yes/no): "))