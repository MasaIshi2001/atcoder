n,w = (int(x) for x in input().split())

ab_lis = []
for i in range(n):
    a,b = (int(x) for x in input().split())
    ab_lis.append([a,b])

ab_lis.sort(reverse=True)

umasa = 0

for i in ab_lis:
    if w >= i[1]:
        umasa += i[1]*i[0]
        w = w - i[1]
    else:
        umasa += w*i[0]
        break

    if w == 0:
        break

print(umasa)
