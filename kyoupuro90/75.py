import math
n =int(input())
rem = n
cnt = 0
 
ans_lis = []
roop = int(math.sqrt(n))
for i in range(1,roop):
    while rem%(i+1)==0:
        rem = rem//(i+1)
        ans_lis.append(i+1)
if rem != 1:
    ans_lis.append(rem)
 
n = len(ans_lis)
 
while 2**cnt < n:
    cnt = cnt + 1
 
print(cnt) 
