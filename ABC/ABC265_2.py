n,m,t = (int(x) for x in input().split())
a_list = list(map(int,input().split()))
bonus_lis = []
for i in range(m):
    x,y = (int(x) for x in input().split())
    bonus_lis.append([x,y])

heyaPos = 1
bonusPos = 0
for i in a_list:
    heyaPos = heyaPos + 1
    t = t - i
    if t <= 0:
        print("No")
        exit()

    if m != 0:
        if heyaPos == bonus_lis[bonusPos][0]:
            t = t + bonus_lis[bonusPos][0]
            if bonusPos < m-1:
                bonusPos = bonusPos + 1


print("Yes")
