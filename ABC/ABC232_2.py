s = str(input())
s_lis = list(s)
t = str(input())
t_lis = list(t)

for i in range(len(s)):
    a = ord(s_lis[i])
    b = ord(t_lis[i])
    if i >= 1:
        if a-b >= 0:
            sa = a-b
        else:
            sa = a + 26 - b
        if past != sa:
           print("No")
    if a-b >= 0:
        past = a-b
    else:
        past = a + 26 - b

print("Yes")
