import math
 
def checker(midian,b_val):
    if a_list[midian] < b_val:
        return 1
    else:
        return -1
 
 
n = int(input())
a_list = list(map(int,input().split()))
q = int(input())
b_lis = []
for i in range(q):
    b = int(input())
    b_lis.append(b)
 
a_list.sort()
 
r = n - 1
l = 0
for i in b_lis:
    
    while r-l > 1:
        mid = math.floor((r+l)/2)
        if checker(mid,i) == 1:
            l = mid
        elif checker(mid,i) == -1:
            r = mid

    print(min(abs(i-a_list[l]),abs(i-a_list[r])))
    r = n - 1
    l = 0