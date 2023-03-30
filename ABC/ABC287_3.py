n,m = (int(x) for x in input().split())

if m != n-1:
    print("No")
    exit()

v_lis = []
for i in range(m):
    a,b = (int(x) for x in input().split())
    v_lis.append([a,b])


v_dict = {}
for i in v_lis:
    if i[0] not in v_dict.keys():
        v_dict[i[0]] = []
    v_dict[i[0]].append(i[1])
    if i[1] not in v_dict.keys():
        v_dict[i[1]] = []
    v_dict[i[1]].append(i[0])

visited = [0 for i in range(n)]
stack = []
stack.append(1)

while len(stack) != 0:
    q = stack.pop()
    if q in v_dict.keys():
        if len(q) > 2:
            print("No")
            exit()
        for j in q:
            if visited[j-1] != 1:
                visited[j-1] = 1
                stack.append(j)

if min(visited) == 0:
    print("No")
else:
    print("Yes")
