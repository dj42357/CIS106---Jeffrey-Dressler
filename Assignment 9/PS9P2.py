def compBattingAvg(hits, bats):
  battingAvg = hits / bats
  return battingAvg

sumPlayers = 0
r = input("Do you want to compute a player's batting average? (y/n): ")
while r == "y":
  name = str(input("Input player's last name: "))
  bats = int(input("Input the number of at bats: "))
  hits = int(input("Input the number of hits: "))
  battingAvg = compBattingAvg(hits, bats)
  sumPlayers += 1
  print("Player: ", name)
  print("Batting Average: ", battingAvg)
  r = input("Do you want to compute another player's batting average? (y/n): ")
  
print("Total number of players: ", sumPlayers)