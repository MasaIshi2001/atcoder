a,b,c,d,e = (int(x) for x in input().split())

lis = [a,b,c,d,e]

lis.sort()
cntLis = []
cnt = 1
for i in range(len(lis)):
    if len(lis)-1 > i >= 1:
        if past == lis[i]:
            cnt = cnt + 1
        else:
            cntLis.append(cnt)
            cnt = 1
    if i == len(lis)-1:
        cntLis.append(cnt)

    past = lis[i] 

if cntLis == [2,3] or cntLis == [3,2]:
    print("Yes")
else:
    print("No")

