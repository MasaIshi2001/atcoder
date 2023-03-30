a_list = list(map(int,input().split()))
a_list.sort()
if a_list[2] - a_list[1] == a_list[1] - a_list[0]:
    print("Yes")
else:
    print("No")
