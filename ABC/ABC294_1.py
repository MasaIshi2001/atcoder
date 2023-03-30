n = int(input())
num = list(map(int,input().split()))

ans = []
for i in num:
    if i%2 == 0:
        ans.append(i)

print(*ans)
