n,k = (int(x) for x in input().split())
s_lis = []
for i in range(n):
    s = str(input())
    s_lis.append(s)

tmp_lis = s_lis[:k]
tmp_lis.sort()
for i in tmp_lis:
    print(i)