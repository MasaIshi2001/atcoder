import math
r,x,y = (int(x) for x in input().split())
dis = math.sqrt(x**2 + y**2)
cnt = 0
tmp = 0

while tmp < dis:
    tmp += r
    cnt += 1

if cnt == 1 and tmp != dis:
    cnt = 2

print(cnt)