n,m = (int(x) for x in input().split())
s_list = list(map(int,input().split()))
t_list = set(map(int,input().split()))

for i in s_list:
    if i in t_list:
        print("Yes")
    else:
        print("No")