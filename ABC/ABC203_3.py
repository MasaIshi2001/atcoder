n,k = (int(x) for x in input().split())
ab_lis = []
for i in range(n):
    a,b = (int(x) for x in input().split())
    ab_lis.append([a,b])

mura_bonus = {}
for i in ab_lis:
    if i[0] not in mura_bonus.keys():
        mura_bonus[i[0]] = i[1]
    else:
        mura_bonus[i[0]] += i[1]

mura_bonus2 = sorted(mura_bonus.items())

pos = 0
for i in mura_bonus2:
    if k - i[0] < 0:
        pos += k
        print(pos)
        break
    else:
        k = k - i[0]
        k = k + i[1]
        pos = pos + i[0]

pos = pos + k
print(pos)



