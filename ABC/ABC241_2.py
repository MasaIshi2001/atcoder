n,m = (int(x) for x in input().split())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

flag = 0
for i in b_list:
    if i in a_list:
        a_list.remove(i)
    else:
        flag = 1
        break

if flag == 1:
    print("No")
else:
    print("Yes")