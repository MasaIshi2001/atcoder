from collections import defaultdict
n,q = (int(x) for x in input().split())
a_lis = list(map(int,input().split()))
xk_lis = []
for i in range(q):
    x,k = (int(x) for x in input().split())
    xk_lis.append([x,k])

num_dic = defaultdict(list)

for i in range(len(a_lis)):
    num_dic[a_lis[i]].append(i+1)

for x,k in xk_lis:
    if len(num_dic[x]) >= k:
        print(num_dic[x][k-1])
    else:
        print(-1)