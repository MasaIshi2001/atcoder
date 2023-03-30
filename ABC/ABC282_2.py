n,m = (int(x) for x in input().split())
p = []
for i in range(n):
    p_line = str(input())
    p.append(p_line)
cnt = 0
tmp = 0
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(m):
            if p[i][k] == "o" or p[j][k] == "o":
                tmp += 1
        if tmp == m:
            cnt += 1
        tmp = 0

print(cnt)

                

