h,w = (int(x) for x in input().split())
g_list = []
for i in range(h):
    g_line = list(str(input()))
    g_list.append(g_line)

y = 0
x = 0
check_lis = [[0 for i in range(w)] for j in range(h)]

while True:
    if check_lis[y][x] == True:
        print(-1)
        exit()

    check_lis[y][x] = True

    if g_list[y][x] == "R" and x != w -1:
        x = x + 1
    elif g_list[y][x] == "L" and x != 0:
        x = x - 1
    elif g_list[y][x] == "D" and y != h -1:
        y = y + 1
    elif g_list[y][x] == "U" and y != 0:
        y = y - 1
    else:
        break

print(str(y+1) + " " + str(x+1))


