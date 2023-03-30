import numpy as np

n,m = (int(x) for x in input().split())
a_list = list(map(int,input().split()))

a_lis = np.array(a_list)
kake_lis = np.array(list(range(1,m+1)))

ans = 0
for i in range(n-m+1):
    sum1 = a_lis[i:i+m]
    sum1 = sum1*kake_lis
    ans = max(np.sum(sum1),ans)

print(ans)