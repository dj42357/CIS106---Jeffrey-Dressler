#I'm unsure if this code is supposed to reflect next month or the current month.
#I wrote it as the current month. Otherwise you would shift the values forward 1 month.
def compForecastSales(month, sales):
  if month == 'January' or month == 'February' or month == 'March':
    forecastSales = sales * 1.1
  elif month == 'April' or month == 'May' or month == 'June':
    forecastSales = sales * 1.15
  elif month == 'July' or month == 'August' or month == 'September':
    forecastSales = sales * 1.2
  elif month == 'October' or month == 'November' or month == 'December':
    forecastSales = sales * 1.25
  #generic fallback code, unsure what the fallback should've been, possibly 1.1 instead
  else:
    forecastSales = sales
  return forecastSales

r = input("Do you want to compute next month's sales? (y/n): ")
while r == "y":
  name = str(input("Input your last name: "))
  month = str(input("Input the current month: "))
  sales = int(input("Input amount of sales: "))
  forecastSales = compForecastSales(month, sales)
  print("")
  print("Next month's sales:",int(forecastSales))
  r = input("Would you like to run the program again? (y/n): ")
