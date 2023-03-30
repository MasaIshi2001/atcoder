n = int(input())
s = int(input())
q = int(input())
q_list = []
for i in range(q):
    t,a,b = (int(x) for x in input().split())
    q_list.append([t,a,b])

indlis = list(s)
c_flag = 0

for i in q_list:
    if i[0] == 1:
        if c_flag == 0:
            tmp = indlis[i[1]-1]
            indlis[i[1]-1] = indlis[i[2]-1]
            indlis[i[2]-1] = tmp
        else:
            tmp = indlis[i[1]-1+n]
            indlis[i[1]-1+n] = indlis[i[2]-1-n]
            indlis[i[2]-1-n] = tmp
    if i[0] == 2:
        if c_flag == 0:
            c_flag = 1
        else:
            c_flag = 0



print("".join(indlis))


