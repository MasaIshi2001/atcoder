n = int(input())
ab_lis = []
for i in range(n):
    a,b = (int(x) for x in input().split())
    ab_lis.append([a,b])

ans = 2**n
hikukazu = 0
tmp0 = 0

for i in range(n):
    if i == 0:
        past_a = ab_lis[i][0]
        past_b = ab_lis[i][1]
    else:
        tmp = 0
        if past_a == ab_lis[i][0]:
            tmp += 1
        if past_b == ab_lis[i][0]:
            tmp += 1
        if past_a == ab_lis[i][1]:
            tmp += 1
        if past_b == ab_lis[i][1]:
            tmp += 1
        
        hikukazu = 2*hikukazu + tmp

print((ans-hikukazu)%998244353)
