from curses.ascii import islower, isupper


s = str(input())
s_lis = list(s)
for i in range(len(s_lis)):
    if (i+1)%2 == 1:
        if s_lis[i].islower():
            print("No")
            exit()
    if (i+1)%2 == 0:
        if s_lis[i].isupper():
            print("No")
            exit()
print("Yes")