n = int(input())
tmp = list(map(int,input().split()))

visited = [0 for i in range(n)]

for i in range(len(tmp)):
    if visited[i] == 0:
        visited[tmp[i]] = 1

for i in range(len(tmp)):
    if tmp[i] == 0:
        print(i+1)