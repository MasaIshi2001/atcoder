a,b =(int(x) for x in input().split())
x = (2*b/a)**(-2/3) - 1
x = int(x)
x2 = x + 1
if x < 0:
    print(a)
else:
    ans = min(b*x+a/(x+1)**(1/2),b*x2+a/(x2+1)**(1/2))
    print('{:.06f}'.format(ans))