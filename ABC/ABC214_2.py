s,t =(int(x) for x in input().split())
cnt = 0
for i in range(s+1):
    for j in range(s+1-i):
        for k in range(s+1-i-j):
            if i*j*k <= t:
                cnt = cnt + 1

print(cnt)