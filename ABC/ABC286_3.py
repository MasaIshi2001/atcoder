n,a,b = (int(x) for x in input().split())
s = str(input())

s += s
ans = 0

for i in range(n):
    tmp = a*i
    for j in range(n//2):
        if s[j+i] != s[n-j+i-1]:
            tmp += b

    if i==0:
        ans = tmp
    else:
        ans = min(ans,tmp)

print(ans)

