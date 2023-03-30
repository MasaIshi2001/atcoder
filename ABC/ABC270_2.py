x,y,z = (int(x) for x in input().split())

if 0<=y<=x or 0>=y>=x:
    if 0<=z<=y or 0>=z>=y:
        print(abs(x))
    elif 0<y<z or 0>y>z:
        print(-1)
    else:
        print(abs(2*z) + abs(x))
else:
    print(abs(x))

    