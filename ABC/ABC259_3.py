import re

s = str(input())
t = str(input())

ansline = []
i = 0
while len(s)-1 >= i :
    roop = 0
    ansline.append(s[i])
    if i+1 <= len(s)-1:
      while s[i] == s[i+1]:
        roop = 1
        i = i + 1
          
        
    if roop > 0:
        ansline.append("+")
    i = i + 1
    

ans = "".join(ansline)

pattern = re.compile(ans)

if bool(pattern.fullmatch(t)) == True:
        print("Yes")
else:
        print("No")