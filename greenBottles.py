import time

bottles = 10

for x in range(bottles,0,-1):
  print("{0} green bottles, hanging on the wall".format(x))
  print("{0} green bottles, hanging on the wall".format(x))
  print("And if 1 green bottle should acidentally fall,")
  print("They'll be {0} green bottles hanging on the wall.".format(x-1))
  time.sleep(0.5)
