import math
x1,y1,x2,y2 = (int(x) for x in input())

dist = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
if x1 > x2:
    st_x = x2
    fi_x = x1
else:
    st_x = x1
    fi_x = x2

if y1 > y2:
    st_y = y2
    fi_y = y1
else:
    st_y = y1
    fi_y = y2

if dist < 6:
    for i in range(st_x-3,fi_x+3):
        for j in range(st_y-3,fi_y+3):
            if math.sqrt(((x1-i)**2)+((y1-j)**2)) == 5:
                if math.sqrt(((x2-i)**2)+((y2-j)**2)) == 5:
                    print("Yes")
                    exit()


print("No")
    