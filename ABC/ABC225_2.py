from tabnanny import check


n = int(input())
ab_list = []
for i in range(n-1):
    a,b = (int(x) for x in input().split())
    ab_list.append([a,b])

check_lis = [0 for i in range(n)]

for i in ab_list:
    check_lis[i[0]] += 1
    check_lis[i[1]] += 1

if n-1 in check_lis:
    print("Yes")
else:
    print("No")