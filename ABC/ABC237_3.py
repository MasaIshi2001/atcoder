
s = str(input())
s_list = list(s)
flag = 0
fACnt = 0 #前のaの数
bACnt = 0 #後ろのaの数
for i in range(len(s_list)):
    if s_list[i] == 'a':
        fACnt = fACnt + 1
    else:
        break

for i in range(len(s_list)):
    if s_list[len(s_list)-(i+1)] == 'a':
        bACnt = bACnt + 1
    else:
        break

if fACnt == len(s_list): #全部aだったら
    print("Yes")
    exit()

if fACnt > bACnt: #前の方のaが後ろに対してたくさんあった場合、先頭にaをいくら付加しても無意味なので
    print("No")
    exit()

for i in range(fACnt,len(s_list)- bACnt): #それ以外つまり後ろの方がaをたくさん持っている場合、その差の分後ろを削って回文検査
    if s_list[i] != s_list[len(s_list) + fACnt - bACnt - (i+1)]:
        print("No")
        exit()
    
print("Yes")
