n = int(input())
a_list = list(map(int,input().split()))
q = int(input())
q_list = []
for i in range(q):
    q = list(map(int,input().split()))
    q_list.append(q)

for i in q_list:
    if i[0] == 1:
        a_list[i[1]-1] = i[2]
    elif i[0] == 2:
        print(a_list[i[1]-1])