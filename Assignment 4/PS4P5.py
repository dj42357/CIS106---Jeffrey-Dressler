#inputs
costs = float(input("Input the fixed costs: "))
ppu = float(input("Input the price per unit: "))
cpu = float(input("Input the cost per unit: "))

#processes
bep = costs / (ppu - cpu)

#outputs
print("")
print("Break even point:",round(bep,1),"units")