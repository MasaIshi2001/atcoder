import itertools


n = int(input())
a_list = []
for i in range(n):
    a_line = list(map(int,input().split()))
    a_list.append(a_line)

m = int(input())
xy_list = []
for i in range(m):
    x,y = (int(x) for x in input().split())
    xy_list.append([x,y])

kenaku = [[0 for i in range(n)] for j in range(n)]

for i in xy_list: #険悪なやつを示す隣接行列を生成
    kenaku[i[0]-1][i[1]-1] = True
    kenaku[i[1]-1][i[0]-1] = True

sousya = "".join(str(_) for _ in list(range(n)))
s_pattern = itertools.permutations(sousya,n)
ans = 100000

for i in s_pattern:
    flag = True
    sum = 0
    for j in range(n-1):
        if kenaku[int(i[j])][int(i[j+1])] == True:
            flag = False

    for k in range(n):
        sum += a_list[int(i[k])][k]

    if flag == True:
        ans = min(ans,sum)

        
if ans == 100000:
    print(-1)
else:
    print(ans)



