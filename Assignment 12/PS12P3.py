def displaynames(lastn,score):
  l = len(lastn)
  print (">>>List:")
  for x in range(0,l,1):
    print(x, " ", lastn[x], " ", score[x])

def displayr(lastn,score):
  l = len(lastn)
  print(">>>Reverse List:")
  for y in range (l-1,-1,-1):
    print(y, " ", lastn[y], " ", score[y])

def highlow(lastn,score):
  l = len(lastn)
  highscore = -1
  lowscore = 9999
  for y in range (0,l,1):
    if float(score[y]) > float(highscore):
      highindex = y
      highscore = score[y]
    if float(score[y]) < float(lowscore):
      lowindex = y
      lowscore = score[y]
  print(">>>Highest & Lowest:")
  print(highindex, " ", lastn[highindex], " ", highscore)
  print(lowindex, " ", lastn[lowindex], " ", lowscore)

f = open("PS12P3.txt", "r")

lastn = []
score = []

lastname = f.readline()

while lastname != "":
  lastn.append(str(lastname).rstrip("\n"))
  s = float(f.readline())
  score.append(s)
  lastname = f.readline()
f.close()

displaynames(lastn,score)
print("")
displayr(lastn,score)
print("")
highlow(lastn,score)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>1ST ATTEMPT (before watching video)

'''
def printList(lname, score):
  l = len(lname)
  for x in range(0,l,1):
    print(lname[x], " ", score[x])


def reverseList(A, start, end): 
  while start < end: 
    A[start], A[end] = A[end], A[start] 
    start += 1
    end -= 1
  return

def highestLowest(lname, score):

  max = 0
  min = 999
  minN = ""
  maxN = ""
  l = len(lname)

  for i in range(1, l):
    if score[i] > max:
      max = score[i]
      maxN = lname[i]

  for i in range(1, l):
    if score[i] < min:
      min = score[i-1]
      minN = lname[i-1]

  print("Highest:", maxN, max)
  print("Lowest:", minN, min)
  return

f = open("PS12P3.txt", "r")

lname = []
score = []

lastname = f.readline()

while lastname != "":
  lname.append(str(lastname).rstrip("\n"))
  s = float(f.readline())
  score.append(s)
  lastname = f.readline()
f.close()

print(">>>List:")
printList(lname, score)

print("")
print(">>>Reversed List:")
reverseList(lname, 0, 9)
reverseList(score, 0, 9)
printList(lname, score)

print("")
print(">>>Highest & Lowest:")
highestLowest(lname, score)
'''