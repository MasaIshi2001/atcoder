n = int(input())
s_list = []
for i in range(n):
    s_line = str(input())
    s_list.append([s_line,i])

s_list2 = sorted(s_list)
count_list = [0]*n
onazi = 0

for i in range(n):
    if i != 0:
        if past_mozi == s_list2[i][0]:
            onazi = onazi + 1
            count_list[i] = onazi
        else:
            onazi = 0
    past_mozi = s_list2[i][0]


for i in range(n):
    if count_list[i] != 0:
        s_list2[i][0]= s_list2[i][0]+"("+str(count_list[i])+")"
    else:
        s_list2[i][0]= s_list2[i][0]

ans_list = sorted(s_list2,key=lambda x:x[1])
print(ans_list)