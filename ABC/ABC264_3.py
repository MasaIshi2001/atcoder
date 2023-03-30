from collections import defaultdict

h,w = (int(x) for x in input().split())

f_lis = []
for i in range(h):
    a_line = list(map(int,input().split()))
    f_lis.append(a_line)

h2,w2 = (int(x) for x in input().split())

s_lis = []
for i in range(h2):
    b_line = list(map(int,input().split()))
    s_lis.append(b_line)

check_lis = [[0 for i in range(h)] for j in range(w)]
for i in range(h2):
    for j in range(w2):
        for k in range(h):
            for g in range(w):
                if s_lis[i][j] == f_lis[k][g]:
                    check_lis[k][g] == 1

c_dic = {}               
for i in range(len(check_lis)):
    for j in range(len(i)):
        if check_lis[i][j] == 1:
            if i not in c_dic:
                c_dic[i] = []
            c_dic[i].append([i,j])

print(c_dic)
