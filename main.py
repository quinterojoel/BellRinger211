x = 1
y = 20
z = True
while z == True:
  y += 1
  if y == 60:
    y = 1
    x +=1
  print(x, ":", y, "PM")
  if x == 2 and y == 19:
    break
  time.sleep(60)
