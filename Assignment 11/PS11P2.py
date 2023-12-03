def compScore(score1, score2, score3):
  total = score1 + score2 + score3
  average = total / 3
  
  return total, average

name = str(input("Input your last name: "))
score1 = float(input("Input your 1st exam score: "))
score2 = float(input("Input your 2nd exam score: "))
score3 = float(input("Input your 3rd exam score: "))
total, average = compScore(score1, score2, score3)

print("")
print("Last name:",name)
print("Total score:",total)
print("Average score:",average)