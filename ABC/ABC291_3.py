n = int(input())
s = str(input())

x_pos = 0
y_pos = 0

pos_dict = {}

for i in range(len(s)):
    if s[i] == "R":
        x_pos += 1
    
    if s[i] == "L":
        x_pos -= 1

    if s[i] == "U":
        y_pos += 1

    if s[i] == "D":
        y_pos -= 1

    if (x_pos,y_pos) not in pos_dict.keys:
        pos_dict[(x_pos,y_pos)] = True
    else:
        print("Yes")
        exit()

print("No")