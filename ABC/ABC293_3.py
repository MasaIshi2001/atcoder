def dfs(x, y):
    global ans
    # 上下左右への移動パターンで再起していく
    if x >= w or y >= h:       
        return
    if x == w-1 and y== h-1:
          sets = set(stack)
          if len(sets) == len(stack):
            ans += 1        
    stack[x+y] = a_lis[x][y]
    dfs(x+1, y)
    dfs(x, y+1)

h,w = (int(x) for x in input().split())
ans = 0
stack = [-1 for i in range(h+w-1)]
a_lis = []

for i in range(h):
    tmp = list(map(int,input().split()))
    a_lis.append(tmp)

dfs(0,0)
print(ans)