h1,h2,h3,w1,w2,w3 = (int(x) for x in input().split())

ab_list = []
for a in range(h1-2):
    a = a+1
    for b in range(h1-1-a):
        b = b+1
        if a+b > h1:
            break
        ab_list.append([a,b])

de_list = []
for d in range(h2-2):
    d = d+1
    for e in range(h2-1-d):
        e = e+1
        if d+e > h2:
            break
        de_list.append([d,e])

