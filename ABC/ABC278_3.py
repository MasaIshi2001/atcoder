n,q = (int(x) for x in input().split())
t_list = []
for i in range(q):
    t,a,q = (int(x) for x in input().split())
    t_list.append([t,a,q])

c_dic = {}
for i in t_list:
    cnt = 0
    if i[0] == 1:
        if i[1] not in c_dic.keys():
            c_dic[i[1]] = {}
        c_dic[i[1]][i[2]] = 1
    elif i[0] == 2:
        if i[1] in c_dic.keys():
            dic = c_dic[i[1]]
            if i[2] in dic.keys():
                c_dic[i[1]][i[2]] = 0


    else:
        if i[1] in c_dic.keys():
            dic = c_dic[i[1]]
            if i[2] in dic.keys():
                if dic[2] == 1:
                    cnt = cnt + 1
        if i[2] in c_dic.keys():
            dic = c_dic[i[2]]
            if i[1] in dic.keys():
                if dic[1] == 1:
                    cnt = cnt + 1
        if cnt == 2:
            print("Yes")
        else:
            print("No")
            
