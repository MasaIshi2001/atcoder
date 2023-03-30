import math
n = int(input())
xy_lis = []
for i in range(n):
    x,y = (int(x) for x in input().split())
    xy_lis.append([x,y])


ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for l in range(j+1,n):
            menseki = abs(0.5*((xy_lis[i][1] - xy_lis[j][1])*(xy_lis[i][0] - xy_lis[l][0]) - (xy_lis[i][1] - xy_lis[l][1])*(xy_lis[i][0] - xy_lis[j][0])))
            if menseki != 0:
                ans += 1

print(ans)
