h,w = (int(x) for x in input().split())
a_list = []
sum_yoko_list = []
for i in range(h):
    a_line = list(map(int,input().split()))
    sum_yoko_list.append(sum(a_line))
    a_list.append(a_line)


sum_tate_list = []
sum_tate = 0

for i in range(w):
    for j in range(h):
        sum_tate = sum_tate + a_list[j][i]
    
    sum_tate_list.append(sum_tate)
    sum_tate = 0

ans_list = []
ans_line = ''

for i in range(h):
    for j in range(w):
        ans_line += str(sum_yoko_list[i] + sum_tate_list[j] - a_list[i][j]) + " "
    
    ans_list.append(ans_line)
    ans_line=''

for i in ans_list:
    print(i)
    