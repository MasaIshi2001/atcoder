from collections import defaultdict

n,m = (int(x) for x in input().split())
a_lis = list(map(int,input().split()))
b_lis = list(map(int,input().split()))

a_pos = 0
b_pos = 0
ans_pos = 1
tmp1 = []
tmp2 = []

while a_pos < len(a_lis) and b_pos < len(b_lis):
    if a_lis[a_pos] < b_lis[b_pos]:
        tmp1.append(ans_pos)
        a_pos += 1
    else:
        tmp2.append(ans_pos)
        b_pos += 1
    ans_pos += 1

if a_pos == len(a_lis):
    lim = len(b_lis) - b_pos 
    for i in range(lim):
        tmp2.append(ans_pos)
        ans_pos += 1
else:
    lim = len(a_lis) - a_pos 
    for i in range(lim):
        tmp1.append(ans_pos)
        ans_pos += 1
print(*tmp1)
print(*tmp2)
