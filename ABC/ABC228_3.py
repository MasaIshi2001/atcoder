n,k = (int(x) for x in input().split())
p_lis = []
for i in range(n):
    p1,p2,p3 = (int(x) for x in input().split())
    p_lis.append([p1,p2,p3])

minMax = []
for i in p_lis:
    min = (i[0]+i[1]+i[2]+0)/4
    max = (i[0]+i[1]+i[2]+300)/4
    minMax.append([max,min])

tmp = sorted(minMax,reverse=True)

minLine = tmp[k-1][1]

for i in range(n):
    if minMax[i][0] >= minLine:
        print("Yes")
    else:
        print("No")