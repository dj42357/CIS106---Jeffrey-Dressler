#inputs
run = str(input("Would you like to run the program? (yes/no): "))
students = 0
#processes & outputs
while run == "yes":
  print("")
  name = str(input("Enter students' last name: "))
  score1 = float(input("Enter the first exam score: "))
  score2 = float(input("Enter the second exam score: "))
  average = (score1 + score2) / 2
  print("")
  print("Last name: {}".format(name))
  print("Average score: {}".format(average))
  students += 1
  print("Number of students: {}".format(students))
  print("")
  run = str(input("Calculate another students' score? (yes/no): "))