import math

h,w = (int(x) for x in input().split())

if h==1 or w == 1:
    print(h*w)
    
else:
    tate = math.ceil(h/2)
    yoko = math.ceil(w/2)

    print(tate*yoko)

