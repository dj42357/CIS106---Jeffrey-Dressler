def displaynames(lastn):
  l = len(lastn)
  print (">>>List:")
  for x in range(0,l,1):
    print(x, " ", lastn[x])

def displayr(lastn):
  l = len(lastn)
  print(">>>Reverse List:")
  for y in range (l-1,-1,-1):
    print(y, " ", lastn[y])

f = open("PS12P1.txt", "r")

lastn = []

lastname = f.readline()

while lastname != "":
  lastn.append(str(lastname).rstrip("\n"))
  lastname = f.readline()
f.close()

displaynames(lastn)
print("")
displayr(lastn)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>1ST ATTEMPT (before watching video)

#def printList(lname):
#  for i in lname:
#    print(i)
#
#def reverseList(A, start, end): 
#  while start < end: 
#    A[start], A[end] = A[end], A[start] 
#    start += 1
#    end -= 1
#  return
#
#f = open("PS12P1.txt", "r")
#
#name = []
#
#lastname = f.readline()
#
#while lastname != "":
#  lname.append(str(lastname).rstrip("\n"))
#  lastname = f.readline()
#f.close()
#
#print(">>>List:")
#printList(lname)
#
#print("")
#print(">>>Reversed List:")
#reverseList(lname, 0, 9)
#printList(lname)