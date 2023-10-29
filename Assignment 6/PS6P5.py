#inputs
name = str(input("Input your last name: "))
salary = float(input("Input your salary: "))
job = int(input("Input your job level: "))

#processes
if job >= 10:
  bonus_rate = 0.25
elif job <= 9 and job >= 5:
  bonus_rate = 0.2
else:
  bonus_rate = 0.1
bonus = bonus_rate * salary

#outputs
print("")
print("Last name: {}".format(name))
print("Bonus: ${}".format(round(bonus,2)))