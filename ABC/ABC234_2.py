import numpy as np
n = int(input())
xy_list = []
for i in range(n):
    x,y = (int(x) for x in input().split())
    xy_line = [x,y]
    xy_list.append(xy_line)

len_lis = []
for i in range(len(xy_list)):
    for j in range(i+1,len(xy_list)):
        a = np.array(xy_list[i])
        b = np.array(xy_list[j])
        dis = np.linalg.norm(b-a)
        len_lis.append(dis)

print(max(len_lis))