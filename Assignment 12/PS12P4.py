def displaynames(lastn,batAVG):
  l = len(lastn)
  print (">>>Player List:")
  for x in range(0,l,1):
    print(x, " ", lastn[x], " ", batAVG[x])

def findname(lastn,batAVG,nameinput):
  l = len(lastn)
  for y in range (0,l,1):
    if lastn[y] == nameinput:
      print(y, " ", lastn[y], " ", batAVG[y])

f = open("PS12P4.txt", "r")

lastn = []
batAVG = []

lastname = f.readline()

while lastname != "":
  lastn.append(str(lastname).rstrip("\n"))
  s = float(f.readline())
  batAVG.append(s)
  lastname = f.readline()
f.close()

displaynames(lastn,batAVG)
print("")
r = input("Would you like to find a players' batting average? (y/n): ")
while r == "y":
  print("")
  nameinput = input("Enter a players' last name: ")
  findname(lastn,batAVG,nameinput)
  print("")
  r = input("Would you like to run the program again? (y/n): ")