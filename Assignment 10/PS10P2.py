def compSquareFootage(length, width, height):
  squareFootage = (2 * length * width) + (2 * length * height) + (2 * width * height)
  return squareFootage

r = input("Do you want to compute the amount of paint needed for a room? (y/n): ")
while r == "y":
  length = float(input("Input the rooms' length: "))
  width = float(input("Input the rooms' width: "))
  height = float(input("Input the rooms' height: "))
  squareFootage = compSquareFootage(length, width, height)

  paint = squareFootage / 50
  print("")
  print("Gallons of paint needed:",paint)
  r = input("Would you like to run the program again? (y/n): ")