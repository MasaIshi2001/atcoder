n,m = (int(x) for x in input().split())
s_lis = []
for i in range(n):
    s = str(input())
    s_lis.append(s)
t_lis = []
for i in range(m):
    t = str(input())
    t_lis.append(t)

kouho = []
for i in range(n):
    k = s_lis[i][3:]
    kouho.append(k)

ans = 0
for i in range(n):
    for j in range(m):
        if t_lis[j] == kouho[i]:
            ans += 1
            break

print(ans)