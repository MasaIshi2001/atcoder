r,c = (int(x) for x in input().split())
map_b = []
for i in range(c):
    tmp = input()
    map_b.append(list(tmp))

for j in range(c):
    for i in range(r):
        if map_b[i][j].isdecimal() == True:
            bom = int(map_b[i][j])
            map_b[i][j] = "."
            for n in range(c):
                for m in range(r):
                    if map_b[n][m] == "#":
                        if abs(n-j) + abs(m-r) <= bom:
                            map_b[n][m] = "."

for i in map_b:
    print("".join(i))

