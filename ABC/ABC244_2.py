n = int(input())
t = str(input())

x = 0
y = 0

r_count = 0

for i in range(n):
    if t[i] == 'R':
        r_count = r_count + 1

    elif t[i] == 'S':
        if r_count%4 == 0:
            x = x+1
        elif r_count%4 == 1:
            y = y-1
        elif r_count%4 == 2:
            x = x-1
        elif r_count%4 == 3:
            y = y+1
        
print(str(x) + " " + str(y))