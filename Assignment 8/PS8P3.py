f = open("PS8P3.txt", "r")

#initialize counters and sums to 0
count = 0
tot_bonus = 0

#get first data line
name = str(f.readline().rstrip('\n'))

while name !="":
  salary = float(f.readline())
  if salary >= 100000:
    rate = 0.2
  elif salary >= 50000:
    rate = 0.15
  else:
    rate = 0.1
  bonus = salary * rate
  #sum and count
  tot_bonus += bonus
  count += 1
  #display data
  print("Last name: {}".format(name))
  print("Salary: ${}".format(salary))
  print("Bonus: ${}".format(bonus))
  print("")
  #get next data
  name = str(f.readline().rstrip('\n'))
#after loop
print("Sum of all bonuses: ${}".format(tot_bonus))