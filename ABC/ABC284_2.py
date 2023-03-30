t = int(input())
lis = []
for i in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    lis.append(num)

for i in lis:
    cnt = 0
    for j in i:
        if j % 2 == 1:
            cnt += 1
    print(cnt)
