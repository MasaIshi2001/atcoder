s = str(input())

retu = [1,1,2,1,2,1,1]
if s[0] == "0":
    if s[1] == "0":
        retu[2] = retu[2] - 1
    if s[2] == "0":
        retu[4] = retu[4] - 1
    if s[3] == "0":
        retu[1] = retu[1] - 1
    if s[4] == "0":
        retu[3] = retu[3] - 1
    if s[5] == "0":
        retu[5] = retu[5] - 1
    if s[6] == "0":
        retu[0] = retu[0] - 1
    if s[7] == "0":
        retu[2] = retu[2] - 1
    if s[8] == "0":
        retu[4] = retu[4] - 1
    if s[9] == "0":
        retu[6] = retu[6] - 1
else:
    print("No")
    exit()

o_flag = 0
z_flag = 0

for i in retu:
    if i == 1 or i == 2:
        o_flag = o_flag + 1
        if o_flag == 1:
            z_flag = 0

        if o_flag == 2:
            if z_flag > 0:
                print("Yes")
                exit()
            else:
                o_flag = 1
    elif i == 0:
        z_flag = z_flag + 1

print("No")
