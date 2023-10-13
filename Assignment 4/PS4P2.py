#inputs
PPS = float(input("Input the purchase price per share: "))
CSP = float(input("Input the current stock price per share: "))
NS = int(input("Input the number of shares: "))

#processes
change = (CSP - PPS) * NS

#outputs
print("")
print("Amount lost/gained: ${}".format(change))