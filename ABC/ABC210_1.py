n,a,x,y = (int(x) for x in input().split())
if n <= a:
    print(n*x)
else:
    print(a*x + (n-a)*y)