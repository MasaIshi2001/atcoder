n = int(input())
txy_lis = []
for i in range(n):
    t,x,y = (int(x) for x in input().split())
    txy_lis.append([t,x,y])

stPos = [0,0,0]
saitan_lis = []
kaisuu_lis = []

for i in txy_lis:
    zikan = i[0] - stPos[0]
    tate = i[1] - stPos[1]
    yoko = i[2] - stPos[2]
    saitan = tate + yoko
    kaisuu_lis.append(zikan)
    saitan_lis.append(abs(saitan))
    stPos[0] = zikan
    stPos[1] = tate
    stPos[2] = yoko

flag = 0
for i in range(len(saitan_lis)):
    if saitan_lis[i] - kaisuu_lis[i] < 0 and (kaisuu_lis[i] - saitan_lis[i])%2 == 0:
        flag += 1
    else:
        print("No")
        exit()

print("Yes")