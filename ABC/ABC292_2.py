n,q = (int(x) for x in input().split())
q_lis = []
for i in range(q):
    a,b = (int(x) for x in input().split())
    q_lis.append([a,b])

sensyu = [2 for i in range(n)]
for i in q_lis:
    if i[0] == 1:
        q_lis[i[1]-1] -= 1
    elif i[0] == 2:
        q_lis[i[1]-1] = 0
    else:
        if q_lis[i[1]-1] == 0:
            print("Yes")
        else:
            print("No")