
h,m = (str(x) for x in input().split())
h = h.zfill(2)
m = m.zfill(2)
a = int(h[0])
b = int(h[1])
c = int(m[0])
d = int(m[1])

zi = a*10+c
hun = b*10+d
while zi >= 24 or hun > 59:
    if c >= 4:
        c = 0
        d = 0
        b = b + 1

    if b >= 6:
        c = 0
        d = 0
        b = 0
        a = a + 1
    
    if a==2 and b == 4:
        a = 0
        b = 0

    zi = a*10+c
    hun = b*10+d

print(str(a*10+b) + " " + str(c*10+d))

