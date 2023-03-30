from collections import defaultdict

n = int(input())

x_list = []
y_list = []
for i in range(n):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

s = str(input())
xy_dict = defaultdict(list)

for i in range(len(s)):
    xy_dict[y_list[i]].append([s[i],x_list[i]])

rl_list = []
r_pos = 2*10**5 + 1
l_pos = -1
for i in xy_dict.values():
    if len(i) > 1:
        for j in i:
            if j[0] == "R":
                r_pos = min(j[1],r_pos)
            elif j[0] == "L":
                l_pos = max(j[1],l_pos)

        if r_pos < l_pos:
            print("Yes")
            exit()

    r_pos = 2*10**5 + 1
    l_pos = -1

print("No")    



