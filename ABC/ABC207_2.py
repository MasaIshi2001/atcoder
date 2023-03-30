import math
a,b,c,d = (int(x) for x in input().split())
if d*c - b <= 0:
    print(-1)
else:
    print(math.ceil(a/(d*c - b)))

