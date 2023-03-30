import math
n = int(input())
apx_list = []
for i in range(n):
    a,p,x = (int(x) for x in input().split())
    apx_list.append([a,p,x])

ok_tenpo = [10**9]*n
for i in range(n):
    if apx_list[i][2] - int(math.ceil(2*apx_list[i][0]-apx_list[i][0])) > 0:
        ok_tenpo[i] = apx_list[i][1]

print(min(ok_tenpo))



