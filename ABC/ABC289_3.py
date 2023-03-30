from itertools import product

n,m = (int(x) for x in input().split())
num_lis = []
for i in range(m):
    num = list(map(int,input().split()))
    num_lis.append(num)

visited = [0 for i in range(n)]
ans = 0

for p in product((0, 1), repeat=n):
    print(p)
    for i in range(n):
        if p[i] == 1:
            for j in num_lis[i]:
                visited[j-1] = 1
    if sum(visited) == len(visited):
        ans += 1
    visited = [0 for i in range(n)]

print(ans)


