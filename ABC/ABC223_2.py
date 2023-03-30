from collections import deque
s = str(input())
s_list = deque(s)

ans_list = []
ans_list.append(s)
for i in range(len(s_list)):
    s_list.rotate(1)
    ans = "".join(list(s_list))
    ans_list.append(ans)

ans_list.sort()
print(ans_list[0])
print(ans_list[len(ans_list)-1])