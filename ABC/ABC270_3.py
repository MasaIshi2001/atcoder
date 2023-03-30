from collections import deque

n,x,y = (int(x) for x in input().split())
uv_list = []
for i in range(n-1):
    u,v = (int(x) for x in input().split())
    uv_list.append([u,v])

rinsetu = [[] for i in range(n)] 
for i in uv_list:
    rinsetu[i[0]-1].append(i[1])
    rinsetu[i[1]-1].append(i[0])

visit = [False for i in range(n)]
visit[x-1] = True
keiro = [0 for i in range(n)]

q = deque()
q.append(x)

#ここから深さ優先探索の探索部
while len(q) != 0:
    now = q.popleft()
    visit[now-1] = True
    for nx in rinsetu[now-1]:
        if visit[nx-1] == False:
            q.append(nx)
            keiro[nx-1] = now
            if nx == y:
                break
#ここまで深さ優先探索の探索部
s=y
ans = [y]
while s!=x:
    s = keiro[y-1]
    ans.append(s)
    y = s

ans.reverse()

for x in ans:
    print(x,end=" ")