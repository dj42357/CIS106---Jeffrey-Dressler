principle = float(input("Enter a principle amount: "))
rate = float(input("Enter the interest rate: "))
print("")

#initialize counters and sums to 0
count = 0
tot_interest = 0

while count < 5:
  interest = principle * rate
  end_bal = principle + interest
  #sum and count
  tot_interest += interest
  count += 1
  #display data
  print("Year: {}".format(count))
  print("Starting Balance: ${}".format(principle))
  print("Ending Balance: ${}".format(end_bal))
  print("")
  #get next data
  principle = end_bal
#after loop
print("Accumulated interest: ${}".format(tot_interest))
