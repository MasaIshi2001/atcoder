n,m = (int(x) for x in input().split())
a_lis = list(map(int,input().split()))
b_lis = list(map(int,input().split()))

ans = 0
for i in b_lis:
    ans += a_lis[i-1]

print(ans)
