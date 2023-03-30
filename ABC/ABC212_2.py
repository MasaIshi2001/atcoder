s = input()
s_lis = list(s)
s_set = set(s_lis)
if len(s_set) == 1:
    print("Weak")
    exit()

tmp_num = -1
cnt = 0
for i in range(len(s_lis)):
    if i > 0:
        if s_lis[i] == tmp_num:
            cnt = cnt + 1
    tmp_num = s_lis[i] + 1
    if tmp_num == 10:
        tmp_num = 0

if cnt == len(s_lis) - 1:
    print("Weak")
    exit()

print("Strong")
