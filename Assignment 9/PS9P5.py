def compTuition(hours, code):
  credit = 250 if code == "I" else 550
  tuition = hours * credit
  return tuition

sumTuition = 0
r = input("Do you want to compute a student's tuition? (y/n): ")
while r == "y":
  name = str(input("Input your last name: "))
  code = str(input("Input your district code (I/O): "))
  hours = float(input("Input credit hours: "))
  tuition = compTuition(hours, code)
  sumTuition += tuition
  print("Last name: ", name)
  print("Tuition owed: ", tuition)
  r = input("Do you want to compute another student's tuition? (y/n): ")

print("Sum of all tuitions owed: ", sumTuition)