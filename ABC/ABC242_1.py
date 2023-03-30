a,b,c,x = (int(x) for x in input().split())

if a>=x:
    print(1)
elif a<x and x<=b:
    print(c/(b-a))
else:
    print(0)