h,w,r,c = (int(x) for x in input().split())
n = int(input())
rc_list = []
for i in range(n):
    r,c = (int(x) for x in input().split())
    rc_list.append([r,c])
dl_lis = []
q = int(input())
for j in range(q):
    d,l = (int(x) for x in input().split())
    dl_lis.append([d,l])

Tmap = [[0 for i in range(w)] for j in range(h)]

for i in rc_list:
    Tmap[i[0],i[1]] = 1

stPoint = [r,c]

for i in dl_lis:
    if 

