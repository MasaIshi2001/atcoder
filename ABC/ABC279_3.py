import numpy as np
h,w =(int(x) for x in input().split())
s_list = []
for i in range(h):
    s = list(str(input()))
    s_list.append(s)
t_list = []
for i in range(h):
    t = list(str(input()))
    t_list.append(t)
 
s_list2 = np.array(s_list).T.tolist()
t_list2 = np.array(t_list).T.tolist()
 
s_list3 = []
for i in s_list2:
  s_list3.append("".join(i))
  
t_list3 = []
for i in t_list2:
  t_list3.append("".join(i))
 
 
s_dic = {}
for i in s_list3:
    if i not in s_dic.keys():
        s_dic[i] = 0
    s_dic[i] = s_dic[i] + 1
 
t_dic = {}
for i in t_list3:
    if i not in t_dic.keys():
        t_dic[i] = 0
    t_dic[i] = t_dic[i] + 1
 
s_dic2 = sorted(s_dic.items())
t_dic2 = sorted(t_dic.items())
 
if s_dic2 == t_dic2:
    print("Yes")
else:
    print("No")
