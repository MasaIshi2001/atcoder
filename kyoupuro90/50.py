import math

n,l = (int(x) for x in input().split())

max_l_num = n//l

c_num = 0

for i in range(max_l_num+1):
    if i == 0:
        c_num += 1
    else:
        num = n - (i*(l-1))
        c_num += math.comb(num,i)

print(c_num%((10**9)+7))