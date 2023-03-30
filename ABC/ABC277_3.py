from collections import defaultdict,deque
 
n = int(input())
ab_dic = defaultdict(list)
for i in range(n):
    a,b = (int(x) for x in input().split())
    ab_dic[a].append(b)
    ab_dic[b].append(a)
 
dfs = deque()
visited = {1}
if 1 in ab_dic.keys():
  for k in ab_dic[1]:
    dfs.append(k)
    
now = 1
 
while len(dfs) > 0:
    tmp = dfs.pop()
    now = max(tmp,now)
    if tmp in ab_dic.keys():
        for j in ab_dic[tmp]:
            if j not in visited:
                visited.add(j)
                dfs.append(j)         
 
print(now)
