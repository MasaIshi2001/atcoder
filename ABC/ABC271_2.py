n,q = (int(x) for x in input().split())
s_list = []
for i in range(n):
    s_line = list(map(int,input().split()))
    s_list.append(s_line)

q_l = []
for i in range(q):
    q_line = list(map,input().split())
    q_l.append(q_line)

for i in q_l:
    print(s_list[i[0]-1][q[1]])

