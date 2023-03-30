from collections import deque


n,q = (int(x) for x in input().split())

a_list = list(map(int,input().split()))

q_list = []
for i in range(q):
    t,x,y = (int(x) for x in input().split())
    q_list.append([t,x,y])

mv = 0

for i in q_list:
    if i[0] == 1:
        tmp = a_list[(i[1]-1-mv)%n]
        a_list[(i[1]-1-mv)%n] = a_list[(i[2]-1-mv)%n]
        a_list[(i[2]-1-mv)%n] = tmp

    elif i[0] == 2:
        mv = mv + 1

    elif i[0] == 3:
        print(a_list[(i[1]-1-mv)%n])