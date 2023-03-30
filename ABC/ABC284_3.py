n,m = (int(x) for x in input().split())
uv_lis = []
for i in range(m):
    u,v = (int(x) for x in input().split())
    uv_lis.append([u,v])

if m == 0:
  print(n)
  exit()

rinsetu = []
checked = [0 for i in range(n)]
dict = {}

for i in uv_lis:
    if i[0] not in dict.keys():
        dict[i[0]] = []
    dict[i[0]].append(i[1])
    if i[1] not in dict.keys():
        dict[i[1]] = []
    dict[i[1]].append(i[0])

tmp = []
cnt = 0
for i in range(n):
    tmp = [i+1]
    if checked[i] == 0:
        checked[i] = 1
        while len(tmp) != 0:
            n = tmp.pop()
            if n in dict.keys():
            	tmplis = dict[n]
                for j in tmplis:
                    if checked[j-1] == 0:
                        tmp.append(j)
                        checked[j-1] = 1
        cnt += 1

print(cnt)