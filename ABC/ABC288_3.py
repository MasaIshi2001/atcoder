n,m = (int(x) for x in input().split())
ab_lis = []
for i in range(m):
    a,b = (int(x) for x in input().split())
    ab_lis.append([a,b])

ab_dict = {}
for i in ab_lis:
    if i[0] not in ab_dict.keys():
        ab_dict[i[0]] = []
    ab_dict[i[0]].append(i[1])
    if i[1] not in ab_dict.keys():
        ab_dict[i[1]] = []
    ab_dict[i[1]].append(i[0])


visited = [0 for i in range(n)]
renketu_num = 0
stack = []
for i in range(n):
    if visited[i+1] == 0:
        renketu_num += 1
        stack.append(i+1)
        while len(stack) != 0:
            q = stack.pop()
            for j in ab_dict[q]:
                if visited[i+1] == 0:
                    visited[i+1] = 1
                    for k in j:
                        stack.append(k)

print(renketu_num)