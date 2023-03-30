n,m =(int(x) for x in input().split())
ab_list = []
for i in range(m):
    a,b = (int(x) for x in input().split())
    ab_list.append([a,b])
 
rinsetu = {}
 
for i in ab_list:
    if i[0] not in rinsetu.keys():
        rinsetu[i[0]] = []
    rinsetu[i[0]].append(i[1])
 
    if i[1] not in rinsetu.keys():
        rinsetu[i[1]] = []
    rinsetu[i[1]].append(i[0])
 
for v in rinsetu.values():
    v.sort()
for i in range(n):
    if i+1 not in rinsetu.keys():
        print(0)
    else:
        print(len(rinsetu[i+1]),end = " ")
        print(*rinsetu[i+1])
