n,m,x,t,d = (int(x) for x in input().split())
if x <= m:
    print(t)
else:
    print(t-d*(m-x))