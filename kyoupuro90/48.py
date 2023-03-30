n,k = (int(x) for x in input().split())
pt_lis = []
for i in range(n):
    a,b = (int(x) for x in input().split())
    pt_lis.append(b)
    pt_lis.append(a-b)

pt_lis.sort(reverse=True)

print(sum(pt_lis[0:k]))

