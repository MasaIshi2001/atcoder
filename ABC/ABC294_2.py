h,w = (int(x) for x in input().split())
a_lis = []
for i in range(h):
    a_line = list(map(int,input().split()))
    a_lis.append(a_line)

ans = []
for i in a_lis:
    tmp = []
    for j in i:
        if j == 0:
            tmp.append(".")
        else:
            tmp.append(chr(64+j))
    ans.append(tmp)

for i in ans:
    print(*i)
