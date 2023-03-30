n = int(input())
a_list = list(map(int,input().split()))
comp_list = [int(i+1) for i in range(n)]
a_list.sort()
if comp_list == a_list:
    print("Yes")
else:
    print("No")