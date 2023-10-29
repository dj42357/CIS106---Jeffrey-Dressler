#inputs
principle = float(input("Input the principle amount of the CD: "))
maturity = int(input("Input the years to maturity: "))

#processes
if principle > 100000 and maturity == 5:
  interest_rate = 0.06
elif principle >= 50000 and principle <= 100000 and maturity == 10:
  interest_rate = 0.05
elif principle >= 50000 and principle <= 100000 and maturity == 5:
  interest_rate = 0.04
else:
  interest_rate = 0.02
interest_amt = principle * interest_rate
interest_perc = interest_rate * 100

#outputs
print("")
print("Principle: ${}".format(principle))
print("Interest rate: {}%".format(int(interest_perc)))
print("Interest for the first year: ${}".format(round(interest_amt,2)))