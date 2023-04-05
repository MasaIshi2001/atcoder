n = int(input())
t_lis = []
for i in range(n):
    tmp = list(map(int,input().split()))
    t_lis.append(tmp)

hidari_1 = 0
migi_1 = 0

hidari_2 = 0
migi_2 = 0

ans = 0
for i in range(n):
    for j in range(i+1,n):
        if t_lis[i][0] == 1:
            hidari_1 = t_lis[i][1]
            migi_1 = t_lis[i][2]
        elif t_lis[i][0] == 2:
            hidari_1 = t_lis[i][1]
            migi_1 = t_lis[i][2]-0.1
        elif t_lis[i][0] == 3:
            hidari_1 = t_lis[i][1]+0.1
            migi_1 = t_lis[i][2]
        elif t_lis[i][0] == 4:
            hidari_1 = t_lis[i][1]+0.1
            migi_1 = t_lis[i][2]-0.1
        
        if t_lis[j][0] == 1:
            hidari_2 = t_lis[j][1]
            migi_2 = t_lis[j][2]
        elif t_lis[j][0] == 2:
            hidari_2 = t_lis[j][1]
            migi_2 = t_lis[j][2]-0.1
        elif t_lis[j][0] == 3:
            hidari_2 = t_lis[j][1]+0.1
            migi_2 = t_lis[j][2]
        elif t_lis[j][0] == 4:
            hidari_2 = t_lis[j][1]+0.1
            migi_2 = t_lis[j][2]-0.1

        if migi_1 >= hidari_2 and hidari_1 <= migi_2:
            ans += 1
        elif hidari_1 <= hidari_2 and migi_2 <= migi_1:
            ans += 1
        elif hidari_2 <= hidari_1 and migi_1 <= migi_2:
            ans += 1
        elif migi_2 >= hidari_1 and hidari_2 <= migi_1:
            ans += 1

print(ans)
        

