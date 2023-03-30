import math

n = int(input())
a_lis = list(map(int,input().split()))

amari = [0 for i in range(200)]

for i in a_lis:
    amari[i%200] += 1

ans = 0
for i in amari:
    if i > 1:
        ans += math.factorial(i)/(2*math.factorial(i-2))

print(ans)
