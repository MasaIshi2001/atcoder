x,y,n = (int(x) for x in input().split())
if 3*x >= y:
    yANum = n//3

    xANum = n%3

    print(yANum*y + xANum*x)

else:
    print(x*n)