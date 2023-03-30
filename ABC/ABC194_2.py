n = int(input())
ab_list = []
for i in range(n):
    a,b = (int(x) for x in input().split())
    ab_list.append([a,b])

id_lis = []
time_lis = []
for i in range(n):
    for j in range(n):
        if i == j:
            time_lis.append(ab_list[i][0]+ab_list[j][1])
            id_lis.append(i,j)
        else:
            time_lis.append(max(ab_list[i][0],ab_list[j][1]))
            id_lis.append(i,j)

print(min(time_lis))
