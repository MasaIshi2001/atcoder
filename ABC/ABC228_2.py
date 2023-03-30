from tabnanny import check


n,x = (int(x) for x in input().split())
a_lis = list(map(int,input().split()))

dicti = {}
for i in range(len(a_lis)):
    dicti[i+1] = a_lis[i]

check_lis = [0]*n
check_lis[x-1] = 1
tugi = dicti[x]
cnt = 1

while check_lis[tugi-1] != 1:
    check_lis[tugi-1] = 1
    tugi = dicti[tugi]
    cnt = cnt + 1
print(cnt)