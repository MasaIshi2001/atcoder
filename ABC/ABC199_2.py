n = int(input())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
if min(b_list) - max(a_list) >= 0:
    print(min(b_list) - max(a_list) + 1)
else:
    print(0)