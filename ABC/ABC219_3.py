from collections import defaultdict
x = str(input())
n = int(input())
s_lis = []
for i in range(n):
    s = str(input())
    s_lis.append(s)

s_dic = defaultdict(int)

for i in range(len(x)):
    s_dic[x[i]] = i

ans = defaultdict(list)

for i in s_lis:
    for j in range(len(i)):
        ans[i].append(s_dic[i[j]])

ans1 = sorted(ans.items(),key=lambda x: x[1])
print(ans)
for i in ans1:
    print(i[0])