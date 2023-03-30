from collections import defaultdict
n = int(input())
a_lis = list(map(int,input().split()))
q = int(input())
q_lis = []
for i in range(q):
    tmp = list(map(int,input().split()))
    q_lis.append(tmp)

reset = 0
rflag = False
zrfalg = False
zoubun = defaultdict(int)
tmp = [0 for i in range(n)]

for i in q_lis:
    if i[0] == 1:
        reset = i[1]
        rflag = True
        zoubun = defaultdict(int)
    elif i[0] == 2:
        zoubun[i[1]-1] += i[2]
    else:
        if rflag == False:
            print(a_lis[i[1]-1]+zoubun[i[1]-1])
        else:
            print(reset+zoubun[i[1]-1])
