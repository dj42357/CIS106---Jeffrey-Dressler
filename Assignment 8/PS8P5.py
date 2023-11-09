f = open("PS8P5.txt", "r")

#initialize counters and sums to 0
count = 0
sum_tuition = 0

#get first data line
name = str(f.readline().rstrip('\n'))

while name !="":
  district = str(f.readline().rstrip('\n'))
  credits = float(f.readline())
  cost = 250 if district == "I" else 500
  tuition = cost * credits
  #sum and count
  sum_tuition += tuition
  count += 1
  #display data
  print("Last name: {}".format(name))
  print("Number of credits: {}".format(credits))
  print("Tuition: ${}".format(tuition))
  print("")
  #get next data
  name = str(f.readline().rstrip('\n'))
#after loop
print("Tuition sum: ${}".format(sum_tuition))
print("Number of students: {}".format(int(count)))