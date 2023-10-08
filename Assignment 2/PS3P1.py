#inputs
ticker = input("Input the stock ticker symbol: ")
numshare = float(input("Input the number of shares: "))
costshare = float(input("Input the cost of the share(s): "))

#processes
invested = numshare * costshare

#outputs
print("")
print("Stock:",ticker)
#I was getting weird long decimals, so I'm just going to implement round() for this problem
print("Amount invested:",round(invested,2))