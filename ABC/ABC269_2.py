s_list = []
for i in range(10):
    s_line = str(input())
    s_list.append(s_line)

recnt = 0
sfl = 0
for i in s_list:

    recnt = recnt + 1
    if "#" in i:
        scnt = 0
        for j in range(i):
            if i[j] == "#":
                scnt = scnt + 1
        idx = i.index("#")
        c = idx + 1
        d = idx + scnt + 1
        if sfl == 0:
            sfl = 1
            a = recnt
    else:
        if sfl == 1:
            b = recnt

print(str(a) + " " + str(b))
print(str(c) + " " + str(d))
