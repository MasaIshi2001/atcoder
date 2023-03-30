h,w = (int(x) for x in input().split())
cw_lis = []
for i in range(h):
    cw_line = list(map(int,input().split()))
    cw_lis.append(cw_line)

cnt_lis = [0 for i in range(w)]

for i in cw_lis:
    for j in range(len(i)):
        if i[j] == "#":
            cnt_lis[i] += 1


print(i)