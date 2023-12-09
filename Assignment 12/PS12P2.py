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

f = open("PS12P2.txt", "r")

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>1ST ATTEMPT (before watching video)

"""
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

f = open("PS12P2.txt", "r")

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
reverseList(score, 0, 9)rintList(lname, score)
"""