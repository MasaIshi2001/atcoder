n,a,b = (int(x) for x in input().split())
flag = False
flag1 = False
tmp = ""
for i in range(n):
  flag = not(flag)
  for j in range(a):
    flag1 = False
    for l in range(n):
      flag1 = not(flag1)
      for k in range(b):
        if flag == True:
          if flag1 == True:
            tmp += "."
          else:
            tmp += "#"
        else:
          if flag1 == True:
            tmp += "#"
          else:
            tmp += "."
    print(tmp)
    tmp = ""

