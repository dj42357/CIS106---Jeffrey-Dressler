def compScore(score1, score2, score3, handicap):
  total = score1 + score2 + score3
  scoreAvg = total / 3
  scoreAvgH = scoreAvg * handicap

  return scoreAvg, scoreAvgH

name = str(input("Input your last name: "))
score1 = float(input("Input your 1st score: "))
score2 = float(input("Input your 2nd score: "))
score3 = float(input("Input your 3rd score: "))
#for handicap it's your total%, so if you gain handicap 1.10, or if you lose it 0.9
#if worded differently, I'd change line 4 to "scoreAvgH = scoreAvg * (1 +/- handicap)"
handicap = float(input("Input your handicapped percentage: "))
scoreAvg, scoreAvgH = compScore(score1, score2, score3, handicap)

print("")
print("Last name: ",name)
print("Average score:",scoreAvg)
print("Average score w/ Handicap:",scoreAvgH)