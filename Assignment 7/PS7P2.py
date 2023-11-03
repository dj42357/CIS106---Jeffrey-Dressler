#inputs
start = int(input("Input a starting value: "))
stop = int(input("Input a stopping value: "))
increment = int(input("Input an increment value: "))

#processes & outputs
end = 0
print("[{}]".format(start))
while start < stop and end == 0:
  if start + increment <= stop:
    start += increment
  else:
    end = 1
  if start == stop or end == 1:
    pass
  else:
    print(start)
print("[{}]".format(stop))