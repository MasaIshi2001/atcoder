from collections import deque

q = int(input())
query_list = []
for i in range(q):
    TX_list = list(map(int,input().split()))
    query_list.append(TX_list)

ans_list = deque()

for i in query_list:
    if i[0] == 1:
        ans_list.appendleft(i[1])
    elif i[0] == 2:
        ans_list.append(i[1])
    elif i[0] == 3:
        print(ans_list[i[1]-1])

