import difflib
import math



def takahashi(m):
    global t_list
    t_list = ''
    for i in W_list:
        if m <= i:
            t_list = t_list + str(1)
        elif m > i:
            t_list = t_list + str(0)
    if t_list == s:
        return 0
    elif s.count("0") <= t_list.count("0"): #探索時点で子供の方が多く出てしまったら
        return 1
    elif s.count("1") <= t_list.count("1"): #探索時点で大人の方が多く出たら
        return 2




n = int(input())
s = str(input())
W_list = list(map(int,input().split()))

right = max(W_list)
left = min(W_list)
cnt = 0

while right - left > 1:
    
    mid = (right + left)/2
    mid = math.floor(mid)
    print(mid)
    if takahashi(mid) == 0:
        break
    elif takahashi(mid) == 1:
        right = mid
    elif takahashi(mid) == 2:
        left  = mid

for i in range(n):
    if s[i] == t_list[i]:
        cnt = cnt + 1

print(cnt)
