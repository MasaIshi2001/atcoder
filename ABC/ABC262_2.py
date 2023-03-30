from typing import Counter


n,m = (int(x) for x in input().split())
uv_list = []

for i in range(m):
    u,v = (int(x) for x in input().split())
    uv_list.append([u,v])


dicti = {}
for i in uv_list:
    if i[0] not in dicti:
        dicti[i[0]] = []
    dicti[i[0]].append(i[1])

c_lis = [[0 for i in range(n)] for j in range(n)]
for i in uv_list:
    c_lis[i[0]-1][i[1]-1] = 1
    c_lis[i[1]-1][i[0]-1] = 1

counter = 0
for i,j in dicti.items():
    if len(j) >= 2:
        for k in range(len(j)):
            for m in range(k+1,len(j)):
                a1 = j[k]-1
                a2 = j[m]-1
                if c_lis[a1][a2] == 1:
                    counter = counter + 1
        

print(counter)