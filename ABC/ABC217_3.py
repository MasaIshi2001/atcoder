n = int(input())
p_list = list(map(int,input().split()))
q_list = [0 for i in range(n)]
for i in range(n):
    q_list[p_list[i]] = i

for i in q_list:
    print(q_list)
