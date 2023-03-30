s,t,x = (int(x) for x in input().split())
if t - s < 0:
  if x < t or s <= x:
    print("Yes")
  else:
    print("No")
else:
  if x < t and s <= x:
    print("Yes")
  else:
    print("No")