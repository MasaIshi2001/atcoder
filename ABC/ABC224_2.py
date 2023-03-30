h,w = (int(x) for x in input().split())

a_list = []
for i in range(h):
    a_line = list(map(int,input().split()))
    a_list.append(a_line)

for i1 in range(h-2):
    for i2 in range(i1+1,h-1):
        for j1 in range(w-2):
            for j2 in range(j1+1,w-1):
                if a_list[i1][i1] + a_list[i2][i2] > a_list[i2][j1] + a_list[i1][j2]:
                    print("No")
                    exit()


print("Yes")