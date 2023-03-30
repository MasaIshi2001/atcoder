s = str(input())
t = str(input())

if s == t:
    print("Yes")
    exit()

s_lis = list(s)

for i in range(len(s_lis)-1):
    
    tmp = s_lis[i]
    s_lis[i] = s_lis[i+1]
    s_lis[i+1] = tmp
    if "".join(s_lis) == t:
        print("Yes")
        exit()
    s_lis = list(s)

print("No")
            