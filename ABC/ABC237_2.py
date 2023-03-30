h,w = (int(x) for x in input().split())
a_list = []
for i in range(h):
    a_line = list(map(int,input().split()))
    a_list.append(a_line)

b_list = []
for i in range(w):
    b_line = []
    for j in range(h):
        b_line.append(a_list[j][i])
    b_list.append(b_line)

for i in range(w):
    b_map = map(str,b_list[i])
    ans_line = " ".join(b_map)
    print(ans_line)