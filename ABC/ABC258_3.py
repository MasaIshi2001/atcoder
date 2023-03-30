from collections import deque

n,q = (int(x) for x in input().split())
s = str(input())
s_list = list(s)
query_list = []
for i in range(q):
    query = list(map(int,input().split()))
    query_list.append(query)

for i in query_list:
    if i[0] == 1:
        start = n - i[1]
        temp_line = s_list[start:n]
        del s_list[start:n]
        temp_line.reverse()
        s_list2 = deque(s_list)
        s_list2.appendleft(temp_line)
    if i[0] == 2:
        s_list2 = list(s_list2)
        print(s_list2[i[1]-1])

